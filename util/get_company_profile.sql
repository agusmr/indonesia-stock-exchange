CREATE TABLE company_profile (
    ticker_code VARCHAR (4) NOT NULL PRIMARY KEY UNIQUE,
    company_address VARCHAR,
    sector VARCHAR,
    subsector VARCHAR,
    listing_date DATE,
    website VARCHAR,
    count_secretary BIGINT,
    count_director BIGINT,
    count_commissioner BIGINT,
    count_audit_committee BIGINT,
    count_stakeholder BIGINT,
    count_subsidiary BIGINT,
    count_dividend BIGINT,
    created_at TIMESTAMP NOT NULL
);
