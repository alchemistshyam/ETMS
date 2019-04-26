import requests
import sys
import datetime
import os
sys.path.append(os.path.abspath('..\\'))
from   drivers.http_connection import HTTP_Connection
class TestScan:
    def test_scan_process():
        print(HTTP_Connection.get_http_connection("http://127.0.0.1:5000/scan/process" , "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.e30.EqHv-Xtqoa8iF4jLbuLQ8xUEzQiuiZNvtEyyR1kEglo"))

TestScan.test_scan_process()