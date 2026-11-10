from checkout import quote_credit_micro


def payment_summary(amount_cents, micro_per_cent=10000):
    return {
        "principal_cents": amount_cents,
        "received_micro": quote_credit_micro(amount_cents, micro_per_cent),
        "heading": "Add credits",
        "class_name": "rounded-xl",
        "dom_order": ("heading", "amount", "pay"),
    }


def copy_feedback(success):
    if success:
        return "Copied"
    return "Copy failed"


def payment_button(loading):
    if loading:
        return {"disabled": True, "label": "Loading", "icon": "spinner"}
    return {"disabled": False, "label": "Pay", "icon": "arrow"}
