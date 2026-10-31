from pathlib import Path
import subprocess
import sys
import unittest

from calculator import invoice_total


class InvoiceTests(unittest.TestCase):
    def test_one_item(self):
        self.assertEqual(invoice_total(100, 1), 100)

    def test_eleven_items(self):
        self.assertEqual(invoice_total(100, 11), 990)

    def test_text_output(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, "-B", str(root / "main.py"), "100", "1"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout, "total=100\n")


if __name__ == "__main__":
    unittest.main()
