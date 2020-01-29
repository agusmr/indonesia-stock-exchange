import json
import psycopg2
import requests

CONNECTION = json.load(open('.connection.json'))
PSQL_CONNECT = psycopg2.connect(
    host=CONNECTION['host'],
    port=CONNECTION['port'],
    database=CONNECTION['database'],
    user=CONNECTION['user'],
    password=CONNECTION['password']
)
CUR = PSQL_CONNECT.cursor()

class TestListedCompany:

    def test_psql_connection(self):
        assert PSQL_CONNECT.closed == 0

    def test_cur_connection(self):
        assert CUR.closed == False
    
    def test_column_name(self):
        CUR.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'listed_company'")
        column_name = [x[0] for x in CUR.fetchall()]
        assert [x for x in column_name] == ['ticker_code', 'company_name', 'created_at']

    def test_column_type(self):
        CUR.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'listed_company'")
        column_name = [x[1] for x in CUR.fetchall()]
        assert [x for x in column_name] == ['character varying', 'character varying', 'timestamp without time zone']

    def test_count(self):
        url = 'https://www.idx.co.id/umbraco/Surface/Helper/GetEmiten?emitenType=s'
        response = requests.get(url)
        data = response.json()
        CUR.execute("SELECT COUNT(*) FROM listed_company")
        count = CUR.fetchone()[0]
        assert count == len(data)

    
    def test_psql_connection(self):
        PSQL_CONNECT.close()
        assert PSQL_CONNECT.closed == 1

    def test_cur_connection(self):
        CUR.close()
        assert CUR.closed == True

