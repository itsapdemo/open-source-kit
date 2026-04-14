# Templates for WBG Open Source Catalog Requirements

These are *starting points*, not fill-in-the-blank forms. Before generating any file, read the repo's existing code, structure, and any existing docs to understand what the project actually does. Adapt language, structure, and examples to match the project type (library, CLI tool, web app, research scripts, data pipeline, etc.).

---

## README.md — How to Write a Good One

The README should feel like it was written by someone who understands the project deeply. Read the code and existing docs first.

**Project types and their README emphasis:**
- **Library/package**: Lead with a code snippet showing the main use case. Emphasize API and installation.
- **Web application**: Screenshot is important. Focus on deployment and getting the app running.
- **Research scripts / notebooks**: Emphasize data inputs/outputs, reproducibility, and what the outputs mean.
- **CLI tool**: Show command examples prominently in Getting Started.
- **Monorepo**: Show the package structure clearly, then Getting Started per component.

### Required sections (in order):

```markdown
# [Project Name]

[2-3 sentence description: what does this do and who is it for? Be specific about the problem solved.]

> **Audience**: [Optional but helpful — who will use this?]

[Screenshot or diagram — only if the project has visual output; omit if purely code/data]
![Description](docs/screenshot.png)

## [Problem / Background — if complex enough to warrant it]

[Optional: what problem does this solve and why does it matter?]

## Key Features / How It Works

[Optional but useful for non-trivial projects]

## Getting Started

### Prerequisites

[What the user needs installed before they can use this]

### Installation

[Exact commands to install and set up]

### Usage

[One or more concrete examples showing real usage]

## Documentation

[Link to full documentation site — required. If docs don't exist yet, note they're forthcoming and link to the docs/ folder]

## Contact

[World Bank staff name + @worldbank.org email. This is required for WBG catalog endorsement.
External/personal emails won't satisfy the requirement — the contact must be a WB staff member.]

## License

This project is licensed under the MIT License together with the World Bank IGO Rider.
The Rider is purely procedural: it reserves all privileges and immunities enjoyed by the
World Bank, without adding restrictions to the MIT permissions. Please review both files
before using, distributing or contributing.

See [LICENSE](LICENSE) for the full license text.
```

### The license notice (verbatim — do not paraphrase)

The following exact text must appear at the bottom of the README:

```
This project is licensed under the MIT License together with the World Bank IGO Rider.
The Rider is purely procedural: it reserves all privileges and immunities enjoyed by the
World Bank, without adding restrictions to the MIT permissions. Please review both files
before using, distributing or contributing.
```

---

## CITATION.cff — Starter Template

```yaml
cff-version: 1.2.0
message: "If you use this software, please cite it as below."
type: software
title: "[Project Title]"
abstract: "[One or two sentence description]"
authors:
  - family-names: "[LastName]"
    given-names: "[FirstName]"
    affiliation: "World Bank"
    email: "[email@worldbank.org]"
version: "1.0.0"
date-released: "[YYYY-MM-DD]"
license: MIT
repository-code: "https://github.com/worldbank/[repo-name]"
keywords:
  - "[keyword1]"
  - "[keyword2]"
  - "world bank"
```

If the project has an associated paper or preprint, add:
```yaml
preferred-citation:
  type: article
  title: "[Paper title]"
  authors:
    - family-names: "[LastName]"
      given-names: "[FirstName]"
  journal: "[Journal or arXiv]"
  year: [YYYY]
  url: "[DOI or URL]"
```

Full template reference: https://github.com/worldbank/template/blob/main/CITATION.cff

---

## LICENSE — MIT License

```
MIT License

Copyright (c) [year] The World Bank

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

The WB IGO Rider must also be present. Either:
- Fetch the current text from https://github.com/worldbank/.github/blob/main/WB-IGO-RIDER.md and save as `WB-IGO-RIDER.md`
- Or create `WB-IGO-RIDER.md` that clearly references the canonical URL

---

## CODE_OF_CONDUCT.md

Do NOT write a custom Code of Conduct. Fetch and use the official WB template:
https://github.com/worldbank/.github/blob/main/CODE_OF_CONDUCT.md

---

## CONTRIBUTING.md

Do NOT write a custom Contributing guide. Fetch and use the official WB template:
https://github.com/worldbank/.github/blob/main/CONTRIBUTING.md

---

## .env.example — Template

If the project uses environment variables (check for `os.getenv`, `process.env`, dotenv usage, etc.):

```bash
# .env.example
# Copy this file to .env and fill in your values.
# Do NOT commit your actual .env file.

# [Group: e.g., API Configuration]
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com

# [Group: e.g., Database]
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

---

## Simple docs/index.md (for GitHub Pages)

If the user needs minimal web documentation to satisfy Requirement 5:

```markdown
# [Project Name]

[Same description as README]

## Overview

[What this project does, who it's for, and why it exists]

## Getting Started

See the [README](https://github.com/worldbank/[repo-name]#readme) for installation and usage.

## User Guide

[Key documentation — be accessible to non-technical readers here]

## Contact

[Contact info]
```

To enable GitHub Pages from a `docs/` folder:
1. Push the file to `docs/index.md` (or `docs/index.html`) on the default branch
2. Go to GitHub repo Settings → Pages
3. Set Source to "Deploy from a branch", Branch = `main`, folder = `/docs`
4. Save — site publishes at `https://worldbank.github.io/[repo-name]`

---

## Bibliography template (optional, docs/bibliography.bib)

```bibtex
@article{author2024title,
  title   = {Full Paper Title},
  author  = {Author, First and Coauthor, Second},
  journal = {Journal Name},
  year    = {2024},
  volume  = {1},
  number  = {1},
  pages   = {1--10},
  doi     = {10.xxxx/xxxxx}
}
```

Template reference: https://github.com/worldbank/template/blob/main/docs/bibliography.bib
