# WBG Open Source Code Catalog — Full Checklist Reference

## Requirement 1: README.md

The README.md must include ALL of the following:

### 1a. Project Name
A clear heading with the project name.

### 1b. Description (2-3 sentences)
Clear description of purpose and target audience. Should answer: what does this do, and who is it for?

### 1c. Screenshot (if applicable)
If the software has a visual output (UI, charts, maps, etc.), include at least one screenshot or example output image.

### 1d. Getting Started
Must cover prerequisites, installation guidance, and at least one usage example. May vary by project type (CLI tool, Python library, web app, etc.).

### 1e. Documentation link
Link to thorough documentation — either within the README or pointing to a separate page (GitHub Pages, Read the Docs, etc.).

### 1f. Contact Information
Must include World Bank staff names and their `@worldbank.org` email addresses, OR a mailbox/distribution list. Personal emails outside WB domain do not count.

### 1g. License Notice
The following **exact text** must appear at the bottom of the README:

```
This project is licensed under the MIT License together with the World Bank IGO Rider.
The Rider is purely procedural: it reserves all privileges and immunities enjoyed by the
World Bank, without adding restrictions to the MIT permissions. Please review both files
before using, distributing or contributing.
```

---

## Requirement 2: Repository Details (GitHub Settings)

In the GitHub repository's "About" section (top-right of repo homepage), the user must set:

- **Description**: A clear one-line description (used for catalog entries and search). Should describe what the repo does.
- **Website**: Link to documentation/project page (see Requirement 5).
- **Topics**: Relevant tags/keywords to help people discover the repo.

This cannot be checked by reading files — ask the user to confirm or tell them to set it manually in GitHub repo settings.

---

## Requirement 3: License

If no license exists, the repo must adopt:
- **MIT License** (standard text)
- **World Bank IGO Rider**: https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md

Both should be present. Typically:
- `LICENSE` or `LICENSE.md` — the MIT License text
- `LICENSE-IGO-RIDER.md` or similar — the WB IGO Rider, OR a reference/link to the official one

The README must also contain the notice text from Requirement 1g.

---

## Requirement 5: Documentation

The repo must have accompanying web-based documentation accessible to non-technical audiences.

Acceptable forms:
- GitHub Pages (simple HTML/Markdown)
- Jupyter Book (common with WB Data Science Template)
- Read the Docs
- Any external documentation website

The documentation link must appear in:
1. The README.md
2. The GitHub repository "Website" field (Requirement 2)

If no docs exist, suggest the user create a simple GitHub Pages site from a `docs/` folder or `index.md`.

---

## Requirement 6: CITATION.cff

A `CITATION.cff` file at the repo root.

Format: [Citation File Format (CFF)](https://citation-file-format.github.io/)

Template available at: https://github.com/worldbank/template/blob/main/CITATION.cff

Minimum required fields:
```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
title: "Project Title"
authors:
  - family-names: "LastName"
    given-names: "FirstName"
    affiliation: "World Bank"
version: "1.0.0"
date-released: "YYYY-MM-DD"
```

---

## Requirement 7: Code of Conduct

A `CODE_OF_CONDUCT.md` file must be present in the repo.

Use the official WB template: https://github.com/worldbank/.github/blob/main/CODE_OF_CONDUCT.md

Do NOT write a custom code of conduct — use the official WB template.

---

## Requirement 8: Contributing Guide

A `CONTRIBUTING.md` file must be present in the repo.

Use the official WB template: https://github.com/worldbank/.github/blob/main/CONTRIBUTING.md

Do NOT write a custom contributing guide — use the official WB template.

---

## Requirement 9: Exclusions

The repo must NOT contain:

### 9a. Original data
Data files should NOT be stored in the repo. They should live in:
- World Bank Data Catalog
- SharePoint
- OneDrive
- External data repositories

Files to flag: `.csv`, `.xlsx`, `.xls`, `.ods`, `.db`, `.sqlite`, `.parquet`, `.feather`, `.shp`, `.geojson`, `.gpkg`, and directories named `data/`, `datasets/`, `raw/`, `input/`.

Exception: small example/sample data files for documentation purposes may be acceptable — use judgment.

### 9b. Secrets and API keys
Must not be committed. Common patterns to check:
- Files: `.env`, `secrets.yaml`, `secrets.json`, `credentials.json`, `config.local.*`
- Content patterns: `password`, `api_key`, `secret`, `token`, `AKIA` (AWS), `sk-` (OpenAI), `Bearer `
- Check `.gitignore` to see if secret files are properly excluded

A `.env.example` or `.env.sample` is acceptable (and encouraged) to show required variables.

### 9c. Hard-coded variables
Avoid hard-coded:
- File paths with usernames (e.g., `/home/jdoe/`, `C:\Users\jdoe\`)
- Database connection strings
- IP addresses and hostnames
- URLs that should be configurable
- Magic numbers that should be named constants

---

## Requirement 10: Bibliography (Optional)

If the project references academic literature, include a BibTeX bibliography file.

Location: `docs/bibliography.bib` (or similar)
Format: [BibTeX](https://www.bibtex.org/Format/)
Template: https://github.com/worldbank/template/blob/main/docs/bibliography.bib

If using Jupyter Book: see [Citations and bibliographies](https://jupyterbook.org/en/stable/content/citations.html).
