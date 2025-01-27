from transformers import pipeline

# Initialize GPT model
generator = pipeline("text-generation", model="gpt-3.5-turbo")

def generate_content(data: dict):
    prompt = data.get("prompt", "Welcome to our game!")
    generated = generator(prompt, max_length=100, num_return_sequences=1)
    return {"generated_content": generated[0]["generated_text"]}
