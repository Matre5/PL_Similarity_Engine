import streamlit as st
import time
import pandas as pd
from utils.data_loader import find_similar_players
from utils.visualisations import create_player_radar

st.set_page_config(page_title="Player Comparison", page_icon="📊", layout="wide")

st.sidebar.header("Player Comparison 📊")

progress_bar = st.sidebar.progress(0)