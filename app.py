import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import find_similar_players

st.set_page_config(
    page_title="PL Similarity Engine",
    page_icon="⚽",
    layout="wide"
)

@st.cache_data
def load_data():
    pca_df = pd.read_csv('data/pca_df.csv')
    stats_df = pd.read_csv('data/player_stats.csv')
    
    full_df = pca_df.merge(stats_df, on='player', how='inner')
    
    return full_df

df = load_data()

st.title("⚽ PL Similarity Engine")
st.write(f"Total players loaded: {len(df)}")
st.write(f"Total unique roles: {df['role_name'].nunique()}")

selected_player = st.selectbox(
    "Search for a player",
    options=sorted(df['player'].unique())
)
# st.dataframe(df)

st.write(f"You selected: {selected_player}")
player_data = df[df['player']==selected_player].iloc[0]

st.divider()

col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.metric("Role", player_data['role_name'])
    st.metric("Team", player_data['team_x'])
    
with col2:
    st.metric("PC1 (Attacking)", f"{player_data['PC1']:.2f}")
    st.metric("PC2 (Involvement)", f"{player_data['PC2']:.2f}")
    st.metric("Interceptions", f"{player_data['interceptions']}")
    
with col3:
    st.metric("Minutes", f"{player_data['minutes']:.0f}")
    st.metric("xG", f"{player_data['xg']:.2f}")
    st.metric("Touches", f"{player_data['touches']}")
    

# Test function 1
print("=== ALL PLAYERS ===")
result1 = find_similar_players("Declan Rice", top_n=5)
print(result1)
print(type(result1))  # What type is this?

# print("\n=== SAME ROLE ONLY ===")
# result2 = similar_players("Declan Rice", pca_df, top_n=5)
# print(result2)
# print(type(result2))  # What type is this? 