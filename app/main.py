from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import pickle
from diffusers import StableDiffusionPipeline

app = FastAPI()

# Load pre-trained recommendation model
with open("model.pkl", "rb") as f:
    recommendation_model = pickle.load(f)

# Load GPT model
text_generator = pipeline("text-generation", model="gpt-3.5-turbo")

# Load Stable Diffusion for image generation
sd_pipeline = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")
sd_pipeline.to("cuda")


class PlayerProfile(BaseModel):
    PlayerID: int
    GameGenre: str
    PlaytimeHours: int
    Spending: float


@app.post("/generate/")
def generate_content(profile: PlayerProfile):
    # Predict recommended reward
    reward = recommendation_model.predict([[profile.GameGenre, profile.PlaytimeHours, profile.Spending]])
    
    # Generate personalized text
    text_message = text_generator(f"Player profile: {profile.dict()}. Generate a reward message.", max_length=50)[0]['generated_text']
    
    # Generate promotional image
    prompt = f"A promotional banner for a {profile.GameGenre} player with {profile.PlaytimeHours} hours."
    image = sd_pipeline(prompt).images[0]
    image.save("output.png")
    
    return {"reward": reward[0], "message": text_message, "image_path": "output.png"}
