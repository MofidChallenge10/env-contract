import sys,tempfile,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from env_contract import audit,parse_env
class Tests(unittest.TestCase):
 def test_diff(self): self.assertEqual({"undocumented":["B"],"unused":["C"]},audit({"A","B"},{"A","C"}))
 def test_parse(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/".env.example"; p.write_text("# comment\nexport API_KEY=\nPORT=3\n")
   self.assertEqual({"API_KEY","PORT"},parse_env(p))
if __name__=="__main__": unittest.main()
