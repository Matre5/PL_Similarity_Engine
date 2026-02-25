import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
from datetime import datetime
from utils.data_loader import find_similar_players
from utils.visualisations import create_player_radar

st.set_page_config(
    page_title="Add Custom Player",
    page_icon="➕",
    layout="wide"
)

# Load data and models
@st.cache_data
def load_data():
    pca_df = pd.read_csv('data/pca_df.csv')
    stats_df = pd.read_csv('data/player_stats.csv')
    full_df = pca_df.merge(stats_df, on='player', how='inner')
    return full_df

@st.cache_resource
def load_models():
    with open('data/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('data/pca_model.pkl', 'rb') as f:
        pca = pickle.load(f)
    return scaler, pca

df = load_data()
scaler, pca = load_models()
league_avg = df.mean(numeric_only=True)

# Features that were scaled
SCALED_FEATURES = [
    'touches_def_3rd_pct', 'touches_mid_3rd_pct', 'touches_att_3rd_pct',
    'touches_att_pen_pct', 'touches', 'tackles', 'interceptions', 'shots', 'xg'
]

# Title
st.title("➕ Add Custom Player")
st.markdown("Input your own player stats and find similar Premier League players")

st.divider()

# Upload section
st.subheader("📤 Upload Player Data")
uploaded_file = st.file_uploader("Upload previously saved player data (JSON)", type=['json'])

if uploaded_file:
    player_data = json.load(uploaded_file)
    st.success(f"✅ Loaded: {player_data['player']}")
    st.session_state.custom_player = player_data

st.divider()

# Input form
st.subheader("📝 Enter Player Stats")

col1, col2 = st.columns(2)

with col1:
    player_name = st.text_input("Player Name*", placeholder="e.g. Gabriel Jesus")
    team_name = st.text_input("Team", placeholder="e.g., Arsenal")
    minutes = st.number_input("Minutes Played", min_value=0, value=900, help="Total minutes played this season")

with col2:
    touches = st.number_input("Touches per 90", min_value=0.0, value=50.0, step=1.0)
    tackles = st.number_input("Tackles per 90", min_value=0.0, value=2.0, step=0.1)
    interceptions = st.number_input("Interceptions per 90", min_value=0.0, value=1.0, step=0.1)

st.markdown("### Touch Distribution (as percentages)")
st.info("💡 These should add up to ~100%. They represent WHERE the player receives the ball.")

col3, col4, col5, col6 = st.columns(4)

with col3:
    def_3rd_pct = st.number_input("Defensive 3rd %", min_value=0.0, max_value=100.0, value=30.0, step=1.0)
with col4:
    mid_3rd_pct = st.number_input("Middle 3rd %", min_value=0.0, max_value=100.0, value=40.0, step=1.0)
with col5:
    att_3rd_pct = st.number_input("Attacking 3rd %", min_value=0.0, max_value=100.0, value=30.0, step=1.0)
with col6:
    att_pen_pct = st.number_input("Penalty Area %", min_value=0.0, max_value=100.0, value=10.0, step=1.0)

# Check if percentages are reasonable
total_pct = def_3rd_pct + mid_3rd_pct + att_3rd_pct
if total_pct > 0:
    st.caption(f"Total touch distribution: {total_pct:.1f}% (should be ~100%)")

st.markdown("### Attacking Output")

col7, col8 = st.columns(2)

with col7:
    shots = st.number_input("Shots per 90", min_value=0.0, value=1.5, step=0.1)
with col8:
    xg = st.number_input("xG per 90", min_value=0.0, value=0.15, step=0.01, help="Expected goals per 90 minutes")

st.divider()

# Action buttons
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2])

with col_btn1:
    analyze_button = st.button("🔍 Find Similar Players", type="primary", use_container_width=True)

