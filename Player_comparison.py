import streamlit as st
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
    
    st.image("assets/images/player_placeholder.svg", caption=player1, width=200)
    st.markdown("**Role**")
    st.markdown(f"<span style='font-size:18px'>{player1_data['role_name']}</span>", unsafe_allow_html=True)

    st.markdown("**Team**")
    st.markdown(f"<span style='font-size:18px'>{player1_data['team_x']}</span>", unsafe_allow_html=True)
    
    st.markdown("**Minutes**")
    st.markdown(f"<span style='font-size:20px'>{player1_data['minutes']:.0f}</span>", unsafe_allow_html=True)
        
 
with col3:
    st.subheader("Player Two", text_alignment="center")
    player2 = st.selectbox(
        "Select second player",
        options=sorted(df['player'].unique()),
        key='player2'
    )
    
    player2_data = df[df['player']==player2].iloc[0]
    
    st.image("assets/images/player_placeholder.svg", caption=player2, width=200)
    st.markdown("**Role**")
    st.markdown(f"<span style='font-size:20px'>{player2_data['role_name']}</span>", unsafe_allow_html=True)

    st.markdown("**Team**")
    st.markdown(f"<span style='font-size:20px'>{player2_data['team_x']}</span>", unsafe_allow_html=True)
    
    st.markdown("**Minutes**")
    st.markdown(f"<span style='font-size:20px'>{player2_data['minutes']:.0f}</span>", unsafe_allow_html=True)

    
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


        
st.divider()

# Stats comparison table
st.subheader("Detailed Stats Comparison", text_alignment="center")

comparison_stats = {
    'Metric': [
        'Defensive 3rd %',
        'Middle 3rd %',
        'Attacking 3rd %',
        'Penalty Area %',
        'Tackles/90',
        'Interceptions/90',
        'Shots/90',
        'xG/90'
    ],
    player1: [
        f"{player1_data['touches_def_3rd_pct']:.1f}%",
        f"{player1_data['touches_mid_3rd_pct']:.1f}%",
        f"{player1_data['touches_att_3rd_pct']:.1f}%",
        f"{player1_data['touches_att_pen_pct']:.1f}%",
        f"{player1_data['tackles']:.2f}",
        f"{player1_data['interceptions']:.2f}",
        f"{player1_data['shots']:.2f}",
        f"{player1_data['xg']:.2f}"
    ],
    player2: [
        f"{player2_data['touches_def_3rd_pct']:.1f}%",
        f"{player2_data['touches_mid_3rd_pct']:.1f}%",
        f"{player2_data['touches_att_3rd_pct']:.1f}%",
        f"{player2_data['touches_att_pen_pct']:.1f}%",
        f"{player2_data['tackles']:.2f}",
        f"{player2_data['interceptions']:.2f}",
        f"{player2_data['shots']:.2f}",
        f"{player2_data['xg']:.2f}"
    ]
}

comparison_df = pd.DataFrame(comparison_stats)

st.dataframe(
    comparison_df,
    hide_index=True,
    use_container_width=True
)