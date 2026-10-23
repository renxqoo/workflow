DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100
SCHEMA_VERSION = "records/1"
SPINNER_TICK_MS = 80


def page_records(records, page=1, size=DEFAULT_PAGE_SIZE):
    if page < 1:
        raise ValueError("page must be positive")
    if size < 1 or size > MAX_PAGE_SIZE:
        raise ValueError("size out of range")
    start = (page - 1) * size
    return list(records[start:start + size])


def page_response(records, page=1, size=DEFAULT_PAGE_SIZE):
    return {
        "schema": SCHEMA_VERSION,
        "records": page_records(records, page=page, size=size),
    }
