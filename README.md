# Open Source Compliance Kit

Reusable GitHub Actions workflow and VS Code Copilot skill for World Bank open source compliance.

## Checks

- **License** — Whitelist: MIT, Apache-2.0. Requires WB IGO Rider for each.
- **README** — Presence and content checks
- **Secrets** — Queries GitHub Secret Scanning API (public repos); TruffleHog fallback (private repos)
- **Data Files** — Warns on large data files; suggests data catalog
- **Dependencies** — Queries Dependabot Alerts API
- **Code Quality (Basic)** — Local linters (eslint/ruff/flake8) or Super-Linter fallback
- **Code Quality (CodeQL)** — Queries GitHub Code Scanning API (public repos); skipped for private repos
- **Tech Stack** — GitHub Languages API + framework detection (informational)
- **AI Usage** — Detects AI library usage (informational)

For Secret Scanning, Dependabot, and CodeQL, the workflow **queries native GitHub APIs** rather than duplicating these scans. This avoids redundancy while consolidating all results into a single compliance issue.

On the default branch, a **compliance issue** is automatically created/updated with a checklist of results. The issue closes when all required checks pass (code quality checks are optional).

## Org Prerequisites

1. Enable **Dependabot alerts** org-wide: Settings > Code security > Dependabot alerts

2. *(Optional)* In **GitHub Org Secrets**, add:
   - `DEPENDABOT_TOKEN` — PAT with `security_events` scope for Dependabot API access on private repos

## How It Works — Two-Stage Review

Open source publication follows a two-stage process:

1. **Stage 1 — Automated CI**: The team adds the compliance workflow to their repo. It runs on every push, PR, and daily schedule. A compliance issue is auto-created with pass/fail results. The team iterates until checks pass.
2. **Stage 2 — OSPO Review**: The OSPO lead clones the repo, copies the Copilot skill in, and invokes it as a failsafe review. The skill cross-references automated results with the intranet request form, audits the repo independently, and generates fixes + PR content.

After both stages pass, the OSPO lead **manually changes the repo visibility to public**. GitHub native features (Secret Scanning, CodeQL default setup) activate automatically on public repos.

The compliance workflow continues running after publication as an ongoing check.

## How Teams Adopt

### Step 1: Add the compliance workflow

Copy [`.github/compliance/sample-per-repo-caller.yml`](.github/compliance/sample-per-repo-caller.yml) to the target repo as `.github/workflows/compliance.yml`. Push to the default branch. The workflow runs automatically and creates a compliance issue with a checklist of results.

The team reviews the compliance issue and fixes failures. The workflow re-runs on each push and updates the issue automatically.

### Step 2: OSPO review (when ready for publication)

When the team believes their repo is ready, the OSPO lead:

1. Clones the target repo and copies the [`.github/skills/wbg-oss-review/`](.github/skills/wbg-oss-review/) directory into it
2. Opens the repo in VS Code and invokes the **wbg-oss-review** Copilot skill
3. Provides: (a) the compliance issue content and (b) the intranet request form data
4. The skill audits the repo, creates/updates compliance files, and generates PR content
5. Creates a branch, commits the changes, and opens a PR using the generated content
6. The team merges the PR — the compliance workflow re-runs automatically
7. When all required checks pass, the compliance issue closes (code quality is optional)

### Step 3: Pre-publication check (optional)

Run the [pre-publication compliance check](.github/compliance/make-public.yml) via manual dispatch. This performs a deep secret scan across the full git history. This step is optional but recommended.

### Step 4: Go public

The OSPO lead manually changes the repo visibility to public in GitHub Settings. Once public, GitHub native features (Secret Scanning, CodeQL default setup) activate automatically. The compliance workflow will then query their APIs instead of running TruffleHog.

## WB IGO Riders

Repos using MIT license must include [WB-IGO-RIDER.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md).

Repos using Apache-2.0 license must include [WB-IGO-RIDER-APACHE.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER-APACHE.md).

The compliance workflow validates that the rider content matches the canonical version.
