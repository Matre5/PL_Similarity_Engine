import streamlit as st
import time
import pandas as pd
from utils.visualisations import create_comparison_radar

st.set_page_config(page_title="Player Comparison", page_icon="📊", layout="wide")

st.sidebar.header("Player Comparison 📊")

@st.cache_data
def load_data():
    pca_df = pd.read_csv("data/pca_df.csv")
    stats_df = pd.read_csv('data/player_stats.csv')
    
    full_df = pca_df.merge(stats_df, on='player', how='inner')
    
    return full_df

df = load_data()

st.title(":red[Player Comparison]")
st.divider()
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.subheader("Player One", text_alignment="center")
    player1 = st.selectbox(
        "Select first player",
        options=sorted(df['player'].unique()),
        key='player1'
    )
    
    player1_data = df[df['player']==player1].iloc[0]
    
    st.image("assets/images/decs.png", caption=player1, width=200)
    st.metric("Role", player1_data['role_name'])
    st.metric("Team", player1_data['team_x'])
    st.metric("Minutes", f"{player1_data['minutes']:.0f}")
        
 
with col3:
    st.subheader("Player Two", text_alignment="center")
    player2 = st.selectbox(
        "Select second player",
        options=sorted(df['player'].unique()),
        key='player2'
    )
    
    player2_data = df[df['player']==player2].iloc[0]
    
    st.image("assets/images/decs.png", caption=player2, width=200)
    st.metric("Role", player2_data['role_name'])
    st.metric("Team", player2_data['team_x'])
    st.metric("Minutes", f"{player2_data['minutes']:.0f}")
    
with col2:
    
    st.subheader("Tactical Profile Comparison", text_alignment='center')
    if player1 != player2:

        radar_features = [
            'touches_def_3rd_pct',
            'touches_mid_3rd_pct', 
            'touches_att_3rd_pct',
            'touches_att_pen_pct',
            'tackles',
            'interceptions',
            'shots',
            'xg'
        ]

        fig = create_comparison_radar(
            player1_data,
            player2_data,
            radar_features,
            player1,
            player2
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("⚠️ Please select two different players to compare")