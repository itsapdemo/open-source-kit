import json, os, tomllib

def exists(*names): return any(os.path.exists(n) for n in names)

frameworks = []
if os.path.exists("package.json"):
    import json as _json
    try:
        pj = _json.load(open("package.json"))
        deps = (pj.get("dependencies") or {}) | (pj.get("devDependencies") or {})
        for k in deps:
            if k in ("react","next","vue","svelte","vite","angular"): frameworks.append(k)
            if k in ("express","fastify","koa","nest"): frameworks.append(k)
    except Exception: pass

if os.path.exists("pyproject.toml"):
    try:
        py = tomllib.load(open("pyproject.toml","rb"))
        if "tool" in py and "poetry" in py["tool"]: frameworks.append("poetry")
        if "project" in py and "dependencies" in py["project"]:
            for d in py["project"]["dependencies"]:
                if isinstance(d,str) and any(x in d.lower() for x in ("django","fastapi","flask","pydantic")):
                    frameworks.append(d.split()[0])
                if isinstance(d,str) and "pyspark" in d.lower():
                    frameworks.append("spark")
    except Exception: pass

# Spark detection in requirements.txt
if os.path.exists("requirements.txt"):
    try:
        with open("requirements.txt") as f:
            reqs = f.read().lower()
            if "pyspark" in reqs:
                frameworks.append("spark")
    except Exception: pass

# Databricks detection (config files or notebook source markers)
if exists("databricks.yml","databricks.yaml",".databricks","bundle.yml"):
    frameworks.append("databricks")

# Check for Databricks notebook markers in source files
databricks_markers = {
    ".py": "# Databricks notebook source",
    ".r": "# Databricks notebook source",
    ".scala": "// Databricks notebook source",
    ".sql": "-- Databricks notebook source"
}
for ext, marker in databricks_markers.items():
    for f in [f for f in os.listdir(".") if f.endswith(ext)]:
        try:
            with open(f) as fp:
                if marker in fp.readline():
                    frameworks.append("databricks")
                    break
        except Exception: pass
    if "databricks" in frameworks: break

# Check Jupyter notebooks for Databricks
for nb in [f for f in os.listdir(".") if f.endswith(".ipynb")]:
    try:
        with open(nb) as f:
            content = f.read()
            if "Databricks notebook source" in content or '"databricks"' in content.lower():
                frameworks.append("databricks")
                break
    except Exception: pass

result = {"frameworks": sorted(set(frameworks))}
print(json.dumps(result, indent=2))

# Output for GitHub Actions
if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"frameworks={json.dumps(sorted(set(frameworks)))}\n")

