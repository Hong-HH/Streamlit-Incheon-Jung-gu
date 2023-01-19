from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config
from add_coordinate import get_coordinate


st.title("가까운 병원 찾기")

df = pd.read_csv('data/hospital.csv')

st.dataframe(df)

# 행의 수를 추출
num_lows = df.shape[0]

# 행의 수와 인덱스와 같은 리스트를 생성해 반복
for i in list(np.arange(num_lows)) :
    # 병원이름 추출
    keyword = df.iloc[i, 1] 
    print(keyword)

