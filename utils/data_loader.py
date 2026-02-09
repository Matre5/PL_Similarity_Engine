from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def find_similar_players(target_player, df, top_n=10):
    """Find similar players using cosine similarity"""
    
    # Get coordinates for all players
    coords = df[['PC1', 'PC2']].values
    
    # Calculate similarity
    similarities = cosine_similarity(coords, coords)
    
    # Create similarity dataframe
    similarity_df = pd.DataFrame(
        similarities,
        index=df['player'],
        columns=df['player']
    )
    
    # Get similar players (exclude the target player itself)
    similar = similarity_df[target_player].sort_values(ascending=False)
    similar = similar.iloc[1:top_n+1]  # Skip first (it's the player themselves)
    
    # Get full player details
    result = df[df['player'].isin(similar.index)].copy()
    result['similarity'] = result['player'].map(similar)
    result = result.sort_values('similarity', ascending=False)
    
    return result[['player', 'team', 'role_name', 'similarity']]