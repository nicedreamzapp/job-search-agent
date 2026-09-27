"""Unit tests for the LLM scorer.

Both HTTP backends (the local OpenAI-compatible server and the Anthropic
Messages API) are exercised by patching `urllib.request.urlopen` inside
`scorer`, so these tests run fully offline and never need an API key or a
local model.
"""

from __future__ import annotations

import io
import json
import os
import sys
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch

# Allow `python3 -m unittest discover tests` from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import scorer  # noqa: E402
from connectors.base import Job  # noqa: E402


def make_job(**overrides) -> Job:
    fields = {
        "id": "job-1",
        "source": "greenhouse",
        "company_slug": "acme",
        "company_name": "Acme",
        "title": "Staff Engineer",
        "location": "Remote",
        "url": "https://example.com/jobs/1",
        "description": "Build distributed systems.",
        "department": "Engineering",
    }
    fields.update(overrides)
    return Job(**fields)


class FakeResponse:
    """Minimal stand-in for the object `urlopen` returns as a context manager."""

    def __init__(self, payload):
        self._body = payload if isinstance(payload, bytes) else json.dumps(payload).encode("utf-8")

    def read(self):
        return self._body

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def local_payload(content: str) -> dict:
    return {"choices": [{"message": {"role": "assistant", "content": content}}]}


def anthropic_payload(content: str) -> dict:
    return {"content": [{"type": "text", "text": content}], "stop_reason": "end_turn"}


class RecordingUrlopen:
    """Returns queued responses in order and records every request sent."""

    def __init__(self, *responses):
        self.responses = list(responses)
        self.requests = []

    def __call__(self, req, timeout=None):
        self.requests.append(req)
        item = self.responses.pop(0)
        if isinstance(item, BaseException):
            raise item
        return FakeResponse(item)

    def body(self, index: int) -> dict:
        return json.loads(self.requests[index].data.decode("utf-8"))


LOCAL_ENV = {"ANTHROPIC_API_KEY": "", "JOBSCOUT_LLM_ENDPOINT": "http://llm.test:9000/"}
ANTHROPIC_ENV = {"ANTHROPIC_API_KEY": "sk-test-key"}


class ParseJsonResponseTests(unittest.TestCase):
    def test_plain_json(self):
        result = scorer._parse_json_response('{"score": 72, "rationale": "Solid fit."}')
        self.assertEqual((result.score, result.rationale, result.error), (72, "Solid fit.", None))

    def test_fenced_json(self):
        content = 'Here you go:\n```json\n{"score": 55, "rationale": "Meh."}\n```\nThanks!'
        result = scorer._parse_json_response(content)
        self.assertEqual((result.score, result.rationale, result.error), (55, "Meh.", None))

    def test_json_embedded_in_prose(self):
        result = scorer._parse_json_response('Result: {"score": 90, "rationale": "Great."} done')
        self.assertEqual((result.score, result.error), (90, None))

    def test_score_clamped_to_range(self):
        self.assertEqual(scorer._parse_json_response('{"score": 150}').score, 100)
        self.assertEqual(scorer._parse_json_response('{"score": -5}').score, 0)

    def test_string_score_is_coerced(self):
        self.assertEqual(scorer._parse_json_response('{"score": "81", "rationale": "x"}').score, 81)

    def test_non_numeric_score_defaults_to_zero(self):
        result = scorer._parse_json_response('{"score": "high", "rationale": "x"}')
        self.assertEqual((result.score, result.error), (0, None))

    def test_no_json_is_an_error(self):
        result = scorer._parse_json_response("I cannot score this job.")
        self.assertEqual(result.error, "no JSON in response")
        self.assertEqual(result.rationale, "I cannot score this job.")

    def test_malformed_json_is_an_error(self):
        result = scorer._parse_json_response("{score: 80, rationale: oops}")
        self.assertEqual(result.error, "could not parse score JSON")

    def test_pitch_field(self):
        result = scorer._parse_json_response('{"pitch": "  Hire me.  "}', expect_field="pitch")
        self.assertEqual((result.pitch, result.error), ("Hire me.", None))

    def test_missing_pitch_is_an_error(self):
        result = scorer._parse_json_response('{"score": 90}', expect_field="pitch")
        self.assertEqual(result.error, "no pitch field in response")


class LocalBackendTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.dict(os.environ, LOCAL_ENV)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_request_shape_and_success(self):
        fake = RecordingUrlopen(local_payload('{"score": 64, "rationale": "Decent."}'))
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "I am an engineer.")

        self.assertEqual((result.score, result.rationale, result.pitch, result.error), (64, "Decent.", "", None))
        self.assertEqual(len(fake.requests), 1)
        req = fake.requests[0]
        self.assertEqual(req.full_url, "http://llm.test:9000/v1/chat/completions")
        self.assertEqual(req.get_method(), "POST")
        body = fake.body(0)
        self.assertEqual(body["model"], scorer.DEFAULT_LOCAL_MODEL)
        prompt = body["messages"][0]["content"]
        self.assertIn("I am an engineer.", prompt)
        self.assertIn("Staff Engineer", prompt)

    def test_unreachable_server(self):
        fake = RecordingUrlopen(urllib.error.URLError("connection refused"))
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertEqual(result.score, 0)
        self.assertIn("local LLM unreachable", result.error)

    def test_non_json_body(self):
        fake = RecordingUrlopen(b"<html>502 Bad Gateway</html>")
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertIn("local LLM call failed", result.error)

    def test_unexpected_response_shape(self):
        fake = RecordingUrlopen({"choices": []})
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertIn("unexpected local LLM response", result.error)


class AnthropicBackendTests(unittest.TestCase):
    def setUp(self):
        patcher = patch.dict(os.environ, ANTHROPIC_ENV)
        patcher.start()
        self.addCleanup(patcher.stop)
        os.environ.pop("JOBSCOUT_ANTHROPIC_MODEL", None)

    def test_default_model_is_current(self):
        self.assertEqual(scorer.DEFAULT_ANTHROPIC_MODEL, "claude-sonnet-5")

    def test_request_shape_and_success(self):
        fake = RecordingUrlopen(anthropic_payload('{"score": 70, "rationale": "Good."}'))
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")

        self.assertEqual((result.score, result.rationale, result.error), (70, "Good.", None))
        req = fake.requests[0]
        self.assertEqual(req.full_url, "https://api.anthropic.com/v1/messages")
        self.assertEqual(req.get_header("X-api-key"), "sk-test-key")
        self.assertEqual(req.get_header("Anthropic-version"), "2023-06-01")
        body = fake.body(0)
        self.assertEqual(body["model"], "claude-sonnet-5")
        # Current models reject sampling params with a 400.
        self.assertNotIn("temperature", body)
        self.assertEqual(body["thinking"], {"type": "disabled"})

    def test_model_override_from_env(self):
        fake = RecordingUrlopen(anthropic_payload('{"score": 10, "rationale": "No."}'))
        with patch.dict(os.environ, {"JOBSCOUT_ANTHROPIC_MODEL": "claude-opus-5"}):
            with patch.object(scorer.urllib.request, "urlopen", fake):
                scorer.score_job(make_job(), "creds")
        self.assertEqual(fake.body(0)["model"], "claude-opus-5")

    def test_skips_non_text_blocks(self):
        payload = {"content": [
            {"type": "thinking", "thinking": ""},
            {"type": "text", "text": '{"score": 42, "rationale": "Hm."}'},
        ]}
        fake = RecordingUrlopen(payload)
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertEqual((result.score, result.error), (42, None))

    def test_http_error_surfaces_status_and_body(self):
        err = urllib.error.HTTPError(
            "https://api.anthropic.com/v1/messages", 429, "Too Many Requests", {},
            io.BytesIO(b'{"type":"error","error":{"type":"rate_limit_error"}}'),
        )
        fake = RecordingUrlopen(err)
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertEqual(result.score, 0)
        self.assertIn("anthropic API 429", result.error)
        self.assertIn("rate_limit_error", result.error)

    def test_unreachable(self):
        fake = RecordingUrlopen(urllib.error.URLError("dns failure"))
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertIn("anthropic API unreachable", result.error)

    def test_no_text_block(self):
        fake = RecordingUrlopen({"content": []})
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds")
        self.assertIn("unexpected anthropic response", result.error)


