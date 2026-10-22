import unittest
from calculator import invoice_total


class InvoiceTests(unittest.TestCase):
    def test_small_order_keeps_full_price(self):
        self.assertEqual(invoice_total(100, 1), 100)

    def test_large_order_receives_discount(self):
        self.assertEqual(invoice_total(100, 11), 990)
