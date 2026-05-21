# Jane Doe — Senior Backend / ML-Adjacent Operator

> **How to use this file**
>
> The scorer reads this entire markdown file as the candidate profile every
> time it scores a role. Keep it under ~1500 words so it fits comfortably in
> a model's context window without crowding out the job description.
>
> Write it the way you'd describe yourself to a sharp recruiter who has
> never met you. Be specific about *what you've shipped* and *what you're
> looking for next*. Vague aspirations score poorly because the LLM has
> nothing concrete to anchor to.

## Snapshot

- **Role I want next:** Senior backend engineer or ML-platform engineer at a
  product-led startup (Series A–C). Open to staff-level if the scope is
  builder-heavy. **Not interested** in pure people-manager roles right now.
- **Location:** New York City or San Francisco preferred; remote-US fine if
  the team is async-first. Willing to relocate for the right role.
- **Compensation:** Targeting $200–260k base + meaningful equity. Will trade
  base down for a team I'd brag about working with.
- **Visa:** US citizen, no sponsorship needed.

## What I've shipped

I'm a senior backend engineer with 7 years across early-stage startups. I
write production Python and Go, and I'm at home anywhere on the stack from
the database up through the load balancer.

**Highlights from the last 3 years:**

- **Acme Corp (2023–present), Staff Engineer, Platform team.** Owned the
  rebuild of our event-ingestion pipeline from a clogged Kafka-plus-cron
  setup to a Temporal-orchestrated streaming system. P99 latency dropped
  from 14s to 380ms; we now process ~2.4 billion events/month on the same
  hardware budget. Wrote the migration runbook the rest of eng followed.
- **Built the internal LLM-evaluation harness** that every product team now
  uses to gate model upgrades. Started as a 200-line script during a
  hackweek; nine months in it runs nightly across 14 product surfaces and
  has caught three regressions that would have shipped otherwise.
- **Mentored 4 mid-level engineers** through promotion; two are now seniors
  running their own subsystems.

**Before Acme:**

- **Beta Logistics (2020–2023), Senior Engineer.** Migrated a 12-year-old
  Rails monolith's billing module to a Go service without losing a cent of
  revenue during cutover. Wrote the dual-write reconciliation framework
  that made the migration provable instead of vibes-based.
- **Gamma Health (2019–2020), Engineer.** Built the patient-intake API
  and the HIPAA-compliant audit log subsystem from scratch. Shipped to
  production in 9 weeks.
- **Self-employed (2018–2019).** Contract backend work for three YC
  companies. Two are still customers of my Github gists; one is a
  Series C now.

## What I'm good at

- **Migrations and decompositions.** I like big legacy systems and the
  social process of getting a team through a rewrite without losing
  morale. I've done it three times now and the playbook is portable.
- **Latency hunting.** I'm the person on the team who actually runs the
  profiler. Most of my "magic" moments have been finding the N+1 query in
  someone else's code at 11pm before a launch.
- **Writing the docs.** I default to writing a one-pager before I write
  the code. The doc gets reviewed, the code gets shipped. This is the
  single highest-leverage habit I've built.
- **ML-platform-adjacent work.** I'm not an ML researcher, but I've spent
  the last two years building the rails ML researchers use — eval harnesses,
  feature stores, batch inference pipelines, model registries. I read
  papers; I don't write them.

## What I'm looking for next

Concretely, the role is most exciting if it ticks at least three of these:

- Real ownership of a system that customers depend on, not a Jira-ticket
  factory inside a bigger team.
- A leadership team that ships taste, not just velocity — I want to work
  somewhere whose product makes me want to use it.
- A bias toward small teams (<25 eng total) where I can know everyone's
  work.
- Genuine technical investment in evals, observability, and platform
  quality — the rails, not the rocket.
- An interesting public artifact: a docs site I'd link a friend to, an
  engineering blog with real teeth, an OSS contribution culture.

I am **not** looking for:

- IPO-track public-company roles or enterprise sales-engineering work.
- Pure people-manager seats with no IC scope. Tech lead, founding eng,
  staff engineer with a small team — yes. Director of 12 — not today.
- Crypto-native or token-launch companies (no judgment, just not my fit).

## Tools I reach for

- **Languages:** Python (primary), Go (second). TypeScript when forced
  but competent. Rust for the right component.
- **Storage:** Postgres for almost everything; Redis for the obvious;
  ClickHouse for analytics. I've operated each in prod.
- **Orchestration:** Temporal, Airflow, plain cron. Strong opinions
  about retries and idempotency.
- **LLM tooling:** Comfortable with the major SDKs. I've built two
  evaluation harnesses from scratch and one model-routing layer.
- **Infra:** AWS (mostly), Terraform, Kubernetes when the team needs it.
  I'm not an SRE but I won't be lost in your runbook.

## A few things that signal fit

- I'd rather take a 6-month detour to fix the foundation than ship a
  feature on broken footing.
- I write design docs that engineers actually want to read. Happy to
  share samples if useful.
- I keep an active home lab — I run my own LLM inference server on a
  Mac mini, so I've felt the latency and quantization tradeoffs myself,
  not just read about them.
- I get along well with founders. I've reported directly into the CEO
  at two of three roles and the working rhythm worked both ways.

## Links

- Portfolio: https://janedoe.example.com
- GitHub: https://github.com/janedoe-example
- LinkedIn: https://linkedin.com/in/janedoe-example
- Email: jane@example.com
