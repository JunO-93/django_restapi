import logging

from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen, Request

from django.shortcuts import render, HttpResponse, redirect
from rest_framework import viewsets
from cube_history.serializers import DataSerializer
from cube_history.models import data
from cube_history.api import apiCall
from django.views import generic

import json
import pandas as pd

serviceKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiMjAwMDA6MTAiLCJhY2NvdW50X2lkIjoiNDg2NjQ0ODIzIiwiYXV0aF9pZCI6IjQiLCJleHAiOjE3MzY4MTM0MTYsImlhdCI6MTY3Mzc0MTQxNiwibmJmIjoxNjczNzQxNDE2LCJzZXJ2aWNlX2lkIjoiNDMwMDExMzk3IiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIn0.FN0ZQrkhRJ7TpSU04AIo5dpvQwoQZvsu2mVjK25lrtw'
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')

# Create your views here.
# class DataViewSet(viewsets.ModelViewSet):
#     queryset = data.objects.all()
#     serializer_class = DataSerializer

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def valueInputSet(request):
    return render(request, 'html/valueInput.html') 


def selectCubeData(request):
    
    if request.method =='POST':
   
        try:
            count = request.POST['count']
            date = request.POST['date']            
            print(f'count : {count}, date : {date}')
        except Exception as e:            
            logger.debug(e)      
        
    return HttpResponse(f'count : {count}, date : {date}')

#     template_name = 'html/contact.html'

#     def post(self , request):
#         inputkw = request.POST.get('name')
#         result = apiCall.kewordFindAPI(inputkw)
#         context = {
#             'result' : result             
#         }
#         return render (request, self.template_name, context)