class PitchThresholdTests(unittest.TestCase):
    """The second (pitch) call fires only at or above the threshold."""

    def setUp(self):
        patcher = patch.dict(os.environ, LOCAL_ENV)
        patcher.start()
        self.addCleanup(patcher.stop)

    def run_score(self, *responses, **kwargs):
        fake = RecordingUrlopen(*responses)
        with patch.object(scorer.urllib.request, "urlopen", fake):
            result = scorer.score_job(make_job(), "creds", **kwargs)
        return result, fake

    def test_default_threshold_is_80(self):
        self.assertEqual(scorer.DEFAULT_PITCH_THRESHOLD, 80)

    def test_below_threshold_makes_one_call(self):
        result, fake = self.run_score(local_payload('{"score": 79, "rationale": "Close."}'))
        self.assertEqual(len(fake.requests), 1)
        self.assertEqual((result.score, result.pitch), (79, ""))

    def test_at_threshold_drafts_pitch(self):
        result, fake = self.run_score(
            local_payload('{"score": 80, "rationale": "Strong."}'),
            local_payload('{"pitch": "I shipped X at Y."}'),
        )
        self.assertEqual(len(fake.requests), 2)
        self.assertEqual((result.score, result.rationale, result.pitch, result.error),
                         (80, "Strong.", "I shipped X at Y.", None))
        # The second call uses the pitch prompt, not the scoring prompt.
        self.assertNotEqual(fake.body(0)["messages"][0]["content"], fake.body(1)["messages"][0]["content"])

    def test_custom_threshold(self):
        _, fake = self.run_score(local_payload('{"score": 85, "rationale": "x"}'), pitch_threshold=90)
        self.assertEqual(len(fake.requests), 1)

    def test_pitch_failure_keeps_score(self):
        with self.assertLogs("scorer", level="WARNING"):
            result, fake = self.run_score(
                local_payload('{"score": 95, "rationale": "Ideal."}'),
                urllib.error.URLError("server went away"),
            )
        self.assertEqual(len(fake.requests), 2)
        self.assertEqual((result.score, result.rationale, result.pitch, result.error), (95, "Ideal.", "", None))

    def test_scoring_error_skips_pitch(self):
        result, fake = self.run_score(local_payload("not json at all"))
        self.assertEqual(len(fake.requests), 1)
        self.assertIsNotNone(result.error)


class BuildPromptTests(unittest.TestCase):
    def test_long_description_truncated_at_paragraph(self):
        para = "x" * 1000
        description = "\n\n".join([para] * 10)  # ~10k chars
        prompt = scorer._build_prompt(make_job(description=description), "creds", "{description}")
        self.assertLessEqual(len(prompt), scorer.MAX_DESCRIPTION_CHARS + 50)
        self.assertTrue(prompt.endswith("[... description truncated ...]"))

    def test_missing_department_shows_na(self):
        prompt = scorer._build_prompt(make_job(department=None), "creds", "Dept: {department}")
        self.assertEqual(prompt, "Dept: n/a")

    def test_literal_braces_in_template_survive(self):
        prompt = scorer._build_prompt(make_job(), "creds", '{title} -> {{"score": 1}}')
        self.assertEqual(prompt, 'Staff Engineer -> {{"score": 1}}')


if __name__ == "__main__":
    unittest.main()
