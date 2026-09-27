<p align="center">
  <img src="branding/logo.svg" width="140" alt="job-search-agent logo">
</p>

<h1 align="center">job-search-agent</h1>

<p align="center">
  <strong>A daily job search that reads your real story first, then scores every open role at the companies you pick against it.<br>
  Runs on your own machine. Pure Python standard library. Nothing gets submitted for you.</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="MIT"></a>
  <a href="#quick-start"><img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+"></a>
  <a href="#privacy"><img src="https://img.shields.io/badge/Dependencies-zero-success?style=for-the-badge" alt="Zero dependencies"></a>
  <a href="#supported-job-boards"><img src="https://img.shields.io/badge/ATS-Ashby_·_Greenhouse_·_Lever-ff69b4?style=for-the-badge" alt="ATS connectors"></a>
</p>

<p align="center">
  <a href="https://youtu.be/qlgvh2N8HJ4">
    <img src="https://img.youtube.com/vi/qlgvh2N8HJ4/maxresdefault.jpg" width="720" alt="job-search-agent 60-second walkthrough on YouTube">
  </a><br>
  <em>60-second walkthrough (the screens in the video are mockups of the flow).</em>
</p>

---

## What it does

Every morning it:

1. **Fetches every open role** from the companies in your list, straight from their public Ashby, Greenhouse or Lever job boards. No login, no scraping, no browser.
2. **Drops the obvious no's** with your own rules (titles, locations, keywords in the description) before any AI time gets spent.
3. **Skips anything it already scored** on a previous day, so you only see new postings.
4. **Scores what's left from 0 to 100** against `credentials.md`, a plain markdown file with your real background, and writes one short reason per score.
5. **Drafts a ~200-word pitch** for every role that scores 80 or higher, ready to adapt for a cover letter or a recruiter message.

You read the results. You decide what to apply to. It never applies for you.

A real dry run on 2026-09-27 against the 14 companies in `examples/companies.example.json` pulled **3,349 open roles**. The example filters cut that to 2,404 before scoring. Your own company list and filters decide how big that number is.

---

## Quick start

Needs Python 3.11 or newer. Nothing else to install.

```bash
git clone https://github.com/nicedreamzapp/job-search-agent.git
cd job-search-agent

# Plain-English setup wizard, writes credentials.md for you (~5-10 min)
python3 jobscout.py setup          # in the terminal
python3 jobscout.py setup --web    # or in your browser

# Or set it up by hand
mkdir -p ~/.config/jobscout
cp examples/credentials.example.md ~/.config/jobscout/credentials.md
cp examples/companies.example.json ~/.config/jobscout/companies.json
cp examples/filters.example.yml    ~/.config/jobscout/filters.yml

# Try the job boards first, no AI needed
python3 jobscout.py --dry-run

# Full run with scoring (needs a model, see below)
python3 jobscout.py
```

If you'd rather not touch a terminal for setup at all, double-click `wizard/index.html`. It works offline and gives you a "Download credentials.md" button at the end. Full guide: [`docs/SETUP_WIZARD.md`](docs/SETUP_WIZARD.md).

### Command-line options

| Flag | What it does |
|---|---|
| `--dry-run` / `--no-llm` | Fetch and filter only, skip scoring. Good for testing your company list. |
| `--companies-only=slug1,slug2` | Run just those companies. |
| `--config-dir DIR` | Use a different config folder. |
| `-v`, `--verbose` | Show why each dropped role was dropped. |

---

## Choosing the AI that does the scoring

**Default: a model on your own machine.** The scorer talks to any server that speaks the OpenAI-style `/v1/chat/completions` API, such as `mlx_lm.server`, Ollama, llama.cpp's server, or vLLM.

| Setting | Default |
|---|---|
| `JOBSCOUT_LLM_ENDPOINT` | `http://localhost:8000` |
| `JOBSCOUT_LLM_MODEL` | `mlx-community/Llama-3.1-8B-Instruct-4bit` |

**Optional: the Anthropic API.** If `ANTHROPIC_API_KEY` is set, the scorer uses Claude instead (pick the model with `JOBSCOUT_ANTHROPIC_MODEL`). This only happens when you set that variable yourself.

---

## Where the results go

