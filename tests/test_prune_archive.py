import json, pathlib, subprocess, sys, tempfile, unittest, importlib.util
ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("prune", ROOT / "scripts" / "prune-archive.py")
prune = importlib.util.module_from_spec(spec); spec.loader.exec_module(prune)

class PruneArchive(unittest.TestCase):
    def _sandbox(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name)
        archive = root / "dynamic" / "archive" / "2026" / "01" / "01"
        archive.mkdir(parents=True)
        for h in ("00", "01", "02"):
            (archive / f"{h}.json").write_text('{"schema":"earth-now.atlas.v1"}')
        index = root / "dynamic" / "archive" / "index.json"
        index.write_text(json.dumps({"schema": "earth-now.archive.v1", "snapshots": [
            {"at": f"2026-01-01T{h}:00:00Z", "path": f"dynamic/archive/2026/01/01/{h}.json", "events": 1}
            for h in ("00", "01", "02")], "updated_at": "2026-01-01T00:00:00Z"}))
        return root, index

    def test_dry_run_changes_nothing(self):
        root, index = self._sandbox()
        before = index.read_text()
        # Patch ROOT to the sandbox.
        orig = prune.ROOT; prune.ROOT = root
        try:
            rc = prune.main.__wrapped__ if hasattr(prune.main, "__wrapped__") else None
            sys.argv = ["prune", "--days", "1"]
            prune.main()
        finally:
            prune.ROOT = orig
        self.assertEqual(index.read_text(), before, "dry run must not modify manifest")
        self.assertTrue((root / "dynamic/archive/2026/01/01/00.json").exists())

    def test_apply_removes_old_snapshots_and_updates_manifest(self):
        root, index = self._sandbox()
        orig = prune.ROOT; prune.ROOT = root
        try:
            sys.argv = ["prune", "--days", "1", "--apply"]
            prune.main()
        finally:
            prune.ROOT = orig
        m = json.loads(index.read_text())
        self.assertEqual(m["schema"], "earth-now.archive.v1")
        # All 2026-01-01 snapshots are old (retention 1 day vs today) -> all dropped.
        self.assertEqual(len(m["snapshots"]), 0)
        self.assertFalse((root / "dynamic/archive/2026/01/01/00.json").exists())

    def test_refuses_unexpected_schema(self):
        root, index = self._sandbox()
        index.write_text(json.dumps({"schema": "other.v1", "snapshots": []}))
        orig = prune.ROOT; prune.ROOT = root
        try:
            sys.argv = ["prune", "--days", "1"]
            with self.assertRaises(SystemExit):
                prune.main()
        finally:
            prune.ROOT = orig

if __name__ == "__main__":
    unittest.main()
