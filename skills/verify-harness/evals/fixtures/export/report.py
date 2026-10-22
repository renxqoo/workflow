import argparse
import csv
from decimal import Decimal
import json
from pathlib import Path


def summarize(rows):
    amounts = [Decimal(row["amount"]) for row in rows]
    return {"rows": len(amounts), "total": format(sum(amounts, Decimal("0")), ".2f")}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    with arguments.input.open(newline="") as handle:
        result = summarize(csv.DictReader(handle))
    arguments.output.write_text(json.dumps(result) + "\n")


if __name__ == "__main__":
    main()
