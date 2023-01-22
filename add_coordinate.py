from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config


# 병원 이름에 따른 위치 및 좌표 추출

def get_address(keyword) :

    location_url = 'https://dapi.kakao.com/v2/local/search/keyword.json'

    params = {'query' : keyword}

    headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

    response = requests.get(location_url, params=params, headers=headers).json()

    location_list = response['documents']
    print (len(location_list))

    # 리스트 일시 api가 같은 주소 2번 리턴하였을 때 중복해서 기록됨을 확인, set으로 바꿈
    temp_location = set()
    temp_x = set()
    temp_y = set()

    for location in location_list :
        road_address_name = location['road_address_name']
        print(road_address_name)
        if '인천 중구' in road_address_name :
            print("등록중~")
            temp_location.add(road_address_name)
            temp_x.add(location['x'])
            temp_y.add(location['y'])


    if len(temp_location) == 1 :
        return [list(temp_location)[0], list(temp_x)[0], list(temp_y)[0]]
    else :
        return ['', '', '']


# test_location = get_address("인천 중구 연안의원")

# print(test_location)
# print(len(test_location))
# print(test_location[0])
# print(test_location[1])
# print(test_location[2])
# print(type(test_location[1]))

# print(list(test_location[2]))
# print(type(list(test_location[2])))
# print(list(test_location[2])[0])


st.title("병원 주소와 좌표 찾기")

df = pd.read_csv('data/hospital.csv')

st.dataframe(df)

# 행의 수를 추출
num_lows = df.shape[0]

# 행으로 넣어줄 빈 리스트 생성
location = []
x_coordinate = []
y_coordinate = []

# 행의 수와 인덱스와 같은 리스트를 생성해 반복
for i in list(np.arange(num_lows)) :
    # 병원이름 추출
    keyword = df.iloc[i, 1] 
    print(keyword)
    location_list = []
    location_list = get_address(keyword)

    location.append(location_list[0])
    x_coordinate.append(location_list[1])
    y_coordinate.append(location_list[2])


df['location'] = location 
df['x_coordinate'] = x_coordinate 
df['y_coordinate'] = y_coordinate 


st.dataframe(df)

df.to_csv('data/hospital_location.csv')

