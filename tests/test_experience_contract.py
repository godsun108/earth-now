import pathlib, unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]

class EarthNowExperienceContract(unittest.TestCase):
    def test_planet_first_surface(self):
        html=(ROOT/"index.html").read_text()
        self.assertIn('id="random"',html)
        self.assertIn('TAKE ME SOMEWHERE',html)
        self.assertIn('id="instruments"',html)
        self.assertIn('hidden aria-label="Earth instruments"',html)

    def test_truth_and_eyes_survive_redesign(self):
        app=(ROOT/"app.js").read_text()
        self.assertIn("IF IT GLOWS", (ROOT/"index.html").read_text())
        self.assertIn("OPEN EYES",app)
        self.assertIn("earth-now:open-eyes",app)
        self.assertIn("VISUALIZATION ANCHOR",app)

    def test_instruments_are_on_demand(self):
        app=(ROOT/"app.js").read_text()
        self.assertIn("function setInstruments",app)
        self.assertIn("instruments.hidden",app)

if __name__=="__main__": unittest.main()
