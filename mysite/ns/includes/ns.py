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

    def search_url(self, itemurl):
        pprint(itemurl)
        parts = urlparse(itemurl)
        qs = dict(parse_qsl(parts.query))
        query = qs['query']
        itemid = qs['nvMid']
        result = self.parse_list(query)
        result['itemid'] = itemid
        return result

    def search_store(self, query, store):
        result = self.parse_list(query)
        result['store_name'] = store
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

