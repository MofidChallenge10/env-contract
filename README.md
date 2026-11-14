# Env Contract

Keep environment configuration documentation aligned with what the code actually reads.

```bash
python -m pip install .
env-contract .env.example src/*.py
```

Reports referenced-but-undocumented and documented-but-unused keys. Current static extraction recognizes common Python `os.getenv`, `os.environ[]`, and JavaScript `process.env.NAME` forms; dynamic lookups and arbitrary languages are outside its scope. Values are never read from the template beyond key names.

## Tests
```bash
python -m unittest discover -s tests -v
```

MIT.
