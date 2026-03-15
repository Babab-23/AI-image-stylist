import io
from huggingface_hub import InferenceClient
from PIL import Image, ImageEnhance, ImageFilter
from datetime import datetime

# Hugging Face API Key
HF_API_KEY = "YOUR_HF_API_KEY"

# Model
MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

# Create client
client = InferenceClient(api_key=HF_API_KEY)

# Ask user for prompt
prompt = input("Enter your image prompt: ")

print("Generating image...")

# Generate image
image_bytes = client.text_to_image(prompt, model=MODEL)

# Convert to image
image = Image.open(io.BytesIO(image_bytes))

# Save original
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
original_name = f"original_{timestamp}.png"
image.save(original_name)

print(f"Original image saved as {original_name}")

# -------------------------
# DAYLIGHT EDITION
# -------------------------

daylight = image.copy()

brightness = ImageEnhance.Brightness(daylight)
daylight = brightness.enhance(1.3)

contrast = ImageEnhance.Contrast(daylight)
daylight = contrast.enhance(0.9)

daylight = daylight.filter(ImageFilter.GaussianBlur(1))

daylight_name = f"daylight_{timestamp}.png"
daylight.save(daylight_name)

print(f"Daylight edition saved as {daylight_name}")

# -------------------------
# NIGHT MOOD
# -------------------------

night = image.copy()

brightness = ImageEnhance.Brightness(night)
night = brightness.enhance(0.7)

contrast = ImageEnhance.Contrast(night)
night = contrast.enhance(1.4)

night = night.filter(ImageFilter.GaussianBlur(2))

night_name = f"night_{timestamp}.png"
night.save(night_name)

print(f"Night mood version saved as {night_name}")

print("All images generated successfully!")