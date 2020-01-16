CREATE TABLE listed_company (
    ticker_code VARCHAR (4) NOT NULL PRIMARY KEY UNIQUE,
    company_name VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL
);
