import streamlit as st


# Hero section
st.title("⚽ Premier League Similarity Engine")
st.markdown("### Find tactical comparables using unsupervised machine learning")

st.divider()

# What is this section
col1, col2 = st.columns([2, 1])

with col1:
    st.header("What is this?")
    st.markdown("""
    This tool helps you discover **tactically similar players** in the Premier League using behavioral data and machine learning.
    
    Unlike traditional scouting that relies on position labels ("midfielder", "striker"), this system analyzes **what players actually do on the pitch**:
    - Where they receive the ball (defensive, middle, attacking thirds)
    - How they contribute (shots, tackles, progressive actions)
    - Their overall involvement and work rate
    
    The result? Find cheaper alternatives, identify role fits, and discover unexpected comparisons.
    """)

with col2:
    st.info("""
    **📊 Dataset**
    
    - 432 Premier League players
    - 2024/25 season
    - 500+ minutes played
    - 15 behavioral metrics
    - 5 tactical roles discovered
    """)

st.divider()

# How it works
st.header("How does it work?")

st.markdown("""
The system uses **unsupervised machine learning** to discover player roles from behavior, not position labels.
""")

# Methodology in expandable sections
with st.expander("🔬 Step 1: Feature Engineering"):
    st.markdown("""
    Raw event data is transformed into **per-90 behavioral metrics**:
    
    - **Touch distribution**: Percentage of touches in defensive third, middle third, attacking third, penalty area
    - **Defensive actions**: Tackles and interceptions per 90 minutes
    - **Attacking output**: Shots and expected goals (xG) per 90 minutes
    
    All metrics are normalized to account for playing time differences.
    """)

with st.expander("📐 Step 2: Dimensionality Reduction (PCA)"):
    st.markdown("""
    **Principal Component Analysis (PCA)** reduces 15 features into 2 dimensions while preserving 76% of variance:
    
    - **PC1**: Vertical Attacking Orientation (defensive ← → attacking positioning)
    - **PC2**: Involvement & Work Rate (specialist ← → omnipresent)
    
    This creates a "tactical space" where similar players cluster together.
    """)

with st.expander("🎯 Step 3: Clustering (K-Means)"):
    st.markdown("""
    **K-Means clustering** discovers 5 natural player groupings based on behavioral similarity:
    
    1. **Attacking Creators** - High final third presence, progressive actions
    2. **Defensive Midfielders** - Strong midfield control, high defensive actions
    3. **Box-to-Box Midfielders** - Balanced across all thirds, high work rate
    4. **Strikers** - Penalty area dominance, shot volume
    5. **Goalkeepers** - Extreme defensive positioning (discovered automatically!)
    
    Notably, the model discovered goalkeepers as a distinct cluster **without being told what a goalkeeper is**.
    """)

with st.expander("🔍 Step 4: Similarity Search"):
    st.markdown("""
    **Cosine similarity** in PCA space finds tactically comparable players:
    
    - Players close in "tactical space" have similar behavioral profiles
    - Similarity scores show how close the match is (99%+ = nearly identical roles)
    - Works across teams and positions
    
    This reveals alternatives you might not find through traditional scouting.
    """)

st.divider()

# Features
st.header("Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🔍 Similarity Search
    - Search any PL player
    - Find top N similar players
    - See similarity scores
    - Filter by number of results
    """)

with col2:
    st.markdown("""
    ### 📊 Tactical Profiles
    - Interactive radar charts
    - Player vs league average
    - 8-dimensional comparison
    - Visual role identification
    """)

with col3:
    st.markdown("""
    ### ⚖️ Player Comparison
    - Side-by-side analysis
    - Overlaid radar charts
    - Detailed stats table
    - Cross-role comparison
    """)

st.divider()

st.header("Use Cases")
col1, col2, col3, col4 = st.columns(4)
# Use cases

with col1:
    
    st.markdown("""
    ### For Recruiters
    - Find cheaper alternatives to expensive targets
    - Identify players who fit your tactical system
    - Discover overlooked talent with similar profiles
    - Validate scouting recommendations with data
    """)
    
with col2:
    st.markdown("""
    ### For Analysts
    - Understand player tactical roles quantitatively
    - Compare players across teams and leagues
    - Identify tactical archetypes in your data
    - Support transfer decision-making with evidence
    """)

with col3:
    st.markdown("""
    ### For Coaches
    - Assess squad composition (do you have role coverage?)
    - Identify players who can deputize for injured starters
    - Find tactical fits for your system
    - Plan recruitment based on behavioral needs
    """)

with col4:
    st.markdown("""
    ### For Fans
    - Discover who your favorite player is similar to
    - Understand tactical roles beyond position labels
    - Explore player profiles visually
    - See the game through a data lens
    """)

st.divider()

# Limitations
st.header("Current Limitations")

st.warning("""
**⚠️ Important Considerations**

- **Team context bias**: Output metrics (shots, xG) favor players from attacking-dominant teams
- **Single season**: Only 2024/25 data; role consistency over time not validated
- **League specific**: Premier League only; cross-league transferability unknown
- **Minimum threshold**: 500+ minutes filter excludes squad players and recent signings
- **Context blindness**: Doesn't account for opponent quality or team tactics

**Future improvements:** Opponent-adjusted metrics, possession-normalized rates, multi-season tracking
""")

st.divider()

# How to use
st.header("How to Use This Tool")

st.markdown("""
### 1️⃣ **PL Similarity Engine**
- Select a player from the dropdown
- View their role and tactical profile (radar chart)
- Click "Find Similar Players" to discover comparables
- Adjust the slider to see more or fewer results

### 2️⃣ **Player Comparison**
- Select two players from the dropdowns
- View their roles, teams, and playing time
- Compare radar charts (overlaid visualization)
- Analyze detailed stats side-by-side

### 3️⃣ **Interpret Results**
- **Similarity scores**: 99%+ = nearly identical, 95-99% = very similar, 90-95% = similar role
- **Radar shapes**: Overlapping areas = similar strengths, gaps = differences
- **Role labels**: Behavioral clusters, not positions
""")

st.divider()

# About the creator
st.header("About")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/images/Matty.png", width=200)  # Replace with your photo when you add it

with col2:
    st.markdown("""
    **Built by:** Matre Aiguokhian
    
    Data scientist and football analytics enthusiast building tools to make player analysis more accessible.
    
    This project demonstrates how unsupervised machine learning can discover tactical patterns that traditional 
    scouting methods miss.
    
    **Connect:**

    - [LinkedIn](www.linkedin.com/in/matre-aiguokhian-iyen)
    - [Github](https://github.com/Matre5)
    
    **Tech Stack in this project:** Python, Streamlit, Scikit-learn, Plotly, Pandas
    
    **Data Source:** FBref (Premier League 2024/25)
    """)

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <p>© 2026 Matre Aiguokhian | Built with ❤️ using Streamlit</p>
    <p>Data: FBref | Premier League 2024/25</p>
</div>
""", unsafe_allow_html=True)

# Call to action
st.success("Ready to explore? Head to the **PL Similarity Engine** to get started! ⚽")