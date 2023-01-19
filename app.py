from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config


# st.title("가까운 병원 찾기")

coordinate_url = 'https://dapi.kakao.com/v2/local/search/address.json'

location = "운남로 167"

params = {'query' : location}

headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

response = requests.get(coordinate_url, params=params, headers=headers).json()


x_coordinate = response['documents'][0]['address']['x']
y_coordinate = response['documents'][0]['address']['y']

print(x_coordinate)
