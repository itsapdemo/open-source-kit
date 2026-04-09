import os, json

DATA_EXT = {".csv",".tsv",".parquet",".xlsx",".zip",".gz",".jsonl",".feather",".sav",".dta",".rds",".db",".sqlite",".shp",".geojson",".gpkg"}
MAX_INLINE_BYTES = 512 * 1024

violations = []  # Large files that should use external storage
detected = []    # All data files found

for root,_,files in os.walk("."):
    if root.startswith("./.git"): continue
    for f in files:
        ext = os.path.splitext(f)[1].lower()
        if ext in DATA_EXT:
            path = os.path.join(root,f)
            try:
                size = os.path.getsize(path)
            except OSError:
                continue
            detected.append(path)
            if size > MAX_INLINE_BYTES:
                violations.append((path, size))

# Report violations
if violations:
    print("Large data files detected (>512KB):")
    for p,s in violations:
        print(f"::error::{p} is {s:,} bytes; must use Git LFS or external storage")
    exit(1)

# Report detected data files (informational)
if detected:
    print(f"Data files detected ({len(detected)}):")
    for p in detected[:10]:
        print(f"  - {p}")
    if len(detected) > 10:
        print(f"  ... and {len(detected) - 10} more")

# Output for GitHub Actions
if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f:
        f.write(f"violations={json.dumps([p for p,s in violations])}\n")
        f.write(f"detected={json.dumps(detected[:20])}\n")
        f.write(f"count={len(detected)}\n")
