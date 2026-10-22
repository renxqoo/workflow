def invoice_total(unit_cents, quantity):
    subtotal = unit_cents * quantity
    if quantity > 10:
        return subtotal * 9 // 10
    return subtotal
