import argparse
from pathlib import Path
import shutil
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("--destination", required=True, type=Path)
arguments = parser.parse_args()
destination = arguments.destination.resolve()
if destination.exists():
    raise SystemExit("Destination must not already exist")
source = Path(__file__).resolve().parent / "fixtures" / "review"
shutil.copytree(source, destination)
commands = [
    ["git", "init", "-q"],
    ["git", "config", "user.name", "Skill evaluation"],
    ["git", "config", "user.email", "evaluation@example.invalid"],
    ["git", "add", "AGENTS.md", "calculator.py", "tests/test_calculator.py", ".gitignore"],
    ["git", "-c", "core.hooksPath=/dev/null", "commit", "-q", "-m", "fixture baseline"],
]
for command in commands:
    subprocess.run(command, cwd=destination, check=True)
calculator = destination / "calculator.py"
original = calculator.read_text()
if original.count("quantity >= 10") != 1:
    raise SystemExit("Expected exactly one discount boundary to change")
calculator.write_text(original.replace("quantity >= 10", "quantity > 10"))
print(destination)
