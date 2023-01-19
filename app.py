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

x = requests.get(coordinate_url, params=params, headers=headers).json()

print(x)

#  x
# {'documents': [{'address': {'address_name': '인천 중구 운남동 1524', 'b_code': '2811014600', 'h_code': '2811062000', 'main_address_no': '1524', 'mountain_yn': 'N',
#  'region_1depth_name': '인천', 'region_2depth_name': '중구', 'region_3depth_h_name': '영종동', 'region_3depth_name': '운남동', 'sub_address_no': '', 
# 'x': '126.532948950121', 'y': '37.4926027457283'}, 'address_name': '인천 중구 운남로 167', 'address_type': 'ROAD_ADDR', '
# road_address': {'address_name': '인천 중구 운남로 167', 'building_name': '허브빌딩', 'main_building_no': '167', 'region_1depth_name': '인천',
#  'region_2depth_name': '중구', 'region_3depth_name': '운남동', 'road_name': '운남로', 'sub_building_no': '', 'underground_yn': 'N', 'x': '126.532948950121', 'y': '37.4926027457283', 
# 'zone_no': '22372'}, 'x': '126.532948950121', 'y': '37.4926027457283'}], 'meta': {'is_end': True, 'pageable_count': 1, 'total_count': 1}}


