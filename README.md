<p align="center">
  <img src="docs/assets/logo.png" width="160" alt="job-search-agent logo placeholder">
</p>

<p align="center">
  <h1 align="center">🎯⚡ job-search-agent</h1>
  <p align="center">
    <strong>Wake up to a hand-curated, AI-scored list of job openings — ranked against <em>you</em>, not against a keyword bag.<br>Local-first. No spray-apply. No SaaS fees.</strong>
  </p>
  <p align="center">
    <a href="../../stargazers"><img src="https://img.shields.io/github/stars/USER/job-search-agent?style=for-the-badge&logo=github&color=f5c542&labelColor=1f2328" alt="GitHub stars"></a>
    <a href="../../network/members"><img src="https://img.shields.io/github/forks/USER/job-search-agent?style=for-the-badge&logo=github&color=4c9a2a&labelColor=1f2328" alt="GitHub forks"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/📜_License-MIT-yellow?style=for-the-badge" alt="MIT"></a>
    <a href="#-quick-start-3-minutes"><img src="https://img.shields.io/badge/🐍_Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11+"></a>
    <a href="#-privacy--local-first"><img src="https://img.shields.io/badge/🔒_Privacy-100%25_Local--First-success?style=for-the-badge" alt="100% Local-First"></a>
    <a href="#-how-it-works-architecture-diagram"><img src="https://img.shields.io/badge/🧠_LLM-MLX_·_Ollama_·_Claude_API-purple?style=for-the-badge" alt="LLM backends"></a>
    <a href="#-what-makes-this-different"><img src="https://img.shields.io/badge/🚫_Spray--Apply-Zero-red?style=for-the-badge" alt="No spray-apply"></a>
    <a href="#-adding-a-new-ats"><img src="https://img.shields.io/badge/🧩_ATS-Ashby_·_Greenhouse_·_Lever-ff69b4?style=for-the-badge" alt="ATS connectors"></a>
    <a href="#-schedule-daily-runs"><img src="https://img.shields.io/badge/📅_Daily-launchd_·_cron_·_systemd-orange?style=for-the-badge" alt="Schedule"></a>
    <a href="#-the-big-claim"><img src="https://img.shields.io/badge/🪴_Ambient-Computing-9cf?style=for-the-badge" alt="Ambient Computing"></a>
  </p>
  <p align="center">
    <a href="#-tldr">✨ TL;DR</a> ·
    <a href="#-the-big-claim">💥 Claim</a> ·
    <a href="#-30-second-demo">🎬 Demo</a> ·
    <a href="#-quick-start-3-minutes">🚀 Quick Start</a> ·
    <a href="#-how-it-works-architecture-diagram">🧠 Architecture</a> ·
    <a href="#-what-makes-this-different">🎯 Why</a> ·
    <a href="#-privacy--local-first">🔒 Privacy</a> ·
    <a href="#-customizing-the-scoring-rubric">🛠️ Customize</a> ·
    <a href="#-adding-a-new-ats">🧩 Connectors</a> ·
    <a href="#-schedule-daily-runs">📅 Schedule</a> ·
    <a href="#-roadmap">🛣️ Roadmap</a> ·
    <a href="#-contributing">🤝 Contribute</a>
  </p>
</p>

---

<p align="center">
  <h2 align="center">🎬 WATCH THE 60-SECOND DEMO</h2>
  <p align="center">
    <strong>A real morning briefing. 47 roles scored across 12 companies. 3 custom pitches drafted. 90 seconds, end to end, on a laptop.<br>
    No cloud LLM. No SaaS. No "AI resume optimizer" hype.</strong>
  </p>
  <p align="center">
    <a href="https://youtu.be/REPLACE_WITH_VIDEO_ID">
      <img src="docs/assets/demo-thumbnail.png" width="720" alt="job-search-agent — 60-second walkthrough">
    </a>
  </p>
  <p align="center">
    <a href="https://youtu.be/REPLACE_WITH_VIDEO_ID">
      <img src="https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
    </a>
    &nbsp;
    <a href="https://www.youtube.com/@REPLACE_WITH_CHANNEL">
      <img src="https://img.shields.io/badge/Subscribe-for_more_demos-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Subscribe">
    </a>
  </p>
  <p align="center">
    <em>Built for anyone who's tired of LinkedIn's "200 applicants in 12 hours" job-board roulette.</em>
  </p>
</p>

---

## ✨ TL;DR

