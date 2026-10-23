def shipping_fee(subtotal_cents):
    if subtotal_cents < 0:
        raise ValueError("subtotal must be non-negative")
    if subtotal_cents >= 5000:
        return 0
    return 500
