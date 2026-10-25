# Security policy

## Reporting a vulnerability

Please do not open a public issue for security problems.

Report them privately through GitHub: go to the **Security** tab of this repo and click **Report a vulnerability** ([direct link](https://github.com/nicedreamzapp/job-search-agent/security/advisories/new)). Only the maintainer sees the report.

Helpful details: what you found, how to reproduce it, which version or commit, your OS and Python version, and which scoring backend you were using (a local model or the Anthropic API). Leave your real `credentials.md` out of the report.

I aim to reply within 3 days and to ship a fix or a clear plan within 30 days, depending on severity. You will be credited in the advisory unless you ask not to be.

## Supported versions

Fixes go into the latest version on `main`. Please update before reporting if you are on an older commit.

## What matters most here

The parts where a mistake could hurt someone:

- `credentials.md`, the user's personal background, which should only ever leave the machine for the scoring backend they chose in `scorer.py`
- API keys and tokens read from the environment: `ANTHROPIC_API_KEY` in `scorer.py`, and `JOBSCOUT_HQ_URL` and `JOBSCOUT_HQ_TOKEN` for the optional webhook in `output.py`
- the browser setup wizard in `setup.py` (`python3 jobscout.py setup --web`), which runs a local server on `127.0.0.1:8765` and writes `credentials.md` from what it receives
- the connectors in `connectors/`, which parse JSON from public job boards that could change or return unexpected data
