import json
import os
import pandas as pd
import requests
import sys
from datetime import datetime, timedelta
from sqlalchemy import create_engine, exc
from zipfile import BadZipFile

CONNECTION = json.load(open('connection.json'))
ENGINE = create_engine(f"postgresql://{CONNECTION['user']}:{CONNECTION['password']}@{CONNECTION['host']}:{CONNECTION['port']}/{CONNECTION['database']}")
YEAR = sys.argv[1]
QUARTER = sys.argv[2]
YEARLY = sys.argv[3]

class FinancialStatement:

    def __init__(self, ticker_code, year, quarter, yearly):
        """
        Get attributes in order to get URLs.

        Arguments:
            - ticker_code = Company ID in Indonesia Stock Exchange. 
            - year = user inputted four digit character. 
            - quarter = Q1, ..., Q3 should be put as TW1, ..., TW3, and Q4 should be Audit.
            - yearly = Q1, ..., Q3 should be put as I, ..., III, and Q4 should be Tahunan.
        """

        self.ticker_code = ticker_code
        self.year = year
        self.quarter = quarter
        self.yearly = yearly

    def get_url(self):

        url = f"http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%20{self.year}/{self.quarter}/{self.ticker_code}/FinancialStatement-{self.year}-{self.yearly}-{self.ticker_code}.xlsx"
        response = requests.get(url)
        if response.status_code == 200:
            os.system(f'wget {url}')

    def get_general_info(self):

        df = pd.read_excel(f'FinancialStatement-{self.year}-{self.yearly}-{self.ticker_code}.xlsx', sheet_name=1)
        df = df[['Unnamed: 2', 'Unnamed: 1']]
        df = df.transpose()
        df = df.rename(columns=df.iloc[0]).iloc[1:].reset_index(drop=True)
        df = df[[
            'Entity code',
            'Current period end date',
            'Description of presentation currency',
            'Conversion rate at reporting date if presentation currency is other than rupiah',
            'Level of rounding used in financial statements',
            'Type of report on financial statements',
            'Type of auditor\'s opinion',
            'Current year auditor'
        ]]
        df.columns = [
            'ticker_code',
            'report_period',
            'currency',
            'conversion_rate',
            'rounding',
            'type_of_report',
            'audit_opinion',
            'auditor'
        ]
        df['created_at'] = datetime.now() + timedelta(hours = 7)

        try:        
            return df.to_sql(
                'financial_statement', 
                con=ENGINE,
                if_exists='append',
                index=False
            )
        except exc.IntegrityError:
            pass

def get_financial_statement():

    listed_company = requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s').json()
    ticker_code = [listed_company[x]['KodeEmiten'] for x in range(len(listed_company))]
    financial_statement = [FinancialStatement(x, YEAR, QUARTER, YEARLY) for x in ticker_code]
    [x.get_url() for x in financial_statement]
    
    for i in range(len(financial_statement)):
        try:
            financial_statement[i].get_general_info()
        except FileNotFoundError:
            pass
        except BadZipFile:
            pass
    

if __name__ == '__main__':
    get_financial_statement()
    os.system('rm -r *.xlsx')
