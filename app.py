from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from PIL import Image
from config import Config


st.title("가까운 병원 찾기")

location = st.text_input('원하는 도로명 주소 입력')

if st.button('검색'):

    df = pd.read_csv('data/hospital_location_complete.csv', index_col= 0)
    # print (df.columns)
    df.columns = [ '분류', '이름', '전화번호', '위치','lon' , 'lat'] #,분류,이름,전화번호,location,x_coordinate,y_coordinate

    # 병원 아이콘 URL
    ICON_URL1 = "https://cdn.pixabay.com/photo/2020/03/12/23/35/covid-19-4926456_960_720.png"
    ICON_URL2 = "https://cdn.pixabay.com/photo/2017/10/08/19/55/cruz-2831364_960_720.png"
    ICON_URL3 = "https://cdn.pixabay.com/photo/2017/09/30/18/58/lungs-2803208_960_720.png"
    ICON_URL4 = "https://cdn.pixabay.com/photo/2013/07/13/11/54/location-158934_960_720.png"



    # 아이콘 크기 등 정의
    icon_data1 = {
        "url": ICON_URL1,
        "width": 242,
        "height": 242,
        "anchorY": 242,
    }
    icon_data2 = {
        "url": ICON_URL2,
        "width": 242,
        "height": 242,
        "anchorY": 242,
    }
    icon_data3 = {
        "url": ICON_URL3,
        "width": 242,
        "height": 242,
        "anchorY": 242,
    }
    icon_data4 = {
        "url": ICON_URL4,
        "width": 242,
        "height": 242,
        "anchorY": 242,
    }


    # dataframe 에 icon_data 행 추가
    df["icon_data"] = None

    # 분류에 따라 아이콘 값 넣어주기
    for i in df.index:        

        if df.iloc[i,0] == 1:
            # print ("분류 1")
            df["icon_data"][i] =  icon_data1
        elif df.iloc[i,0] == 2 :
            # print ("분류 2")
            df["icon_data"][i] =  icon_data2
        elif df.iloc[i,0] == 3 :
            # print ("분류 3")
            df["icon_data"][i] =  icon_data3

        else :
            print("else")

    

    # 행의 수를 추출
    num_lows = df.shape[0]

    # 마지막 행에 내 위치에 대한 데이터 추가
    # 1. 내위치로 api 호출, 좌표 가져오기
    coordinate_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    params = {'query' : location} 
    headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

    try :
        response = requests.get(coordinate_url, params=params, headers=headers).json()

        x_coordinate = float(response['documents'][0]['address']['x'])
        y_coordinate = float(response['documents'][0]['address']['y'])

        

    except :
        print("Error in api")

    # 2. 정보 dataframe 에 넣기
    # 분류, 이름, 전화번호, 위치, lon, lat, icon_data
    df.loc[num_lows] = [4, "내 위치",'', location, x_coordinate, y_coordinate, icon_data4]

    # st.dataframe(df)

    # 연안동 중심으로 보면 중구 가운데 위치함
    # 지금은 입력된 위치 정보 (location) 기준으로 두기

    view_state = pdk.ViewState(
        longitude= x_coordinate,
        latitude= y_coordinate ,
        zoom=15,
        pitch=50
    )



    icon_layer = pdk.Layer(
        type="IconLayer",
        data=df,
        get_icon="icon_data",
        get_size=4,
        size_scale=15,
        get_position=["lon", "lat"],
        pickable=True,
    )

    # 맵스타일 참고 : https://deckgl.readthedocs.io/en/latest/gallery/text_layer.html , 여기서 하긴 했는데 예제에서 따온거라 전에 찾아둔 맵 스타일 모아둔거 다시 찾아보자
    r = pdk.Deck(map_style=pdk.map_styles.ROAD, layers=[icon_layer], initial_view_state=view_state, tooltip={"text": "{이름}"})

    st.pydeck_chart(r)

    # 범례 넣어주기
    image = Image.open('data/hospital_legend.png')

    st.image(image)



