import streamlit as st

about_page = st.Page("About.py", title="🔍 About", default=True)
PL_page = st.Page("PL_Similarity_Engine.py", title="⚽ PL Similarity Engine")
PL_C_page = st.Page("Player_comparison.py", title="⚽ Player Comparison")
C_Player_page = st.Page("Custom_Player.py", title="➕ Custom Player")

pg = st.navigation([about_page, PL_page, PL_C_page, C_Player_page])
# pg = st.navigation([about_page, PL_page, PL_C_page])

st.set_page_config(
    page_title="PL Similarity Engine",
    page_icon="⚽",
    layout="wide"
)

pg.run()
