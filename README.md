# Open Source Compliance Kit

Reusable GitHub Actions workflow for open source compliance checks.

## Checks

- **License** - Whitelist: MIT, Apache-2.0. Requires WB IGO Rider for each.
- **README** - Presence and content checks
- **Secrets** - TruffleHog scan (working tree + optional history)
- **Data Files** - Warns on large data files; suggests data catalog
- **Dependencies** - Dependabot API for vulnerability alerts
- **Code Quality (Basic)** - Local linters (eslint/ruff/flake8) or Super-Linter fallback
- **Code Quality (Sonar)** - SonarCloud analysis
- **Tech Stack** - GitHub Languages API + framework detection (informational)
- **AI Usage** - Detects AI library usage (informational)

On the default branch, a **compliance issue** is automatically created/updated with a checklist of results. The issue closes when all checks pass.

## Org Prerequisites

1. Enable **Dependabot alerts** org-wide: Settings > Code security > Dependabot alerts

2. Create/confirm a **SonarCloud** organization linked to your GitHub org

3. In **GitHub Org Secrets**, add:
   - `SONAR_TOKEN` - SonarCloud user token with "Execute Analysis"
   - `SONAR_ORG_KEY` - Your SonarCloud org key
   - `DEPENDABOT_TOKEN` *(optional)* - PAT with `security_events` scope for Dependabot API access on private repos

## How Teams Adopt

Add a caller workflow to each repo:

```yaml
# .github/workflows/compliance.yml
name: Open Source Compliance
on:
  push:
  pull_request:
  schedule: [{ cron: '17 2 * * *' }]
  workflow_dispatch:
    inputs:
      history_depth:
        description: 'Commits to scan for secrets (0 = off)'
        type: number
        default: 0
permissions:
  contents: read
  security-events: write
  actions: read
  checks: write
  pull-requests: read
  statuses: write
  issues: write
jobs:
  run:
    uses: itsapdemo/open-source-kit/.github/workflows/repo-compliance.yml@main
    with:
      history_depth: ${{ inputs.history_depth || 0 }}
    secrets: inherit
```

## WB IGO Riders

Repos using MIT license must include [WB-IGO-RIDER.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md).

Repos using Apache-2.0 license must include [WB-IGO-RIDER-APACHE.md](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER-APACHE.md).

The compliance workflow validates that the rider content matches the canonical version.
