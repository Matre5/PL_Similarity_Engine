import plotly.graph_objects as go
import pandas as pd

def create_player_radar(player_data, league_avg, features, player_name):
    """
    Create interactive radar chart comparing player to league average
    
    Args:
        player_data (Series): Player's stats
        league_avg (Series): League average stats
        features (list): List of features to display
        player_name (str): Name of player for title
    
    Returns:
        plotly.graph_objects.Figure
    """
    
    # Create the figure
    fig = go.Figure()
    
    # Add player trace
    fig.add_trace(go.Scatterpolar(
        r=[player_data[f] for f in features],
        theta=features,
        fill='toself',
        name=player_name,
        line_color='#FF6B6B',
        fillcolor='rgba(255, 107, 107, 0.3)'
    ))
    
    # Add league average trace
    fig.add_trace(go.Scatterpolar(
        r=[league_avg[f] for f in features],
        theta=features,
        fill='toself',
        name='League Avg',
        line_color="#4E56CD",
        fillcolor='rgba(78, 205, 196, 0.2)'
    ))
    
    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(player_data[features].max(), league_avg[features].max()) * 1.1]
            )
        ),
        showlegend=True,
        title=f"{player_name} vs League Average",
        height=500
    )
    
    return fig