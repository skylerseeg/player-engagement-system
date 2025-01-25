import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Correct the path to player_data.csv
data = pd.read_csv("app/player_data.csv")

# Encode categorical data
le = LabelEncoder()
data['GameGenre'] = le.fit_transform(data['GameGenre'])

# Split data into training and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Define and train a simple recommendation model
model = RandomForestClassifier()
model.fit(train[['GameGenre', 'PlaytimeHours', 'Spending']], train['PreferredRewards'])

# Save the model
import pickle
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved to 'app/model.pkl'")
