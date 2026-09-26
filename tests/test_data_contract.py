import json, pathlib, unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
ALLOWED={"quake","wildfire","storm","volcano","iceberg","dust"}

class EarthNowDataContract(unittest.TestCase):
    def test_latest_snapshot_contract(self):
        p=json.loads((ROOT/"dynamic/latest.json").read_text())
        self.assertEqual(p.get("schema"),"earth-now.atlas.v1")
        self.assertTrue(p.get("generated_at"))
        self.assertIsInstance(p.get("events"),list)
        self.assertGreater(len(p["events"]),0)
        for e in p["events"]:
            self.assertIn(e.get("kind"),ALLOWED)
            self.assertIsInstance(e.get("lat"),(int,float))
            self.assertIsInstance(e.get("lng"),(int,float))
            self.assertGreaterEqual(e["lat"],-90); self.assertLessEqual(e["lat"],90)
            self.assertGreaterEqual(e["lng"],-180); self.assertLessEqual(e["lng"],180)
            self.assertEqual(e.get("semantic"),"observed")
            self.assertTrue(e.get("title"))
            self.assertIsInstance(e.get("source"),dict)
            self.assertTrue(e["source"].get("name"))
            self.assertTrue(e.get("time") is None or isinstance(e.get("time"),(int,float)))

    def test_archive_manifest_contract(self):
        m=json.loads((ROOT/"dynamic/archive/index.json").read_text())
        self.assertEqual(m.get("schema"),"earth-now.archive.v1")
        self.assertIsInstance(m.get("snapshots"),list)
        self.assertLessEqual(len(m["snapshots"]),8760)
        for s in m["snapshots"]:
            self.assertTrue(s.get("at")); self.assertTrue(s.get("path"))
            self.assertTrue(s["path"].startswith("dynamic/archive/"))
            self.assertTrue((ROOT/s["path"]).exists())
            self.assertGreaterEqual(s.get("events",0),0)

if __name__=="__main__": unittest.main()
