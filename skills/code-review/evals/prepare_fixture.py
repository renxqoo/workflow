from pathlib import Path
import argparse
import shutil
import subprocess


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def prepare(destination, mode):
    source = Path(__file__).resolve().parent
    if not destination.is_absolute() or destination.exists():
        raise ValueError("destination must be a new absolute directory")
    shutil.copytree(source / "fixtures/shipping", destination)
    git(destination, "init", "-q")
    git(destination, "config", "user.name", "Skill Evaluation")
    git(destination, "config", "user.email", "eval@example.invalid")
    git(destination, "config", "commit.gpgsign", "false")
    git(destination, "config", "core.hooksPath", "/dev/null")
    git(destination, "add", ".")
    git(destination, "commit", "-q", "-m", "Baseline fixture")
    if mode != "clean":
        target = destination / "shipping.py"
        original = target.read_text()
        assert original.count("subtotal_cents >= 5000") == 1
        target.write_text(original.replace("subtotal_cents >= 5000", "subtotal_cents > 5000", 1))
        if mode == "working":
            shutil.copyfile(source / "changes/checkout.py", destination / "checkout.py")
        elif mode == "staged":
            git(destination, "add", "shipping.py")
            target.write_text(original)
    print(destination)
    print(git(destination, "status", "--short") or "clean")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--mode", choices=("working", "staged", "clean"), required=True)
    arguments = parser.parse_args()
    prepare(arguments.destination, arguments.mode)
