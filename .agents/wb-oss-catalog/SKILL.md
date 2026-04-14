---
name: wb-oss-catalog
description: >
  Audits and prepares a GitHub repository for endorsement in the World Bank Group (WBG) Open Source Code Catalog.
  Use this skill whenever a user mentions submitting a repo to the World Bank open source catalog,
  WBG OSS endorsement, preparing a repo for World Bank review, or wants to check/fix a repository against
  the WBG checklist. Also trigger when a user says their repo needs the WB license, citation file, code of
  conduct, contributing guide, or any combination of World Bank open source requirements. Even if they just
  say "prepare my repo for the World Bank catalog" or "audit my repo for WBG", use this skill.
---

# WBG Open Source Code Catalog — Repo Preparer

This skill helps users audit and prepare a GitHub repository for endorsement in the World Bank Group Open Source Code Catalog. You will scan the repo, identify gaps against the official checklist, generate a clear status report, and help create or fix any missing files.

## Workflow

### Step 1: Understand the target repo

Ask the user which directory to audit (or confirm if a path is already clear from context). Then scan:

- Root file listing (check for README.md, LICENSE, CITATION.cff, CODE_OF_CONDUCT.md, CONTRIBUTING.md, `.env*`, `*.bib`)
- Contents of README.md (if it exists)
- Any existing LICENSE file
- `.gitignore` or `.env.example` patterns
- A quick search for potential secrets and hard-coded values

Do this scanning in parallel where possible to move fast.

### Step 2: Generate the audit report

Produce a structured checklist report with status icons for each requirement. Use this format:

```
## WBG Open Source Catalog — Audit Report

### ✅ / ⚠️ / ❌  [Requirement Name]
**Status**: Pass / Needs Work / Missing
**Finding**: [what you found]
**Action needed**: [what to do, if anything]
```

Work through all 10 requirements (see reference below). Be specific — don't just say "README is missing a section", say *which* section and what content would satisfy it.

### Step 3: Offer to fix things

After the report, ask the user: "Would you like me to create or update any of these files?" Then do what they ask, one file at a time. Use the templates in `references/templates.md` as your starting point, but always personalize with real project details (name, description, contact info, etc.) gathered from the repo or by asking the user.

When creating files, prefer to update existing files rather than overwrite them wholesale — especially README.md.

---

## The 10 Checklist Requirements

Read `references/checklist.md` for the full detail on each requirement. Here's the quick summary:

| # | Requirement | Key Check |
|---|-------------|-----------|
| 1 | README.md | Project name, description (2-3 sentences), screenshot if applicable, Getting Started, docs link, contact (@worldbank.org), license notice |
| 2 | Repository Details | Description, website/docs link, relevant topics set in GitHub repo settings |
| 3 | License | MIT License + WB IGO Rider; specific notice text at bottom of README |
| 5 | Documentation | Web-based docs (GitHub Pages, Jupyter Book, etc.) accessible to non-technical audiences |
| 6 | CITATION.cff | Citation file using CFF format for reproducible research |
| 7 | Code of Conduct | CODE_OF_CONDUCT.md present or linked |
| 8 | Contributing Guide | CONTRIBUTING.md present using WB template |
| 9 | Exclusions | No original data, no secrets/API keys, avoid hard-coded variables |
| 10 | Bibliography (optional) | BibTeX `.bib` file in `docs/` |

*(Note: item 4 is not in the checklist — items go 1, 2, 3, 5, 6, 7, 8, 9, 10.)*

---

## Scanning for Exclusion Violations (Requirement 9)

This is the trickiest requirement because violations may be hard to spot.

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

- Be direct and actionable. Users are typically World Bank staff or contractors who want to get through this process efficiently.
- When something is ambiguous (e.g., "does this README have a description?"), use your judgment and explain your reasoning.
- Don't be preachy about open source best practices beyond what's in the checklist.
- For items 7 and 8 (Code of Conduct, Contributing Guide), the WB provides official templates — users should use those exact files, not write their own.

---

## Reference Files

- `references/checklist.md` — Full detail on each requirement, including required text verbatim and template links
- `references/templates.md` — Starter templates for README sections, CITATION.cff, and the license notice
