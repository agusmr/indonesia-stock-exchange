import json
import psycopg2
import requests
from datetime import datetime, timedelta

CONNECTION = json.load(open('connection.json'))
PSQL_CONNECT = psycopg2.connect(
    host=CONNECTION['host'],
    port=CONNECTION['port'],
    database=CONNECTION['database'],
    user=CONNECTION['user'],
    password=CONNECTION['password']
)
CUR = PSQL_CONNECT.cursor()
URL = 'https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s'
    
def main():

    response = requests.get(URL)
    data = response.json()
    
    for d in data:
        try:
            CUR.execute(
                """
                INSERT INTO listed_company (
                    ticker_code, 
                    company_name,
                    created_at
                ) VALUES (%s, %s, %s)
                """, 
                (
                    d.get('KodeEmiten'),
                    d.get('NamaEmiten').upper(),
                    datetime.now() + timedelta(hours = 7)
                )
            )
            PSQL_CONNECT.commit()
        except psycopg2.errors.UniqueViolation:
            PSQL_CONNECT.rollback()
            pass
        
    CUR.close()
    PSQL_CONNECT.close()
        
if __name__ == "__main__":
    main()