**Wake up to a daily list of AI-scored job matches across 50+ companies.** Local-first. Your data stays on your machine. The agent reads **your** portfolio — GitHub stars, shipped products, published research, community size, the work you'd actually point a hiring manager at — and scores every open role against you, not against a generic resume-keyword match. The top 3 roles each morning come with a 200-word, role-specific pitch already drafted. You stay in the loop on every send.

---

## 💥 The Big Claim

Most job seekers do one of two things: **spray-apply** through a Workday queue and never hear back, or **hand-curate** roles from LinkedIn one tab at a time and burn an hour a day on it. Both lose.

This repo flips it. **You write your credentials once** — your real story, your real ships, your real numbers — into a single markdown file. Every morning, the agent fetches fresh openings from every ATS in your allow-list (Ashby, Greenhouse, Lever, more on the way), filters them through your hard constraints (location, comp band, role family), and **scores each surviving role against your actual portfolio using a local LLM**. The top hits get a 200-word custom pitch drafted on the spot — the kind of paragraph you'd normally take 20 minutes to write, ready to paste into a cover letter or a recruiter DM.

**No auto-submit.** You stay in the loop. No data leaves your machine if you pick the MLX or Ollama backend — the Anthropic API is an explicit, opt-in fallback for users who don't have a beefy local box. Built for the ambient-computing era of job hunting: the agent does the boring grind at 6 AM so you spend your morning coffee reading three roles that actually fit, not 200 that don't.

---

## 🎬 30-Second Demo

<p align="center">
  <img src="docs/assets/demo-loop.gif" width="720" alt="30-second loop of the agent scoring roles">
</p>

<p align="center">
  <em>Watch the agent score 47 roles across Anthropic / Modal / Replit / Cohere / Together in 90 seconds, then write a custom pitch for the top 3.</em>
</p>

---

## 🚀 Quick Start (3 minutes)

```bash
# 1. Clone the repo
git clone https://github.com/USER/job-search-agent.git
cd job-search-agent

# 2. No deps to install — pure stdlib. Python 3.11+ is the only requirement.

# 3. Copy the example configs into your XDG config dir
mkdir -p ~/.config/jobscout
cp examples/credentials.example.md  ~/.config/jobscout/credentials.md
cp examples/companies.example.json  ~/.config/jobscout/companies.json

# 4. Edit them with your real story + your real allow-list
$EDITOR ~/.config/jobscout/credentials.md
$EDITOR ~/.config/jobscout/companies.json

# 5. Run it
python3 jobscout.py
```

What you get back:

```
╭─────────────────────────────────────────────────────────────╮
│  job-search-agent — daily briefing · 2026-05-21 06:14       │
│  ─────────────────────────────────────────────────────────  │
│  Scanned : 12 companies · 312 roles                         │
│  Filtered: 47 roles passed your hard constraints            │
│  Scored  : top 3 below · full list in state/briefing.md     │
╰─────────────────────────────────────────────────────────────╯

🟢 92/100 — Anthropic · Member of Technical Staff, Agents
   why: ships agent frameworks, you've shipped 4 OSS agent repos,
        128k+ combined stars, exactly the cohort they describe.
   pitch drafted → state/pitches/anthropic-mts-agents.md

🟢 88/100 — Modal Labs · Founding DevRel
   why: your blog ships weekly, your community is 3k+ Discord,
        Modal explicitly wants someone who can write & ship demos.
   pitch drafted → state/pitches/modal-devrel.md

🟡 79/100 — Replit · Applied AI Engineer
   ...
```

Open `state/briefing.md` for the full ranked list, or `state/pitches/` to read the auto-drafted role-specific paragraphs.

---

## 🧠 How It Works (architecture diagram)

```
   ┌─────────────────────────────────────────────────────────────────┐
   │                       YOUR MACHINE                              │
   │                                                                 │
   │  📋 companies.json     ┌─────────────────────────────────────┐  │
   │      (allow-list)      │                                     │  │
   │           │            │   🧠 jobscout.py orchestrator       │  │
   │           ▼            │                                     │  │
   │  ┌──────────────────┐  │   ┌─────────────────────────────┐   │  │
   │  │  🔌 connectors   │──┼──▶│  raw_roles[]                │   │  │
   │  │                  │  │   └──────────────┬──────────────┘   │  │
   │  │  · Ashby         │  │                  ▼                  │  │
   │  │  · Greenhouse    │  │   ┌─────────────────────────────┐   │  │
   │  │  · Lever         │  │   │  🪓 hard-constraint filter  │   │  │
   │  │  · (your own)    │  │   │  (location · comp · family) │   │  │
   │  └──────────────────┘  │   └──────────────┬──────────────┘   │  │
   │                        │                  ▼                  │  │
   │  📝 credentials.md ───▶│   ┌─────────────────────────────┐   │  │
   │      (your story)      │   │  🎯 LLM scorer + pitcher    │   │  │
   │                        │   │  (MLX · Ollama · Anthropic) │   │  │
   │                        │   └──────────────┬──────────────┘   │  │
   │                        │                  ▼                  │  │
   │                        │   📬 state/briefing.md              │  │
   │                        │   📝 state/pitches/*.md             │  │
   │                        └─────────────────────────────────────┘  │
   │                                                                 │
   │              🚫 ZERO outbound calls with local backend          │
   └─────────────────────────────────────────────────────────────────┘
```

