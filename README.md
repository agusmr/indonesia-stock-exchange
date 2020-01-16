# indonesia-stock-exchange

## Intro

This repository aims to get the financial data of publicly listed companies in Indonesia for free (one of the things you could do especiallly when you're not rich AF) :stuck_out_tongue_closed_eyes:. It includes both technical and fundamental information, such as stock prices (opening, closing, bid, ask, volume, etc) and financial statements (balance sheet, profit and loss, changes in equity, cash flow). Surely the information contained is more diverse than we can find from other free source (e.g. Yahoo! Finance) and far cheaper than using financial terminal (e.g. Bloomberg). 

I have only tested this using Python 3.7.3 (:snake:), but it should be fine for any Python 3.x. However, I won't bother testing it using Python 2.x. You can read [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for more details. Or you can visit [my Medium](https://medium.com/@lukmanedwindra/get-financial-information-from-indonesian-publicly-listed-companies-for-free-74870235f783) article related to this repository. I hope this can be useful for your own purpose. :smile:

## Clone

```
cd ~
git clone https://github.com/ledwindra/indonesia-stock-exchange.git
```

## Install requirements

```
python3 -m pip install -r requirements
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
```

## End
Hope you enjoy this. Once again, see [wiki](https://github.com/ledwindra/indonesia-stock-exchange/wiki/How-to-Get-Financial-Data-when-You-are-not-Rich-AF) for details. Thanks for reading! :smile:
