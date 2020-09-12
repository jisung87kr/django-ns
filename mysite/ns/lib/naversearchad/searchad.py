import time
import random
import requests
from .signaturehelper import Signature
from .apikey import *

class SearchAd:
    def __init__(self):
        self.BASE_URL = 'https://api.naver.com'
        self.API_KEY = access_key
        self.SECRET_KEY = secret_key
        self.CUSTOMER_ID = customer_id

    def get_header(self, method, uri, api_key, secret_key, customer_id):
        timestamp = str(round(time.time() * 1000))
        signature = Signature.generate(timestamp, method, uri, self.SECRET_KEY)
        return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': self.API_KEY, 'X-Customer': str(self.CUSTOMER_ID), 'X-Signature': signature}

    def get_data(self, uri, method, param):
        r = requests.get(
            self.BASE_URL + uri,
            param,
            headers=self.get_header(method, uri, self.API_KEY, self.SECRET_KEY, self.CUSTOMER_ID))
        return r.json()
        # print("response status_code = {}".format(r.status_code))
        # print(r.json())
        # print("response body = {}".fBormat(r.json()))

    def rel_keyword(self, keyword):
        uri = '/keywordstool'
        method = 'GET'
        param = {
            # 'siteId' : ,
            # 'biztpId' : ,
            'hintKeywords' : keyword,
            # 'event' : ,
            # 'month' : 9,
            'showDetail' : 1
        }

        return self.get_data(uri, method, param)

# api = SearchAd()
# api.rel_keyword('화환')


