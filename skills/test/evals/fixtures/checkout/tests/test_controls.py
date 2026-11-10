import unittest

from checkout_ui import copy_feedback, payment_button, payment_summary


class ControlsTests(unittest.TestCase):
    def test_summary_heading(self):
        self.assertEqual(payment_summary(1250)["heading"], "Add credits")

    def test_summary_corner_style(self):
        self.assertEqual(payment_summary(1250)["class_name"], "rounded-xl")

    def test_summary_dom_order(self):
        self.assertEqual(payment_summary(1250)["dom_order"], ("heading", "amount", "pay"))

    def test_clipboard_feedback(self):
        self.assertEqual(copy_feedback(True), "Copied")
        self.assertEqual(copy_feedback(False), "Copy failed")

    def test_loading_button_projection(self):
        self.assertEqual(payment_button(True), {
            "disabled": True, "label": "Loading", "icon": "spinner",
        })
        self.assertEqual(payment_button(False), {
            "disabled": False, "label": "Pay", "icon": "arrow",
        })
