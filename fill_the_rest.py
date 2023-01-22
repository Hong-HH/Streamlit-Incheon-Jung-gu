from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config


def get_coordinate(location ) :
    coordinate_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    
    params = {'query' : location}

    headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

    response = requests.get(coordinate_url, params=params, headers=headers).json()

    x_coordinate = response['documents'][0]['address']['x']
    y_coordinate = response['documents'][0]['address']['y'] 

    return [x_coordinate, y_coordinate]


st.title("위치 추가 안된 병원 추가입력")

df = pd.read_csv('data/hospital_location2.csv', index_col=0)

st.dataframe(df)

# 행의 수를 추출
num_lows = df.shape[0]

# 행으로 넣어줄 빈 리스트 생성
x_coordinate = []
y_coordinate = []


# 행의 수와 인덱스와 같은 리스트를 생성해 반복
for i in list(np.arange(num_lows)) :
    if df.iloc[i, 5] == '' :
        print("좌표 추가")
        location =  df.iloc[i, 2]
        coordinate_list = get_coordinate(location)

        df.iloc[i, 5] = coordinate_list[0]
        df.iloc[i, 6] = coordinate_list[1]


# 결과 확인
st.dataframe(df)


