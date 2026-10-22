import unittest
from report import summarize


class SummaryTests(unittest.TestCase):
    def test_decimal_amounts_preserve_cents(self):
        self.assertEqual(summarize([{"amount": "0.10"}, {"amount": "0.20"}]),
                         {"rows": 2, "total": "0.30"})

    def test_empty_export_has_zero_total(self):
        self.assertEqual(summarize([]), {"rows": 0, "total": "0.00"})
