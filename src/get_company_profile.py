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
LISTED_COMPANY = requests.get('https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s').json()
    
def main():

    data = []
    for ticker in LISTED_COMPANY:
        url = f'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfilesDetail?emitenType=&kodeEmiten={ticker.get("KodeEmiten")}&language=id-id'
        response = requests.get(url)
        data.append(response.json())

    for d in data:
        try:
            CUR.execute(
                """
                INSERT INTO company_profile (
                    ticker_code,
                    company_address,
                    sector,
                    subsector,
                    listing_date,
                    website,
                    count_secretary,
                    count_director,
                    count_commissioner,
                    count_audit_committee,
                    count_stakeholder,
                    count_subsidiary,
                    count_dividend,
                    created_at
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s
                )
                """,
                (
                    d.get('Search').get('KodeEmiten'),
                    d.get('Profiles')[0].get('Alamat').upper(),
                    d.get('Profiles')[0].get('Sektor').upper(),
                    d.get('Profiles')[0].get('SubSektor').upper(),
                    datetime.strptime(d.get('Profiles')[0].get('TanggalPencatatan')[:10], '%Y-%m-%d').date(),
                    d.get('Profiles')[0].get('Website').lower(),
                    len(d.get('Sekretaris')),
                    len(d.get('Direktur')),
                    len(d.get('Komisaris')),
                    len(d.get('KomiteAudit')),
                    len(d.get('PemegangSaham')),
                    len(d.get('AnakPerusahaan')),
                    len(d.get('Dividen')),
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
