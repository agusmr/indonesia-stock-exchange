import json
import logging
import os
import requests
import sys
import time
from datetime import datetime

class GetEmiten():

    def __init__(self):
        self.path = os.getcwd() + '/output/'
        self.base_url = 'https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s'
        self.retry = int(sys.argv[1])
        self.t = int(sys.argv[2])
        self.interval = int(sys.argv[3])
    
    def main(self):
        "Returns publicly listed companies in Indonesia Stock Exchange."
        i = 0
        while i < self.retry:
            try:
                response = requests.get(self.base_url, timeout = self.t).json()
                with open(self.path + 'get-companies.json', 'w') as f:
                    json.dump(response, f)
                i = self.retry
            except Exception as e:
                logging.error(e)
                time.sleep(self.interval)
                i += 1
        
if __name__ == "__main__":
    logging.basicConfig(
        format = '%(asctime)s: %(message)s', 
        filename = os.getcwd() + '/logs/get-emiten-{}.log'.format(datetime.now().strftime('%Y%m%d%H%M%S')), 
        level = logging.DEBUG
    )
    GetEmiten().main()