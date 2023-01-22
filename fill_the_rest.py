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



