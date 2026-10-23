def checkout_quote(subtotal_cents):
    if subtotal_cents < 0:
        raise ValueError("subtotal must be non-negative")
    fee_cents = 0 if subtotal_cents >= 5000 else 500
    return {
        "subtotal_cents": subtotal_cents,
        "shipping_fee_cents": fee_cents,
        "total_cents": subtotal_cents + fee_cents,
    }
