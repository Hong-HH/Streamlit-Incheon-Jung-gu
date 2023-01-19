import numpy as np
import pandas as pd
import requests
from config import Config


# 병원 이름에 따른 위치 및 좌표 추출

coordinate_url = 'https://dapi.kakao.com/v2/local/search/address.json'

location = "운남로 167"

params = {'query' : location}

headers = {'Authorization': 'KakaoAK ' + Config.REST_API_KEY}

response = requests.get(coordinate_url, params=params, headers=headers).json()

