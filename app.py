from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config


st.title("가까운 병원 찾기")

# pydeck 이해를 위한 테스트 코드

df = pd.read_csv('data/hospital_location_complete.csv', index_col= 0)
df.columns = ['인덱스', '분류', '이름', '전화번호', 'lat' , 'lon'] #,분류,이름,전화번호,location,x_coordinate,y_coordinate

# 병원 아이콘 URL
ICON_URL = "https://cdn.pixabay.com/photo/2017/10/08/19/55/cruz-2831364_960_720.png"

# 아이콘 크기 등 정의
icon_data = {
    "url": ICON_URL,
    "width": 242,
    "height": 242,
    "anchorY": 242,
}

df["icon_data"] = None

df_set = df.copy()

for i in df_set.index:
    df["icon_data"][i] = icon_data

view_state = pdk.data_utils.compute_view(df_set[["lon", "lat"]], 0.1)

icon_layer = pdk.Layer(
    type="IconLayer",
    data=df_set,
    get_icon="icon_data",
    get_size=4,
    size_scale=15,
    get_position=["lon", "lat"],
    pickable=True,
)


r = pdk.Deck(layers=[icon_layer], initial_view_state=view_state, tooltip={"text": "{이름}"})

st.pydeck_chart(r)