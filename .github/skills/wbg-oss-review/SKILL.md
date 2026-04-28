---
name: wbg-oss-review
description: >
  OSPO lead failsafe review for World Bank Group (WBG) open source publication.
  This is Stage 2 of a two-stage process: Stage 1 is the automated compliance
  workflow (CI) that runs on every push/PR; Stage 2 is this skill, invoked manually
  by the OSPO lead before approving publication. Works with the compliance workflow
  results and intranet request form data to audit the repo, fix compliance failures,
  and generate PR content. Use this skill when a user mentions: preparing a repo for
  open source, WBG compliance review, fixing compliance failures, World Bank
  license/rider requirements, open source publication, or "review this repo".
---

# WBG Open Source Review — Copilot Agent Skill

This skill is the OSPO lead's **failsafe review** (Stage 2) before approving a repository for public release.

The review process has two stages:

1. **Stage 1 — Automated CI**: The team adds the compliance workflow to their repo. It runs on every push/PR/daily and creates a compliance issue with pass/fail results. This is the initial gate and the ongoing check after the repo is public.
2. **Stage 2 — OSPO Review (this skill)**: The OSPO lead clones the repo, copies this skill in, and invokes it. The skill cross-references the automated results with the intranet request form, independently audits the repo, analyzes subjective fields (risk, maintenance, licensing), and generates fixes + PR content.

After Stage 2 approval, the OSPO lead manually changes the repo visibility to public. GitHub native features (Secret Scanning, CodeQL default setup) activate automatically once the repo is public.

The user handles all GitHub interactions (creating branches, PRs, and changing repo visibility).

## Reference Files

- `./references/checklist.md` — Compliance checklist: all requirements, what to check, and form-field review items
- `./references/templates.md` — Starter templates for README, CITATION.cff, LICENSE, etc. with placeholder tokens

## Workflow

### Phase 1: Inputs

#### Step 1: Get the compliance issue report (Stage 1 output)

Ask the user to paste the compliance issue content from the target repo. This issue is auto-created by the Stage 1 automated compliance workflow (labeled `compliance`, titled "Open Source Compliance Check: {repo}") and contains:

- A checklist of pass/fail results for: License, README, Secrets, Data Files, Dependencies, Code Quality (Basic), Code Quality (CodeQL)
- Informational results: Languages, Frameworks, AI Usage, Data Files detected, GitHub Native Integration status

Extract which checks passed and which failed. If the user hasn't run the workflow yet, tell them to add the compliance workflow (`.github/workflows/compliance.yml`) from the open-source-kit, push to the default branch, and check the issue it creates.

**Note on native GitHub features**: Secrets, Dependencies, and CodeQL are queried from GitHub's native APIs (Secret Scanning, Dependabot, Code Scanning) — not duplicated. For private repos, Secret Scanning uses TruffleHog as a fallback and CodeQL shows as "skipped". Both activate natively once the repo is made public.

#### Step 2: Get the intranet request form data

Ask the user to paste the details from the intranet open source request. Extract:

- **Project name** and **description** — use for README, CITATION.cff
- **Ownership / team lead** — use for contact info, CITATION.cff authors
- **Tech stack** — informs .gitignore, documentation, and Getting Started guidance
- **AI enablement** — cross-reference with detect_ai_use.py results
- **Request type** — determines README emphasis (application vs library vs research)
- **Third-party licensing** — analyzed in Step 4
- **Data source** — cross-reference with data files check
- **Risk assessment** — analyzed in Step 4
- **Maintenance strategy** — analyzed in Step 4
- **Community engagement** — analyzed in Step 4
- **End of support** — analyzed in Step 4

If the user provides both inputs at once, extract everything and proceed. If they provide only one, ask for the other.

### Phase 2: Validate & Analyze

#### Step 3: Re-audit the repository

Independently validate the workflow results by scanning the repo locally. This is the "trust but verify" step.

