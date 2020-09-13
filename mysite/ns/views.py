from pprint import pprint
from django.shortcuts import render
from django.http import HttpResponse
from .includes.ns import NsParser
from .lib.naversearchad.searchad import SearchAd

# Create your views here.
def index(request):
    return render(request, 'ns/index.html')

def searchRank(request):
    ns = NsParser(1, 40)
    if request.GET['store']:
        result = ns.search_store(request.GET['item'], request.GET['store'])
    else :
        result = ns.search_url(request.GET['query'], request.GET['itemurl'])

    context = {'result' : result }
        
    return render(request, 'ns/search-rank.html', context)

def searchKeyword(request):
    if 'keyword' in request.GET:
        searchAd = SearchAd()
        result = searchAd.rel_keyword(request.GET['keyword'])
        context = {'result' : result }
    else: 
        context = {'result' : 'null' }
    return render(request, 'ns/search-keyword.html', context)

# def searchKeywordResult(request):
#     searchAd = SearchAd()
#     result = searchAd.rel_keyword(request.GET['keyword'])
#     context = {'result' : result }
#     return render(request, 'ns/search-keyword-result.html', context)