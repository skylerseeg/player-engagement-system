import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Mock player data
player_data = pd.read_csv("data/sample_data.csv")

def recommend(player_id: int):
    # Mock recommendation logic
    player = player_data[player_data["player_id"] == player_id]
    if player.empty:
        return {"error": "Player not found"}
    
    # Example: Recommend items similar to what the player purchased
    similarity_scores = cosine_similarity(player_data.iloc[:, 1:], player.iloc[:, 1:])
    recommended_ids = player_data.iloc[similarity_scores.argsort()[0][-5:]]["item_id"].tolist()
    
    return {"player_id": player_id, "recommended_items": recommended_ids}
