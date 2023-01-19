import numpy as np
import pandas as pd
import requests
from config import Config

# 병원 이름에 따른 위치 및 좌표 추출

def get_coordinate(keyword) :
    coordinate_url = 'https://dapi.kakao.com/v2/local/search/address.json'

    params = {'query' : keyword}

    headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

    response = requests.get(coordinate_url, params=params, headers=headers).json()

    location_list = response['documents']

    temp_location = []
    temp_x = []
    temp_y = []

    for location in location_list :

        if location['address']['region_1depth_name'] ==  '인천'  and  location['address']['region_1depth_name'] == '중구':
            temp_location.append({})
            temp_x.append({location['address']['x']})
            temp_y.append({location['address']['y']})

    if len(temp_location) == 1 :
        return [temp_location[0], temp_x[0], temp_y[0]]
    else :
        return ['', '', '']



# x_coordinate = response['documents'][0]['address']['x']
# y_coordinate = response['documents'][0]['address']['y']