with col_btn2:
    if player_name:
        # Create player data dict
        player_data_dict = {
            'player': player_name,
            'team': team_name,
            'minutes': minutes,
            'touches': touches,
            'touches_def_3rd_pct': def_3rd_pct,
            'touches_mid_3rd_pct': mid_3rd_pct,
            'touches_att_3rd_pct': att_3rd_pct,
            'touches_att_pen_pct': att_pen_pct,
            'tackles': tackles,
            'interceptions': interceptions,
            'shots': shots,
            'xg': xg,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Download button
        json_str = json.dumps(player_data_dict, indent=2)
        st.download_button(
            label="💾 Download Player Data",
            data=json_str,
            file_name=f"{player_name.replace(' ', '_')}_data.json",
            mime="application/json",
            use_container_width=True
        )

# Analysis
if analyze_button:
    if not player_name:
        st.error("⚠️ Please enter a player name!")
    elif total_pct < 80 or total_pct > 120:
        st.warning("⚠️ Touch distribution percentages seem off. They should add up to ~100%")
    else:
        # Create custom player dataframe
        custom_player_stats = pd.DataFrame([{
            'player': player_name,
            'team': team_name,
            'minutes': minutes,
            'touches': touches,
            'touches_def_3rd_pct': def_3rd_pct / 100,  # Convert to decimal
            'touches_mid_3rd_pct': mid_3rd_pct / 100,
            'touches_att_3rd_pct': att_3rd_pct / 100,
            'touches_att_pen_pct': att_pen_pct / 100,
            'tackles': tackles,
            'interceptions': interceptions,
            'shots': shots,
            'xg': xg
        }])
        
        # Scale the features
        features_to_scale = custom_player_stats[SCALED_FEATURES].values
        scaled_features = scaler.transform(features_to_scale)
        
        # Transform to PCA space
        pca_coords = pca.transform(scaled_features)
        
        custom_player_stats['PC1'] = pca_coords[0, 0]
        custom_player_stats['PC2'] = pca_coords[0, 1]
        
        # Store in session state
        st.session_state.custom_player_pca = custom_player_stats
        
        st.divider()
        
        # Display results
        st.success(f"✅ Analyzed {player_name}")
        
        col_res1, col_res2 = st.columns([1, 2])
        
        with col_res1:
            st.markdown("### Player Profile")
            st.metric("PC1 (Attacking)", f"{pca_coords[0, 0]:.2f}")
            st.metric("PC2 (Involvement)", f"{pca_coords[0, 1]:.2f}")
            st.metric("Minutes", f"{minutes:.0f}")
            st.metric("Team", team_name if team_name else "Custom")
        
        with col_res2:
            # Radar chart
            st.markdown("### Tactical Profile")
            radar_features = [
                'touches_def_3rd_pct', 'touches_mid_3rd_pct', 'touches_att_3rd_pct',
                'touches_att_pen_pct', 'tackles', 'interceptions', 'shots', 'xg'
            ]
            
            player_data_for_radar = custom_player_stats.iloc[0]
            
            fig = create_player_radar(
                player_data_for_radar,
                league_avg,
                radar_features,
                player_name
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.divider()
        
        # Find similar PL players
        st.subheader(f"🔍 Premier League Players Similar to {player_name}")
        
        # Combine custom player with PL database
        combined_df = pd.concat([df, custom_player_stats], ignore_index=True)
        
        # Find similar
        similar_players = find_similar_players(player_name, combined_df, top_n=10)
        
        # Remove the custom player itself from results (it will be 100% similar to itself)
        similar_players = similar_players[similar_players['player'] != player_name]
        
        # Format similarity
        similar_players['similarity_pct'] = (similar_players['similarity'] * 100).round(3)
        
        st.dataframe(
            similar_players[['player', 'team_x', 'role_name', 'similarity_pct']],
            hide_index=True,
            column_config={
                "player": "Player",
                "team_x": "Team",
                "role_name": "Role",
                "similarity_pct": st.column_config.NumberColumn(
                    "Similarity",
                    format="%.2f%%"
                )
            },
            use_container_width=True
        )

# Footer
st.divider()
st.info("""
**💡 Tips for accurate results:**
- Ensure touch distribution percentages add up to ~100%
- Use per-90 stats (not total season stats)
- Input data should match the quality/style of the league you're comparing to
- Download your player data to reload it later without re-entering stats
""")