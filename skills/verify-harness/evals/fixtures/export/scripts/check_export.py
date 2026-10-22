import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--evidence-dir", required=True, type=Path)
arguments = parser.parse_args()
root = Path(__file__).resolve().parent.parent
with tempfile.TemporaryDirectory(prefix="export-fixture-") as temporary:
    directory = Path(temporary)
    source = directory / "input.csv"
    output = directory / "output.json"
    source.write_text("amount\n0.10\n0.20\n")
    command = [sys.executable, str(root / "report.py"), "--input", str(source),
               "--output", str(output)]
    subprocess.run(command, cwd=root, check=True)
    observed = json.loads(output.read_text())
    if observed != {"rows": 2, "total": "0.30"}:
        raise SystemExit(f"Wrong exported result: {observed!r}")
arguments.evidence_dir.mkdir(parents=True, exist_ok=True)
evidence = {"scenario": "export-two-amounts", "observed": observed,
            "temporary_resources_removed": not directory.exists()}
(arguments.evidence_dir / "result.json").write_text(json.dumps(evidence, indent=2) + "\n")
print("export-two-amounts: passed; evidence=" + str(arguments.evidence_dir / "result.json"))
