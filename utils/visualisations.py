import plotly.graph_objects as go
import pandas as pd

def create_player_radar(player_data, league_avg, features, player_name):
    """
    Creates an interactive radar chart comparing player to league average
    
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



def create_comparison_radar(player1_data, player2_data, features, player1_name, player2_name):
    """
    Creates a radar chart comparing two players
    
    Args:
        player1_data (Series): First player's stats
        player2_data (Series): Second player's stats
        features (list): Features to display
        player1_name (str): First player's name
        player2_name (str): Second player's name
    
    Returns:
        plotly.graph_objects.Figure
    """
    
    fig = go.Figure()
    
    # Player 1 trace
    fig.add_trace(go.Scatterpolar(
        r=[player1_data[f] for f in features],
        theta=features,
        fill='toself',
        name=player1_name,
        line_color='#FF6B6B',
        fillcolor='rgba(255, 107, 107, 0.3)'
    ))
    
    # Player 2 trace
    fig.add_trace(go.Scatterpolar(
        r=[player2_data[f] for f in features],
        theta=features,
        fill='toself',
        name=player2_name,
        line_color="#4E52CD",
        fillcolor='rgba(78, 205, 196, 0.3)'
    ))
    
    # Layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(
                    player1_data[features].max(), 
                    player2_data[features].max()
                ) * 1.1]
            )
        ),
        showlegend=True,
        title=f"{player1_name} vs {player2_name}",
        height=600
    )
    
    return fig