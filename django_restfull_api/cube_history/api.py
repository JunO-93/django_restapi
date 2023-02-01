from urllib.parse import urlencode, unquote, quote_plus
from urllib.request import urlopen, Request
from django.conf import settings

import io, os
import json
import requests
import pandas as pd

SECRET_KEY = getattr(settings, 'SECRET_KEY', None)

def apiCall(count : int , date : str, cursor = ''):
    #.env 파일에서 변수 가져오기
    # serviceKey = os.environ.get("SECRET_KEY")
    serviceKey = SECRET_KEY
    url = f'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results?count={count}&date={date}&cursor={cursor}'  
    headers = {
        'Content-Type': 'application/json',
        'charset': 'UTF-8',
        'Accept': '*/*',
        'authorization' : serviceKey,
    }
    
    try:
        response = requests.get(url, headers = headers)        
        contents = response.text
    except Exception as e:
        print(e)    
    return contents