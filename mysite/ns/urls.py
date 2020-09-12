from django.urls import path
from . import views

app_name = 'ns'
urlpatterns = [
    path('', views.index, name='index'),
    path('search-rank/', views.searchRank, name='search_rank'),
    path('search-keyword/', views.searchKeyword, name='search_keyword'),
    # path('search-keyword/result', views.searchKeywordResult, name='search_keyword_result'),
]