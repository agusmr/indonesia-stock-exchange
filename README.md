# indonesia-stock-exchange

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free (one of the things you could do especiallly when you're not rich AF) :stuck_out_tongue_closed_eyes:. It includes both technical and fundamental information, such as stock prices (opening, closing, bid, ask, volume, etc) and financial statements (balance sheet, profit and loss, changes in equity, cash flow). Surely the information contained is more diverse than we can find from other free source (e.g. Yahoo! Finance) and far cheaper than using financial terminal (e.g. Bloomberg). I hope this can be useful for your own purpose. :smile:

## Robots.txt

Open `https://idx.co.id/robots.txt`:

```
Server Error

404 - File or directory not found.
The resource you are looking for might have been removed, had its name changed, or is temporarily unavailable.
```

## Clone

```
cd ~
git clone https://github.com/ledwindra/indonesia-stock-exchange.git
cd indonesia-stock-exchange/
```

## Use Virtual Environment and install requirements

Run the following on terminal:

```
python3 -m venv [VIRTUAL-ENVIRONMENT-NAME]
source [VIRTUAL-ENVIRONMENT-NAME]/bin/activate
python3 -m pip install -r requirements.txt
```

To exit, run `deactivate`.

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

Run the following on terminal:

```
pytest test/
```

## Heroku

Add ons:

1. Heroku Postgres ([link](https://elements.heroku.com/addons/heroku-postgresql))
2. Heroku Scheduler ([link](https://elements.heroku.com/addons/scheduler))

## Install Heroku

See [here](https://devcenter.heroku.com/articles/heroku-cli)

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
python3 src/get_financial_statement.py [ARGV 1] [ARGV 2] [ARGV 3]
```

## End
Hope you enjoy this. Thanks for reading! :smile:
