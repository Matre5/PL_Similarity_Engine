import streamlit as st
import pandas as pd
import numpy as np
from utils.data_loader import find_similar_players
from utils.visualisations import create_player_radar
from st_click_detector import click_detector

st.set_page_config(
    page_title="PL Similarity Engine",
    page_icon="⚽",
    layout="wide"
)

st.sidebar.success("⚽ PL Similarity Engine")

@st.cache_data
def load_data():
    pca_df = pd.read_csv('data/pca_df.csv')
    stats_df = pd.read_csv('data/player_stats.csv')
    
    full_df = pca_df.merge(stats_df, on='player', how='inner')
    
    return full_df

df = load_data()
league_avg = df.mean(numeric_only=True)

st.title("⚽ PL Similarity Engine")

col1, col2, col3 = st.columns([10, 0.2, 10])

with col1:
    
    selected_player = st.selectbox(
        "Search for a player",
        options=sorted(df['player'].unique())
    )
    # st.dataframe(df)

    # player = selected_player.lower().replace(" ", "_")
    
    # player_id = "204480" 
    # image_url = f"https://resources.premierleague.com/{player_id}.png"

    player_data = df[df['player']==selected_player].iloc[0]

    st.divider()

    cl1, cl2 = st.columns([1,2])

    with cl1:
        st.image("assets/images/decs.png", caption=selected_player, width=200)
        st.metric("Role", player_data['role_name'])
        st.metric("Team", player_data['team_x'])
        
        
        
    with cl2:
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
        
        st.subheader("Player Profile")
        radar_fig = create_player_radar(
            player_data, 
            league_avg, 
            radar_features,
            selected_player
        )
        st.plotly_chart(radar_fig, use_container_width=True)
        
    # with cl3:
    #     st.metric("Minutes", f"{player_data['minutes']:.0f}")
    #     st.metric("xG", f"{player_data['xg']:.2f}")
    #     st.metric("Touches", f"{player_data['touches']}")
        
with col2:
    # Use st.markdown to inject HTML/CSS for the vertical line
    st.markdown(
        """
        <div class="divider-vertical-line"></div>
        <style>
        .divider-vertical-line {
            border-left: 2px solid rgba(49, 51, 63, 0.2);
            height: 80vh; /* Adjust height as needed to cover your content */
            margin: auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
     

with col3: 
    # Similarity section header
    st.subheader("🔍 Find Similar Players")
    
    num = st.slider("Number of similar players", 1,20)
    # Button to trigger search
    if st.button("Find Similar Players", type="primary"):
        # Call the function
        similar_players = find_similar_players(selected_player, df, top_n=num)
        
        # Show results
        st.subheader(f"Top {num} players similar to {selected_player}")
        
        # Format similarity as percentage
        similar_players['similarity_pct'] = (similar_players['similarity'] * 100).round(4)
        
        # Display the table
        st.dataframe(
            similar_players[['player', 'team_x', 'role_name', 'similarity_pct']],
            hide_index=True,
            column_config={
                "player": "Player",
                "team": "Team",
                "role_name": "Role",
                # "similarity_pct": st.column_config.NumberColumn(
                #     "Similarity",
                #     format="%.1f%%"
                # )
            },
            use_container_width=True
        )