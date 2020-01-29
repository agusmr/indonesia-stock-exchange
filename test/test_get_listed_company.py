import json
import psycopg2
import requests
from datetime import datetime, timedelta

CONNECTION = json.load(open('.connection.json'))
PSQL_CONNECT = psycopg2.connect(
    host=CONNECTION['host'],
    port=CONNECTION['port'],
    database=CONNECTION['database'],
    user=CONNECTION['user'],
    password=CONNECTION['password']
)

class TestListedCompany:
    def test_connection(self):
        assert PSQL_CONNECT.closed == 0
        PSQL_CONNECT.close()