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

# 로깅세팅
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# log 출력
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def valueInputSet(request):
    return render(request, 'html/valueInput.html') 

def selectCubeData(request):    
    if request.method =='POST': 
   
        try:
            count = request.POST['count']
            date = request.POST['date']
            
            cubeHis = apiCall(count, date)

            #json_cubeHis
            json_cubeHis = json.loads(cubeHis)

            #데이터 파싱            
            json_cube_histories = json_cubeHis['cube_histories']

            for i in range(len(json_cube_histories)):                
                id = json_cube_histories[i]['id']
                character_name = json_cube_histories[i]['character_name']
                create_date = json_cube_histories[i]['create_date']
                cube_type = json_cube_histories[i]['cube_type']
                item_upgrade_result = json_cube_histories[i]['item_upgrade_result']
                miracle_time_flag = json_cube_histories[i]['miracle_time_flag']
                item_equip_part = json_cube_histories[i]['item_equip_part']
                item_level =  json_cube_histories[i]['item_level']
                target_item = json_cube_histories[i]['target_item']
                potential_option_grade = json_cube_histories[i]['potential_option_grade']
                additional_potential_option_grade = json_cube_histories[i]['additional_potential_option_grade']
                if len(json_cube_histories[i]['before_potential_options']) > 0:
                    before_potential_options_grade_1 = json_cube_histories[i]['before_potential_options'][0]['grade']
                    before_potential_options_value_1 = json_cube_histories[i]['before_potential_options'][0]['value']
                    before_potential_options_grade_2 = json_cube_histories[i]['before_potential_options'][1]['grade']
                    before_potential_options_value_2 = json_cube_histories[i]['before_potential_options'][1]['value']
                    before_potential_options_grade_3 = json_cube_histories[i]['before_potential_options'][2]['grade']
                    before_potential_options_value_3 = json_cube_histories[i]['before_potential_options'][2]['value']
                    before_additional_potential_options_grade_1 = None               
                    before_additional_potential_options_value_1 = None
                    before_additional_potential_options_grade_2 = None
                    before_additional_potential_options_value_2 = None
                    before_additional_potential_options_grade_3 = None
                    before_additional_potential_options_value_3 = None

                if len(json_cube_histories[i]['before_additional_potential_options']) > 0 :
                    before_additional_potential_options_grade_1 = json_cube_histories[i]['before_additional_potential_options'][0]['grade']
                    before_additional_potential_options_value_1 = json_cube_histories[i]['before_additional_potential_options'][0]['value']
                    before_additional_potential_options_grade_2 = json_cube_histories[i]['before_additional_potential_options'][1]['grade']
                    before_additional_potential_options_value_2 = json_cube_histories[i]['before_additional_potential_options'][1]['value']
                    before_additional_potential_options_grade_3 = json_cube_histories[i]['before_additional_potential_options'][2]['grade']
                    before_additional_potential_options_value_3 = json_cube_histories[i]['before_additional_potential_options'][2]['value']
                    before_potential_options_grade_1 = None
                    before_potential_options_value_1 = None
                    before_potential_options_grade_2 = None
                    before_potential_options_value_2 = None
                    before_potential_options_grade_3 = None
                    before_potential_options_value_3 = None

                if len(json_cube_histories[i]['after_potential_options']) > 0 :
                    after_potential_options_grade_1 = json_cube_histories[i]['after_potential_options'][0]['grade']
                    after_potential_options_value_1 = json_cube_histories[i]['after_potential_options'][0]['value']
                    after_potential_options_grade_2 = json_cube_histories[i]['after_potential_options'][1]['grade']
                    after_potential_options_value_2 = json_cube_histories[i]['after_potential_options'][1]['value']
                    after_potential_options_grade_3 = json_cube_histories[i]['after_potential_options'][2]['grade']
                    after_potential_options_value_3 = json_cube_histories[i]['after_potential_options'][2]['value']
                    after_additional_potential_options_grade_1 = None
                    after_additional_potential_options_value_1 = None
                    after_additional_potential_options_grade_2 = None
                    after_additional_potential_options_value_2 = None
                    after_additional_potential_options_grade_3 = None
                    after_additional_potential_options_value_3 = None

                if len(json_cube_histories[i]['after_additional_potential_options']) > 0 :
                    after_additional_potential_options_grade_1 = json_cube_histories[i]['after_additional_potential_options'][0]['grade']
                    after_additional_potential_options_value_1 = json_cube_histories[i]['after_additional_potential_options'][0]['value']
                    after_additional_potential_options_grade_2 = json_cube_histories[i]['after_additional_potential_options'][1]['grade']
                    after_additional_potential_options_value_2 = json_cube_histories[i]['after_additional_potential_options'][1]['value']
                    after_additional_potential_options_grade_3 = json_cube_histories[i]['after_additional_potential_options'][2]['grade']
                    after_additional_potential_options_value_3 = json_cube_histories[i]['after_additional_potential_options'][2]['value']
                    after_potential_options_grade_1 = None
                    after_potential_options_value_1 = None
                    after_potential_options_grade_2 = None
                    after_potential_options_value_2 = None
                    after_potential_options_grade_3 = None
                    after_potential_options_value_3 = None

                # 데이터 저장
                setData = data(
                    id = id,
                    character_name = character_name,
                    create_date = create_date,
                    cube_type = cube_type,
                    item_upgrade_result = item_upgrade_result,
                    miracle_time_flag = miracle_time_flag,
                    item_equip_part = item_equip_part,
                    item_level = item_level,
                    target_item = target_item,
                    potential_option_grade = potential_option_grade,
                    additional_potential_option_grade = additional_potential_option_grade,
                    before_potential_options_grade_1 = before_potential_options_grade_1,
                    before_potential_options_grade_2 = before_potential_options_grade_2,
                    before_potential_options_grade_3 = before_potential_options_grade_3,
                    before_potential_options_value_1 = before_potential_options_value_1,
                    before_potential_options_value_2 = before_potential_options_value_2,
                    before_potential_options_value_3 = before_potential_options_value_3,
                    before_additional_potential_options_grade_1 = before_additional_potential_options_grade_1,
                    before_additional_potential_options_grade_2 = before_additional_potential_options_grade_2,
                    before_additional_potential_options_grade_3 = before_additional_potential_options_grade_3,
                    before_additional_potential_options_value_1 = before_additional_potential_options_value_1,
                    before_additional_potential_options_value_2 = before_additional_potential_options_value_2,
                    before_additional_potential_options_value_3 = before_additional_potential_options_value_3,
                    after_potential_options_grade_1 = after_potential_options_grade_1,
                    after_potential_options_grade_2 = after_potential_options_grade_2,
                    after_potential_options_grade_3 = after_potential_options_grade_3,
                    after_potential_options_value_1 = after_potential_options_value_1,
                    after_potential_options_value_2 = after_potential_options_value_2,
                    after_potential_options_value_3 = after_potential_options_value_3,
                    after_additional_potential_options_grade_1 = after_additional_potential_options_grade_1,
                    after_additional_potential_options_grade_2 = after_additional_potential_options_grade_2,
                    after_additional_potential_options_grade_3 = after_additional_potential_options_grade_3,
                    after_additional_potential_options_value_1 = after_additional_potential_options_value_1,
                    after_additional_potential_options_value_2 = after_additional_potential_options_value_2,
                    after_additional_potential_options_value_3 = after_additional_potential_options_value_3,
                )
                setData.save()                   
        except Exception as e:            
            logger.debug(e)
        
        result = {"count":f"{json_cubeHis['count']}", "date" : date}
        
    # return HttpResponse("데이터 INSERT 완료.")
    return render(request, 'html/returnpage.html', result, status=200)
    

def viewCubeInfo(request):
    return render(request, 'html/viewCubeInfo.html')