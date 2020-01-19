CREATE TABLE financial_statement (
    ticker_code VARCHAR (5) NOT NULL,
    report_period DATE,
    currency VARCHAR,
    conversion_rate INTEGER,
    rounding VARCHAR,
    type_of_report VARCHAR,
    audit_opinion VARCHAR,
    auditor VARCHAR,
    created_at TIMESTAMP,
    UNIQUE(ticker_code, report_period)
);
