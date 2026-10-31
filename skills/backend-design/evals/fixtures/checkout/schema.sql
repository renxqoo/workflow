CREATE TABLE orders (
    id TEXT PRIMARY KEY,
    tenant_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    request_key TEXT NOT NULL,
    amount_minor BIGINT NOT NULL,
    currency TEXT NOT NULL,
    state TEXT NOT NULL,
    payment_id TEXT,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE payment_events (
    id TEXT PRIMARY KEY,
    order_id TEXT NOT NULL,
    provider_event_id TEXT NOT NULL,
    observed_status TEXT NOT NULL,
    received_at TIMESTAMP NOT NULL
);
