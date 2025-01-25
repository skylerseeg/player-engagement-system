import pandas as pd
import random
import os

# Step 1: Create Synthetic Data
# Define genres and reward types
genres = ["FPS", "RPG", "Strategy", "MOBA", "Adventure"]
rewards = ["SkinPack", "WeaponUpgrade", "BonusLevel", "GoldCoins", "CharacterBoost"]

# Generate synthetic player data
num_players = 500
random.seed(42)

player_data = {
    "PlayerID": [i for i in range(1, num_players + 1)],
    "GameGenre": [random.choice(genres) for _ in range(num_players)],
    "PlaytimeHours": [random.randint(10, 500) for _ in range(num_players)],
    "Spending": [random.randint(0, 200) for _ in range(num_players)],
    "PreferredRewards": [random.choice(rewards) for _ in range(num_players)],
}

# Convert to DataFrame
data = pd.DataFrame(player_data)

# Ensure the 'app' directory exists
os.makedirs("app", exist_ok=True)

# Save to CSV
data.to_csv("app/player_data.csv", index=False)

print("Synthetic data created and saved to 'app/player_data.csv'.")
