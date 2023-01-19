from urllib.parse import urlencode, unquote, quote_plus
import requests
from bs4 import BeautifulSoup
import io
import pandas as pd

serviceKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJYLUFwcC1SYXRlLUxpbWl0IjoiMjAwMDA6MTAiLCJhY2NvdW50X2lkIjoiNDg2NjQ0ODIzIiwiYXV0aF9pZCI6IjQiLCJleHAiOjE3MzY4MTM0MTYsImlhdCI6MTY3Mzc0MTQxNiwibmJmIjoxNjczNzQxNDE2LCJzZXJ2aWNlX2lkIjoiNDMwMDExMzk3IiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIn0.FN0ZQrkhRJ7TpSU04AIo5dpvQwoQZvsu2mVjK25lrtw'
serviceKeyDecoded = unquote(serviceKey, 'UTF-8')


def apiCall(count : int , date : str, cursor = ''):
    # api query param 
    url = 'https://public.api.nexon.com/openapi/maplestory/v1/cube-use-results'
    returntype = 'json'
    # count = '10'
    # date = '2022-01-15'
    # cursor = ''

    queryParams = '?' + urlencode({quote_plus('ServiceKey') : serviceKeyDecoded, quote_plus('returnType') : returntype ,
    quote_plus('count') : count , quote_plus('date') : date , quote_plus('cursor') : cursor})
    
    res = requests.get(url + queryParams).content

    rawData = pd.read_csv(io.StringIO(res.decode('utf-8')))

    return rawData