| File | What's in it |
|---|---|
| `~/.local/state/jobscout/results/<date>.json` | Every scored role for the day, best first: company, title, location, link, score, reason, and the pitch if one was drafted |
| `~/.local/state/jobscout/seen.json` | Roles already scored, so tomorrow only shows new ones |

Set `JOBSCOUT_STATE_DIR` to put these somewhere else. If you want the top 10 sent to your own dashboard, set `JOBSCOUT_HQ_URL` (plus `JOBSCOUT_HQ_TOKEN` if it needs a bearer token) and the agent will POST them there after each run.

---

## How it works

```
companies.json ──▶ connectors (Ashby · Greenhouse · Lever)
                        │  normalized Job objects
                        ▼
filters.yml ─────▶ hard filters (title · description · company · location)
                        │
seen.json ───────▶ skip roles already scored
                        │
credentials.md ──▶ scorer: 0-100 + reason ──▶ pitch for scores ≥ 80
                        │
                        ▼
                results/<date>.json  (+ optional webhook)
```

| File | Job |
|---|---|
| `jobscout.py` | Runs the whole pipeline and handles the CLI |
| `connectors/` | One small file per job board, all returning the same `Job` shape |
| `filters.py` | Regex rules loaded from `filters.yml` or `filters.json` |
| `scorer.py` | Scoring and pitch calls, over plain HTTP to either backend |
| `output.py` | Results file, seen list, optional webhook |
| `prompts/` | The scoring and pitch prompts, editable without touching Python |
| `setup.py`, `wizard/` | The terminal and browser setup wizards |

More detail in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## Privacy

`credentials.md` is the most personal file in your job search, so it stays on your machine.

- With a local model, the only network calls are to the public job-board APIs, and those requests never include anything about you.
- The Anthropic fallback and the webhook are both off until you set their environment variables.
- There's no telemetry and no account.

---

## Tuning it

- **Scoring:** edit [`prompts/scoring.md`](prompts/scoring.md) to change what counts as a good fit. Reference: [`docs/CUSTOMIZE_SCORING.md`](docs/CUSTOMIZE_SCORING.md).
- **Pitches:** edit [`prompts/pitch.md`](prompts/pitch.md) to change the voice and length.
- **Filters:** every key in [`examples/filters.example.yml`](examples/filters.example.yml) is a list of case-insensitive regexes. `require_locations_in` is the one allow-list; the rest drop matches.

---

## Supported job boards

| ATS | Module | Public endpoint |
|---|---|---|
| Ashby | `connectors/ashby.py` | `api.ashbyhq.com/posting-api/job-board/{slug}` |
| Greenhouse | `connectors/greenhouse.py` | `boards-api.greenhouse.io/v1/boards/{slug}/jobs` |
| Lever | `connectors/lever.py` | `api.lever.co/v0/postings/{slug}` |

In `companies.json`, each entry needs a `slug` (the company's name in its job-board URL) and an `ats`. `name` is optional. To add another board, write one file in `connectors/` and register it in the `CONNECTORS` table in `jobscout.py`. See [`docs/ADD_A_CONNECTOR.md`](docs/ADD_A_CONNECTOR.md).

---

## Run it every morning

- **macOS:** launchd plist in [`docs/LAUNCHAGENT_MACOS.md`](docs/LAUNCHAGENT_MACOS.md)
- **Linux:** systemd timer in [`docs/SYSTEMD_LINUX.md`](docs/SYSTEMD_LINUX.md)
- **Windows:** point Task Scheduler at `python jobscout.py`

---

## Tests

```bash
python3 -m unittest discover -s tests
```

60 tests covering the three connectors, the filters and the scorer (both AI backends mocked). Three of them hit the live job boards and only run with `JOBSCOUT_LIVE_TESTS=1`.

---

## Roadmap

- [ ] A readable morning briefing (markdown or email) alongside the JSON
- [ ] Workday, SmartRecruiters, Recruitee and Personio connectors
- [ ] Mark roles "not interested" and feed that back into scoring
- [ ] Multiple profiles, so one role can be scored against different versions of you
- [ ] Top roles on a calendar feed by apply deadline

---

## Contributing

New connectors, better prompts and `credentials.md` examples for non-engineering roles are the most useful contributions. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

Built on public job-board APIs and Apple's MLX. Full list in [`CREDITS.md`](CREDITS.md).

## License

MIT
