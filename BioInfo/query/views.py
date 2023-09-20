from elasticsearch_dsl import Search
from .documents import MyDocument
from django.shortcuts import render
from django.conf import settings



def welcome(request):

    return render(request,"search_results.html")