**1 — Connectors** hit each company's public ATS endpoint (Ashby, Greenhouse, Lever) and return a normalized `Role` object. No login. No scraping headless Chrome. Public job-board APIs only.

**2 — The hard-constraint filter** drops anything that fails your non-negotiables (wrong country, below comp floor, wrong role family) before any LLM tokens get spent.

**3 — The scorer** prompts the LLM with your full `credentials.md` and the surviving role, asks for a 0–100 fit score with a one-sentence justification, and — for any role above your `pitch_threshold` (default 80) — drafts a 200-word custom pitch.

---

## 🎯 What Makes This Different

|                                              | This agent | LinkedIn Jobs | Wellfound | Spray-applying |
|----------------------------------------------|:----------:|:-------------:|:---------:|:--------------:|
| Reads YOUR full credentials                  |     ✅     |       ❌      |     ❌    |        ❌       |
| Scores roles against your actual portfolio   |     ✅     |       ❌      |     ❌    |        ❌       |
| Drafts custom pitches per role               |     ✅     |       ❌      |     ❌    |        ❌       |
| Runs locally / private                       |     ✅     |       ❌      |     ❌    |       N/A       |
| Costs $0/mo (local LLM)                      |     ✅     |       ❌      |     ❌    |       N/A       |
| Doesn't spam recruiters                      |     ✅     |       ✅      |     ✅    |        ❌       |
| Surfaces roles you'd never have searched for |     ✅     |       ❌      |     ❌    |        ❌       |
| You stay in the loop on every send           |     ✅     |       ✅      |     ✅    |       N/A       |

The core unlock: **the LLM has read your real story before it ever sees a role.** That's a different question than "does this resume contain the word `kubernetes`."

---

## 🔒 Privacy / Local-First

Your `credentials.md` is the most sensitive file in your job search. It has your real numbers, your real ships, the unvarnished version of your story. It should never leak.

