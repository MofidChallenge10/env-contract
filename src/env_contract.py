"""Compare environment variable references in source with .env templates."""
import argparse,json,re,sys
from pathlib import Path
PATTERNS=[re.compile(r"""(?:os\.)?getenv\(\s*['"]([A-Z][A-Z0-9_]*)['"]"""),re.compile(r"""os\.environ\[\s*['"]([A-Z][A-Z0-9_]*)['"]\s*\]"""),re.compile(r"""process\.env\.([A-Z][A-Z0-9_]*)""")]
def scan_sources(paths):
 found=set()
 for path in paths:
  try: text=Path(path).read_text(encoding="utf-8")
  except (OSError,UnicodeError): continue
  for pattern in PATTERNS: found.update(pattern.findall(text))
 return found
def parse_env(path):
 keys=set()
 for line in Path(path).read_text(encoding="utf-8").splitlines():
  line=line.strip()
  if not line or line.startswith("#"): continue
  m=re.match(r"^(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=",line)
  if m: keys.add(m.group(1))
 return keys
def audit(referenced,documented):
 return {"undocumented":sorted(referenced-documented),"unused":sorted(documented-referenced)}
def main(argv=None):
 p=argparse.ArgumentParser(description="Check source environment variable references against an env template.")
 p.add_argument("template"); p.add_argument("files",nargs="+"); a=p.parse_args(argv)
 result=audit(scan_sources(a.files),parse_env(a.template)); print(json.dumps(result,indent=2))
 return int(bool(result["undocumented"]))
if __name__=="__main__": sys.exit(main())