Scan in parallel:
- Root file listing (check for README.md, LICENSE, CITATION.cff, CODE_OF_CONDUCT.md, CONTRIBUTING.md, `.env*`, `.bib`, WB-IGO-RIDER*.md, .gitignore)
- Contents of README.md — check for required sections, @worldbank.org contact, verbatim license notice
- LICENSE file — determine MIT vs Apache-2.0, check that the correct rider file is present
- .gitignore patterns — check coverage for the detected tech stack
- Quick search for secrets, API keys, hard-coded paths, and sensitive data

Cross-reference findings with the compliance issue from Step 1:
- **If the workflow reported a failure**: confirm the issue exists and determine the specific fix needed
- **If the workflow reported a pass**: verify it — flag any discrepancies found
- **If something wasn't covered by the workflow**: report it as a new finding

Use `references/checklist.md` as the reference for what each requirement needs.

#### Step 4: Analyze form fields (f1–f5)

Analyze the intranet form fields that cannot be validated by scanning files. For each, produce observations and recommendations.

**Third-Party Licensing (f1)**
- Check if listed dependencies include copyleft licenses (GPL, AGPL, LGPL, SSPL)
- If the repo has `package.json` or `requirements.txt`, cross-reference actual dependencies against what was declared
- Flag any incompatibilities with the repo's chosen license (MIT/Apache-2.0)
- Recommend license-checker tools if dependencies are numerous

**Risk Assessment (f2)**
- Flag security concerns (e.g., "handles authentication" + no security audit mentioned)
- Flag reputational risks (e.g., sensitive policy topics without disclaimers)
- Flag data sensitivity (cross-reference with data_source field and data files check results)
- Recommend mitigations for identified risks

**Maintenance Strategy (f3)**
- Check for named maintainers (not just "the team")
- Check for concrete timeline (not just "ongoing")
- Flag if funding source has a known end date but no succession plan

**Community Engagement (f4)**
- Check for response-time commitments
- Check for PR/issue handling process
- Flag if empty or generic ("we'll engage with the community")
- Recommend standard practices if strategy is thin

**End of Support (f5)**
- Check for concrete archival plan
- Check for user notification strategy
- Flag if missing or vague
- Recommend adding an archival notice template to README

### Phase 3: Fix

#### Step 5: Create or update files locally

Based on compliance failures from Step 1/3 and audit findings, create or update files in the working directory. Use form data from Step 2 to populate templates from `./references/templates.md`.

- **README.md** — Use project name from form, description, contact from ownership field. Match the README emphasis to the request type (application → screenshot + deployment, library → code snippet + API, research → data + reproducibility). Prefer updating existing README over wholesale replacement.
- **LICENSE** — Use the license choice. If not specified, check existing LICENSE or default to MIT.
- **WB-IGO-RIDER.md / WB-IGO-RIDER-APACHE.md** — Fetch canonical text from worldbank/.github.
- **CITATION.cff** — Use project name, team lead name, license choice from form.
- **CODE_OF_CONDUCT.md** — Use the official WB template only (no custom versions).
- **CONTRIBUTING.md** — Use the official WB template only (no custom versions).
- **.gitignore** — Generate based on detected tech stack.
- **.env.example** — If environment variables were detected, create a template.

### Phase 4: PR Content & Summary

#### Step 6: Generate PR content

Generate content for a pull request that the user will create manually in GitHub. Output the following clearly labeled so the user can copy-paste:

**PR Title:**
```
chore: add WBG open source compliance files
```

