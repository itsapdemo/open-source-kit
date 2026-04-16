# Open Source Compliance Kit

Reusable GitHub Actions workflow and VS Code Copilot skill for World Bank open source compliance.

## Checks

- **License** — Whitelist: MIT, Apache-2.0. Requires WB IGO Rider for each.
- **README** — Presence and content checks
- **Secrets** — TruffleHog scan (working tree + optional history)
- **Data Files** — Warns on large data files; suggests data catalog
- **Dependencies** — Dependabot API for vulnerability alerts
- **Code Quality (Basic)** — Local linters (eslint/ruff/flake8) or Super-Linter fallback
- **Code Quality (CodeQL)** — GitHub CodeQL analysis (public repos only, free tier)
- **Tech Stack** — GitHub Languages API + framework detection (informational)
- **AI Usage** — Detects AI library usage (informational)

On the default branch, a **compliance issue** is automatically created/updated with a checklist of results. The issue closes when all checks pass.

## Org Prerequisites

1. Enable **Dependabot alerts** org-wide: Settings > Code security > Dependabot alerts

2. *(Optional)* In **GitHub Org Secrets**, add:
   - `DEPENDABOT_TOKEN` — PAT with `security_events` scope for Dependabot API access on private repos

## How Teams Adopt

### Step 1: Add the compliance workflow

Copy [`.github/compliance/sample-per-repo-caller.yml`](.github/compliance/sample-per-repo-caller.yml) to the target repo as `.github/workflows/compliance.yml`. Push to the default branch. The workflow runs automatically and creates a compliance issue with a checklist of results.

### Step 2: Copy the Copilot skill

Copy the [`.github/skills/wbg-oss-review/`](.github/skills/wbg-oss-review/) directory to the target repo. This gives VS Code access to the review skill.

### Step 3: Fix compliance failures

1. Clone the target repo and open it in VS Code
2. Invoke the **wbg-oss-review** skill in Copilot
3. Provide: (a) the compliance issue content and (b) the intranet request form data
4. The skill audits the repo, creates/updates compliance files, and generates PR content
5. Create a branch, commit the changes, and open a PR using the generated content
6. The requestor merges the PR — the compliance workflow re-runs automatically
7. When all checks pass, the compliance issue closes
8. Change the repo visibility to public

## WB IGO Riders

Repos using MIT license must include [WB-IGO-RIDER.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md).

Repos using Apache-2.0 license must include [WB-IGO-RIDER-APACHE.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER-APACHE.md).

The compliance workflow validates that the rider content matches the canonical version.