- **Default backend: local.** Point `JOBSCOUT_LLM_ENDPOINT` at any OpenAI-compatible chat-completions server — an [MLX server](https://github.com/ml-explore/mlx-examples), a local [Ollama](https://ollama.com) instance, `llama.cpp` server mode, vLLM, anything that speaks `/v1/chat/completions`. The default is `http://localhost:8000`. Nothing about your credentials or the roles you're scoring ever touches the public internet.
- **Optional cloud fallback.** If you don't have a beefy enough local box, set `ANTHROPIC_API_KEY` in your environment. The scorer detects the key and switches to the Anthropic Messages API automatically. This is explicitly opt-in — the env var has to be present. There is no "anonymous telemetry," no "share your usage to improve the model" toggle. Off means off.
- **The connectors are read-only.** They hit public ATS endpoints. They never log in as you, never submit anything on your behalf, never even know your name.

```
   ┌─────────────────────────────────────────────────────────┐
   │                    YOUR MACHINE                         │
   │                                                         │
   │   credentials.md  ──▶  scorer  ──▶  LLM (local)         │
   │                                       │                 │
   │                                       └─▶ briefing.md   │
   │                                                         │
   │   🚫 nothing crosses this boundary with local backend   │
   └─────────────────────────────────────────────────────────┘
                              ↕
                  (only the connectors talk out,
                   and only to public ATS endpoints)
```

---

## 🛠️ Customizing the Scoring Rubric

The default scoring prompt asks the LLM to weigh shipped artifacts, demonstrated impact, role-family fit, and timing signals. You can replace it wholesale.

- Edit [`prompts/scoring.md`](prompts/scoring.md) to change how the LLM weighs your portfolio against a role.
- Edit [`prompts/pitch.md`](prompts/pitch.md) to change the voice and length of the auto-drafted pitch.
- Full rubric reference + examples → [`docs/CUSTOMIZE_SCORING.md`](docs/CUSTOMIZE_SCORING.md)

---

## 🧩 Adding a New ATS

Connectors live in `connectors/`. Each one is a single Python file that exposes a `fetch(company_slug) -> list[Role]` function. Adding a new one is usually **under 80 lines of code**.

Already supported:

| ATS | Module | Auth | Public endpoint |
|---|---|---|---|
| 🟢 **Ashby** | `connectors/ashby.py` | None | `api.ashbyhq.com/posting-api/job-board/{slug}` |
| 🟢 **Greenhouse** | `connectors/greenhouse.py` | None | `boards-api.greenhouse.io/v1/boards/{slug}/jobs` |
| 🟢 **Lever** | `connectors/lever.py` | None | `api.lever.co/v0/postings/{slug}` |

Adding Workday, SmartRecruiters, or your own — see [`docs/ADD_A_CONNECTOR.md`](docs/ADD_A_CONNECTOR.md).

---

## 📅 Schedule Daily Runs

The whole point is that you wake up to the briefing, not that you remember to type `python3 jobscout.py`. Pick your platform:

- **macOS** → launchd plist in [`docs/LAUNCHAGENT_MACOS.md`](docs/LAUNCHAGENT_MACOS.md)
- **Linux** → systemd timer in [`docs/SYSTEMD_LINUX.md`](docs/SYSTEMD_LINUX.md)
- **Windows / any** → plain cron / Task Scheduler

macOS one-liner:

```xml
<key>ProgramArguments</key>
<array>
  <string>/usr/bin/env</string>
  <string>python3</string>
  <string>/path/to/job-search-agent/jobscout.py</string>
</array>
<key>StartCalendarInterval</key>
<dict><key>Hour</key><integer>6</integer><key>Minute</key><integer>0</integer></dict>
```

Drop it in `~/Library/LaunchAgents/`, `launchctl load`, done. Briefing waits for you with your first coffee.

---

## 🛣️ Roadmap

- [ ] **LinkedIn Jobs connector** — once the public API stabilizes (currently rate-limited into uselessness for OSS tools)
- [ ] **Workday connector** — the white whale; non-trivial because every Workday instance is its own snowflake
- [ ] **SmartRecruiters + Recruitee + Personio** connectors
- [ ] **More local LLM endpoints** — Ollama is wired, MLX is wired; want vLLM, Together, OpenRouter, llama.cpp as drop-ins
- [ ] **Email-driven results delivery** — agent emails you the briefing instead of dropping it to `state/`
- [ ] **Browser-extension submit-on-your-behalf** — explicit per-role consent toggle, never silent
- [ ] **`.ics` calendar feed** — top roles drop on your calendar at apply-deadline
- [ ] **Multi-credential profiles** — score the same role against "founder-track me" and "IC-track me"
- [ ] **Negative-example training** — let the LLM learn from roles you marked `not_interested` last week

---

## 🤝 Contributing

Issues and PRs welcome. Especially:

1. **New ATS connectors** — bring your favorite company's job board into the allow-list.
2. **Better scoring prompts** — if you've tuned `prompts/scoring.md` to surface better signal, send a PR.
3. **More local-LLM backends** — keep us off the cloud.
4. **Real-world `credentials.md` templates** — the example in `examples/` is a generic engineer; we'd love variants for designers, GTM, applied research, comms, ops.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full guide.

---

## 📜 License

MIT. Use it, fork it, ship it. Credit appreciated but not required.

---

<p align="center">
  <a href="../../stargazers"><img src="https://img.shields.io/github/stars/USER/job-search-agent?style=for-the-badge&logo=github&color=f5c542&labelColor=1f2328" alt="GitHub stars"></a>
  <a href="../../network/members"><img src="https://img.shields.io/github/forks/USER/job-search-agent?style=for-the-badge&logo=github&color=4c9a2a&labelColor=1f2328" alt="GitHub forks"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/📜_License-MIT-yellow?style=for-the-badge" alt="MIT"></a>
  <a href="#-privacy--local-first"><img src="https://img.shields.io/badge/🔒_Privacy-100%25_Local--First-success?style=for-the-badge" alt="100% Local-First"></a>
</p>

<p align="center">
  <a href="https://star-history.com/#USER/job-search-agent&Date">
    <img src="https://api.star-history.com/svg?repos=USER/job-search-agent&type=Date" width="540" alt="Star history">
  </a>
</p>

<p align="center">
  <strong>If this saved you 10 hours of job hunting, please ⭐ the repo.</strong>
</p>
