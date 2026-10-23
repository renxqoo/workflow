import unittest

from shipping import shipping_fee


class ShippingTests(unittest.TestCase):
    def test_below_threshold_has_shipping_fee(self):
        self.assertEqual(shipping_fee(1000), 500)

    def test_above_threshold_has_no_shipping_fee(self):
        self.assertEqual(shipping_fee(6000), 0)

    def test_negative_subtotal_is_rejected(self):
        with self.assertRaises(ValueError):
            shipping_fee(-1)
