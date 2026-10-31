def invoice_total(unit_price_cents, quantity):
    subtotal = unit_price_cents * quantity
    if quantity > 10:
        return subtotal * 90 // 100
    return subtotal
