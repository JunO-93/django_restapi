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

# Create your views here.
# class DataViewSet(viewsets.ModelViewSet):
#     queryset = data.objects.all()
#     serializer_class = DataSerializer

# 로깅세팅
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def valueInputSet(request):
    return render(request, 'html/valueInput.html') 

def selectCubeData(request):
    
    if request.method =='POST': 
   
        try:
            count = request.POST['count']
            date = request.POST['date']                        

            cubeHis = apiCall(count, date)
    
        except Exception as e:            
            logger.debug(e)      
        
    return HttpResponse(cubeHis)