#!/usr/bin/env python3
"""earth-now archive retention tool (safe by default: DRY RUN unless --apply).

The hourly archive keeps one JSON snapshot per hour (8760-cap manifest). Each
snapshot is small (<1MB) and compresses well, so git remains the right storage;
the growth risk is unbounded accumulation over months/years. This tool caps the
archive at a retention window, keeps the manifest contract
(earth-now.archive.v1) valid, and never touches latest.json.
"""
import argparse, datetime, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH_RE = re.compile(r"^dynamic/archive/(\d{4})/(\d{2})/(\d{2})/(\d{2})\.json$")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=90, help="retention window (default 90 days)")
    ap.add_argument("--max-snapshots", type=int, default=8760, help="manifest cap (contract allows <=8760)")
    ap.add_argument("--apply", action="store_true", help="actually delete (default: dry run)")
    args = ap.parse_args()

    archive = ROOT / "dynamic" / "archive"
    index_path = archive / "index.json"
    if not index_path.exists():
        sys.exit("no archive manifest found; nothing to do")
    manifest = json.loads(index_path.read_text())
    if manifest.get("schema") != "earth-now.archive.v1":
        sys.exit("unexpected manifest schema; refusing")

    cutoff = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=args.days)
    keep, drop = [], []
    for snap in manifest.get("snapshots", []):
        m = PATH_RE.match(snap.get("path", ""))
        if not m:
            keep.append(snap); continue
        ts = datetime.datetime(*map(int, m.groups()), tzinfo=datetime.timezone.utc)
        (keep if ts >= cutoff else drop).append(snap)

    excess = max(0, len(keep) - args.max_snapshots)
    if excess:
        drop_ids = {id(s) for s in keep[:excess]}
        drop.extend(s for s in keep if id(s) in drop_ids)
        keep = [s for s in keep if id(s) not in drop_ids]

    print(f"retention window: {args.days} days (cutoff {cutoff.isoformat()})")
    print(f"snapshots: {len(keep)} kept, {len(drop)} to remove")
    total = 0
    for s in drop:
        p = ROOT / s["path"]
        if p.exists():
            total += p.stat().st_size
        print(("WOULD DELETE " if not args.apply else "DELETING    ") + s["path"])
    print(f"space reclaimed: {total/1_000_000:.1f} MB")

    if not args.apply:
        print("dry run - no changes made. Re-run with --apply to execute.")
        return

    for s in drop:
        p = ROOT / s["path"]
        if p.exists():
            p.unlink()
    for day in archive.glob("*/*/*"):
        if day.is_dir() and not any(day.iterdir()):
            day.rmdir()
    manifest["snapshots"] = keep
    manifest["updated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    index_path.write_text(json.dumps(manifest, separators=(",", ":")))

    m2 = json.loads(index_path.read_text())
    assert m2["schema"] == "earth-now.archive.v1" and len(m2["snapshots"]) <= args.max_snapshots
    missing = [s["path"] for s in m2["snapshots"] if not (ROOT / s["path"]).exists()]
    if missing:
        sys.exit(f"CONTRACT VIOLATION: {len(missing)} manifest entries missing files; restore from git")
    print(f"done: {len(keep)} snapshots retained, manifest valid")

if __name__ == "__main__":
    main()
