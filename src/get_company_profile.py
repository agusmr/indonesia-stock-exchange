import json
import logging
import multiprocessing
import os
import requests
import string
import sys
import time
from datetime import datetime

class GetCompanyProfile():

    def __init__(self):
        
        self.data = os.getcwd() + '/output/get-companies.json'
        self.url = 'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfilesDetail?emitenType=&kodeEmiten={}&language=id-id'
        self.path = os.getcwd() + '/output/company-profile/'
        self.retry = int(sys.argv[1])
        self.timeout = int(sys.argv[2])
        self.interval = int(sys.argv[3])

    def get_ticker(self):
        
        with open(self.data, 'r') as f:
            data = json.load(f)
            
        ticker = [x.get('KodeEmiten') for x in data]
        ticker = [self.url.format(x) for x in ticker]

        return ticker
    
    def main(self, ticker):

        file_name =  ticker.translate(str.maketrans('', '', string.punctuation))

        i = 0
        while i < self.retry:
            try:
                r = requests.get(ticker).json()
                with open(self.path + '{}.json'.format(file_name), 'w') as f:
                    json.dump(r, f)
            except Exception as e:
                logging.error(e)
                time.sleep(self.interval)
                i += 1

if __name__ == "__main__":
    logging.basicConfig(
        format = '%(asctime)s: %(message)s', 
        filename = os.getcwd() + '/logs/get-company-profile-{}.log'.format(datetime.now().strftime('%Y%m%d%H%M%S')), 
        level = logging.DEBUG
    )
    profile = GetCompanyProfile()
    multiprocessing.Pool(5).map(profile.main, profile.get_ticker())