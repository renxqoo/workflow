def quote_credit_micro(amount_cents, micro_per_cent=10000):
    if type(amount_cents) is not int or not 100 <= amount_cents <= 1000000:
        raise ValueError("invalid principal")
    if type(micro_per_cent) is not int or micro_per_cent <= 0:
        raise ValueError("invalid channel rate")
    return amount_cents * micro_per_cent


def create_checkout(amount_cents, requested_owner, session_owner, charge):
    if not session_owner or requested_owner != session_owner:
        raise PermissionError("account changed")
    quote_credit_micro(amount_cents)
    return charge(owner=session_owner, amount_cents=amount_cents)