**PR Description:**
```markdown
## Open Source Compliance Fixes

This PR addresses the compliance check failures identified in #{issue_number}.

### Changes

- [list each file created or updated and what changed]

### Checklist

- [ ] README.md has required sections (name, description, Getting Started, docs link, contact, license notice)
- [ ] LICENSE file is MIT or Apache-2.0
- [ ] WB IGO Rider file matches the license type
- [ ] CITATION.cff is present with required fields
- [ ] CODE_OF_CONDUCT.md uses official WB template
- [ ] CONTRIBUTING.md uses official WB template
- [ ] .gitignore covers the tech stack
- [ ] No data files, secrets, or hard-coded values committed

### Review Observations

[Include the form-field analysis from Step 4 — third-party licensing flags, risk assessment, maintenance gaps, etc.]

### Next Steps

Once merged, the compliance workflow will re-run automatically. When all required checks pass, the compliance issue will close (code quality checks are optional and won't block closure). After that, the repo visibility can be changed to public.
```

#### Step 7: Report to user

Summarize everything:

1. **What was fixed** — list each file created or updated and what changed
2. **What still needs manual action**:
   - Set GitHub repo About: description, website, topics (Requirement 2)
   - Set up documentation site — GitHub Pages, Jupyter Book, etc. (Requirement 5)
   - Create a branch and commit the changes
   - Create the PR using the content above
3. **Form-field observations** — recap the key flags from Step 4
4. **After the PR merges**:
   - Compliance workflow re-runs on push to default branch
   - When all required checks pass, the compliance issue closes automatically (code quality is optional)
   - Then change repo visibility to public

---

## The 10 Checklist Requirements

Read `references/checklist.md` for the full detail on each requirement. Quick reference:

| # | Requirement | Check Type | Key Check |
|---|-------------|------------|-----------|
| 1 | README.md | automated | Name, description, Getting Started, docs link, @worldbank.org contact, verbatim license notice |
| 2 | Repository Details | manual | GitHub About: description, website, topics |
| 3 | License | automated | MIT or Apache-2.0 + matching WB IGO Rider |
| 5 | Documentation | manual | Web-based docs (GitHub Pages, Jupyter Book, etc.) |
| 6 | CITATION.cff | automated | CFF format with required fields |
| 7 | CODE_OF_CONDUCT.md | automated | Official WB template |
| 8 | CONTRIBUTING.md | automated | Official WB template |
| 9 | Exclusions | automated | No data files, no secrets, no hard-coded values |
| 10 | Bibliography | automated (optional) | BibTeX .bib in docs/ |

*(Item 4 is not in the checklist — numbering goes 1, 2, 3, 5, 6, 7, 8, 9, 10.)*

### License choice (MIT vs Apache)

| Base license | IGO rider (canonical) |
|--------------|------------------------|
| MIT License | [`WB-IGO-RIDER.md`](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md) |
| Apache License, Version 2.0 | [`WB-IGO-RIDER-APACHE.md`](https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER-APACHE.md) |

Do not mix riders. README notice must match. See `references/checklist.md` requirement 3, and `references/templates.md` for the verbatim notice blocks.

---

## Scanning for Exclusion Violations (Requirement 9)

**Secrets/API keys**: Search for common patterns:
- Files named `.env`, `secrets.yaml`, `credentials.json`, `config.py` containing keys
- Strings matching patterns like `sk-`, `AKIA`, `Bearer `, `password =`, `api_key =`
- Check `.gitignore` — secrets files should be listed there

**Hard-coded variables**: Look for:
- Literal IP addresses, database connection strings
- Hard-coded file paths (e.g., `/home/username/...`, `C:\Users\...`)
- Hard-coded URLs that should be configuration

**Data files**: Look for:
- Large files or directories named `data/`, `datasets/`, `raw/`
- `.csv`, `.xlsx`, `.shp`, `.geojson`, `.parquet`, `.db` files committed to the repo
- If found, flag them — data should live in the World Bank Data Catalog, SharePoint, or similar

Report findings with specific file paths so the user can act on them.

---

## Tone and Communication

- Be direct and actionable. Users are World Bank staff or reviewers processing publication requests.
- When something is ambiguous, use judgment and explain reasoning.
- Don't be preachy beyond what's in the checklist.
- For CODE_OF_CONDUCT and CONTRIBUTING, insist on the official WB templates — no custom versions.
