# ⚽ Premier League Similarity Engine

An interactive web app that finds tactically similar players in the Premier League using unsupervised machine learning.

🔗 **[Live App](https://your-streamlit-url.streamlit.app)**

---

## Overview

This tool discovers player roles through behavioral analysis rather than position labels. Using PCA and K-Means clustering on Premier League data, it identifies 5 distinct tactical profiles and enables similarity search across all players.

### Key Features

- **Similarity Search**: Find players with comparable tactical profiles using cosine similarity in PCA space
- **Interactive Radar Charts**: Visualize player profiles across 8 behavioral dimensions
- **Side-by-Side Comparison**: Compare two players directly with overlaid radar charts
- **Role Discovery**: 5 tactical archetypes emerged from unsupervised learning

---

## Methodology

### 1. Feature Engineering
Raw event data transformed into per-90 behavioral metrics:
- Touch distribution across thirds (defensive, middle, attacking, penalty area)
- Defensive actions (tackles, interceptions)
- Attacking output (shots, xG)

### 2. Dimensionality Reduction (PCA)
15 features reduced to 2 principal components capturing 76% of variance:
- **PC1**: Vertical Attacking Orientation
- **PC2**: Involvement & Work Rate

### 3. Clustering (K-Means)
5 natural player groupings discovered:
1. **Attacking Creators** - High final third presence
2. **Defensive Midfielders** - Strong midfield control, high defensive actions
3. **Box-to-Box Midfielders** - Balanced across all thirds
4. **Strikers** - Penalty area dominance
5. **Goalkeepers** - Discovered automatically without position labels

### 4. Similarity Search
Cosine similarity in PCA space identifies behavioral comparables regardless of position.

---

## Tech Stack

- **Python 3.11**
- **Streamlit** - Web framework
- **Scikit-learn** - PCA, K-Means clustering, cosine similarity
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation

---

## Dataset

- **Source**: FBref
- **League**: Premier League 2024/25
- **Players**: 432 (minimum 500 minutes)
- **Features**: 15 behavioral metrics

---

## Installation (Local Development)
```bash
# Clone the repository
git clone https://github.com/Matre5/PL_Similarity_Engine.git
cd PL_Similarity_Engine

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## Project Structure
```
PL_Similarity_Engine/
├── app.py                      # Main navigation
├── About.py                    # Landing page
├── PL_Similarity_Engine.py    # Similarity search page
├── Player_comparison.py       # Comparison page
├── data/
│   ├── pca_df.csv            # PCA results
│   └── player_stats.csv      # Player statistics
├── utils/
│   ├── data_loader.py        # Similarity search functions
│   └── visualizations.py     # Radar chart functions
└── requirements.txt
```

---

## Limitations

- **Team context bias**: Output metrics favor possession-dominant teams
- **Single season**: Only 2024/25 data; temporal consistency not validated
- **League specific**: Premier League only
- **Context blindness**: Doesn't account for opponent quality

---

## Future Enhancements

- [ ] Age and nationality filters
- [ ] Opponent-adjusted metrics
- [ ] Possession-normalized rates
- [ ] Multi-season tracking
- [ ] Cross-league expansion
- [ ] Player image integration
- [ ] Export functionality (CSV, PNG)

---

## Author

**Matre Aiguokhian**

- LinkedIn: [linkedin.com/in/matre-aiguokhian-iyen](https://www.linkedin.com/in/matre-aiguokhian-iyen)
- GitHub: [@Matre5](https://github.com/Matre5)

---

## License

MIT License - See LICENSE file for details

---

## Acknowledgments

- Data source: FBref
- Inspired by modern football analytics and unsupervised learning research

---

**Built with ❤️ using Streamlit**
