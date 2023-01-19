from django.shortcuts import render
from rest_framework import viewsets
from cube_history.serializers import DataSerializer
from cube_history.models import data
from cube_history.api import apiCall

# Create your views here.
class DataViewSet(viewsets.ModelViewSet):
    queryset = data.objects.all()
    serializer_class = DataSerializer

class apiViewSet(viewsets.ModelViewSet):
    #비즈니스 로직이나 이게 들어감 
    queryset = data.objects.all()
    serializer_class = DataSerializer
    tmp = apiCall(10, '2023-01-15')

    print(tmp)