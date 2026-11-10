import unittest
from unittest.mock import Mock

from checkout import create_checkout, quote_credit_micro
from checkout_ui import payment_summary


class CheckoutTests(unittest.TestCase):
    def test_channel_rate_preserves_a_fractional_dollar_principal(self):
        self.assertEqual(quote_credit_micro(1251, 8000), 10008000)

    def test_both_principal_boundaries_are_valid(self):
        for cents, expected in [(100, 1000000), (1000000, 10000000000)]:
            with self.subTest(cents=cents):
                self.assertEqual(quote_credit_micro(cents), expected)

    def test_invalid_principal_never_reaches_payment(self):
        for cents in [99, 1000001, True, 1250.5, "1250"]:
            with self.subTest(cents=cents):
                charge = Mock()
                with self.assertRaises(ValueError):
                    create_checkout(cents, "account-a", "account-a", charge)
                charge.assert_not_called()

    def test_invalid_channel_rate_is_not_a_free_quote(self):
        for rate in [0, -1, True, 0.5, "8000"]:
            with self.subTest(rate=rate):
                with self.assertRaises(ValueError):
                    quote_credit_micro(1250, rate)

    def test_a_changed_or_absent_session_cannot_create_payment(self):
        for session in [None, "account-b"]:
            with self.subTest(session=session):
                charge = Mock()
                with self.assertRaises(PermissionError):
                    create_checkout(1250, "account-a", session, charge)
                charge.assert_not_called()

    def test_creation_sends_the_exact_principal_and_verified_owner_once(self):
        charge = Mock(return_value="checkout-7")
        result = create_checkout(1251, "account-a", "account-a", charge)
        self.assertEqual(result, "checkout-7")
        charge.assert_called_once_with(owner="account-a", amount_cents=1251)

    def test_a_payment_transport_failure_is_not_replayed(self):
        charge = Mock(side_effect=ConnectionError("unavailable"))
        with self.assertRaises(ConnectionError):
            create_checkout(1250, "account-a", "account-a", charge)
        charge.assert_called_once_with(owner="account-a", amount_cents=1250)

    def test_summary_keeps_the_channel_amounts_and_layout(self):
        summary = payment_summary(1250, 8000)
        self.assertEqual(summary["principal_cents"], 1250)
        self.assertEqual(summary["received_micro"], 10000000)
        self.assertEqual(summary["heading"], "Add credits")
        self.assertEqual(summary["class_name"], "rounded-xl")
        self.assertEqual(summary["dom_order"], ("heading", "amount", "pay"))
