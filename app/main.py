from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from diffusers import StableDiffusionPipeline
import pickle
import os

app = FastAPI()

# Load the recommendation model
def load_recommendation_model(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)

recommendation_model = load_recommendation_model("model.pkl")

# Initialize text generation pipeline
def load_text_generator(model_name: str):
    return pipeline("text-generation", model=model_name)

text_generator = load_text_generator("gpt-3.5-turbo")

# Initialize Stable Diffusion pipeline
def load_stable_diffusion(model_name: str, device: str = "cuda"):
    pipeline = StableDiffusionPipeline.from_pretrained(model_name)
    pipeline.to(device)
    return pipeline

sd_pipeline = load_stable_diffusion("stabilityai/stable-diffusion-2")


class PlayerProfile(BaseModel):
    PlayerID: int
    GameGenre: str
    PlaytimeHours: int
    Spending: float


@app.post("/generate/")
def generate_content(profile: PlayerProfile):
    # Generate a recommendation
    reward = recommendation_model.predict([[profile.GameGenre, profile.PlaytimeHours, profile.Spending]])

    # Generate personalized text
    prompt = (
        f"Player profile: {profile.dict()}. Create a personalized reward message for this player."
    )
    text_message = text_generator(prompt, max_length=50)[0]["generated_text"]

    # Generate promotional image
    image_prompt = f"A promotional banner for a {profile.GameGenre} player with {profile.PlaytimeHours} hours of playtime."
    image = sd_pipeline(image_prompt).images[0]

    # Save the generated image
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    image_path = os.path.join(output_dir, f"player_{profile.PlayerID}_banner.png")
    image.save(image_path)

    return {
        "reward": reward[0],
        "message": text_message,
        "image_path": image_path,
    }
