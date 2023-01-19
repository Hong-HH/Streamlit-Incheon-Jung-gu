from pydeck.bindings.view_state import ViewState
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
import requests
from config import Config
from add_coordinate import get_coordinate

st.title("가까운 병원 찾기")

