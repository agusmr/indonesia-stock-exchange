import os
import requests
from datetime import datetime, timedelta

class CompanyAndPeriod:
    def __init__(self, ticker_code, year, quarter, yearly):
        self.ticker_code = ticker_code
        self.year = year
        self.quarter = quarter
        self.yearly = yearly

    def get_url(self):
        url = f"http://www.idx.co.id/Portals/0/StaticData/ListedCompanies/Corporate_Actions/New_Info_JSX/Jenis_Informasi/01_Laporan_Keuangan/02_Soft_Copy_Laporan_Keuangan//Laporan%20Keuangan%20Tahun%20{self.year}/{self.quarter}/{self.ticker_code}/FinancialStatement-{self.year}-{self.yearly}-{self.ticker_code}.xlsx"
        response = requests.get(url)
        if response.status_code == 200:
            os.system(f'wget {url}')

def main():
    listed_company = requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s').json()
    ticker_code = [listed_company[x]['KodeEmiten'] for x in range(len(listed_company))]
    for i in ticker_code:
        CompanyAndPeriod(i, 2018, 'Audit', 'Tahunan').get_url()

if __name__ == '__main__':
    os.chdir('tmp')
    main()
