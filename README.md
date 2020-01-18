# indonesia-stock-exchange

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free (one of the things you could do especiallly when you're not rich AF) :stuck_out_tongue_closed_eyes:. It includes both technical and fundamental information, such as stock prices (opening, closing, bid, ask, volume, etc) and financial statements (balance sheet, profit and loss, changes in equity, cash flow). Surely the information contained is more diverse than we can find from other free source (e.g. Yahoo! Finance) and far cheaper than using financial terminal (e.g. Bloomberg). I hope this can be useful for your own purpose. :smile:

## Folder structure

```
.
├── LICENSE.md
├── Procfile
├── README.md
├── connection.json
├── get_financial_statement.ipynb
├── requirements.txt
├── run_test.sh
├── src
│   ├── get_company_profile.py
│   ├── get_financial_statement.py
│   ├── get_listed_company.py
│   └── get_trade_summary.py
├── test
│   ├── test_get_company_profile.py
│   ├── test_get_financial_statement.py
│   ├── test_get_listed_company.py
│   └── test_get_trade_summary.py
└── util
    ├── get_company_profile.sql
    ├── get_financial_statement.sql
    ├── get_listed_company.sql
    └── get_trade_summary.sql
```

## Clone

```
cd ~
git clone https://github.com/ledwindra/indonesia-stock-exchange.git
cd indonesia-stock-exchange/
```

## Install requirements

```
python3 -m pip install -r requirements.txt
```

## Install PostgreSQL

Mac

```
brew install postgresql
```

Ubuntu

```
sudo apt-get install postgresql
```

## Test

Test before deploying to production.

```
sh run_test.sh
```

## Heroku

Add ons:

1. Heroku Postgres ([link](https://elements.heroku.com/addons/heroku-postgresql))
2. Heroku Scheduler ([link](https://elements.heroku.com/addons/scheduler))

## Install Heroku

Mac

```
brew tap heroku/brew && brew install heroku
```

## Connect to Heroku

```
heroku login
heroku create
git add .
git commit -m "Deploy to Heroku"
git push heroku master
```

## Scheduler

```
python3 src/get_listed_company.py
python3 src/get_company_profile.py
python3 src/get_trade_summary.py
python3 src/get_financial_statement.py 2019 Audit Tahunan
```

## End
Hope you enjoy this. Thanks for reading! :smile:
