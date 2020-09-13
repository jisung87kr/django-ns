import requests
import json
from pprint import pprint
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
from bs4 import BeautifulSoup

class NsParser:
    def __init__(self, page, size):
        self.page = page
        self.size = size
        self.list_url = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=&pagingIndex={}&pagingSize={}&productSet=total&query={}&sort=rel&timestamp=&viewType=list'

    def search_url(self, query, itemurl):
        # 네이버쇼핑 인경우와 스마트스토어, 쇼핑윈도 주소를 판단해서 처리 해야함
        # 네이버 쇼핑 https://search.shopping.naver.com/detail/detail.nhn?nvMid=23097538491&query=%EB%9D%BC%EB%A9%B4&NaPm=ct%3Dkezqyq5k%7Cci%3De5b7036e680a8fbec42fbb08f8106e47ceb3fc27%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dba715fbdd58ada996e1d98d0946fb3f5aa1f14d2
        # 스마트스토어 https://smartstore.naver.com/onetopflower/products/4603061842?NaPm=ct%3Dkezr09pk%7Cci%3D30da657f1c0fa89dc44fa26b8876e688e0baff39%7Ctr%3Dslsl%7Csn%3D990525%7Chk%3D007980dcbf5871a513e39e1ef213ba9ad5b1c5ed
        # 쇼핑윈도 https://shopping.naver.com/style/fashionbrand/stores/100157598/products/5060091345?NaPm=ci%3Dshoppingwindow%7Cct%3Ddummy%7Ctr%3Dswl%7Chk%3D25e04798b8e922a82cdde8ee2d70da3d5d487608%7Ctrx%3Di%3A5060091345
        pprint(itemurl)
        parts = urlparse(itemurl)
        qs = dict(parse_qsl(parts.query))
        if 'search.shopping.naver.com' in parts.netloc:
            # query = qs['query']
            itemid = qs['nvMid']
            result = self.parse_list(query)
            result['find_target'] = { 'id' : itemid }
        else:
            path = parts.path.split('/')
            result = self.parse_list(query)
            result['find_target'] = { 'mallProductId' : path[-1] }
        return result

    def search_store(self, query, store):
        result = self.parse_list(query)
        result['find_target'] = { 'mallname' : store }
        return result

    def parse_list(self, query):
        url = self.list_url.format(self.page, self.size, query)
        json_data = self.get_items_to_json(url)
        return json_data

    def get_items_to_json(self, url):
        r = requests.get(url, timeout=100)
        soup = BeautifulSoup(r.content, 'html.parser')
        script = soup.find('script', { 'id': '__NEXT_DATA__' })
        json_data = json.loads(script.contents[0])
        return json_data
    
    def find_rank(self, result, target):
        return result

