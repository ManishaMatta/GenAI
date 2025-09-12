# Install the transformers library
# !pip install transformers Pillow torch torchvision torchaudio

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests

# Initialize the processor and model from Hugging Face
processor1 = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model1 = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
# Load an image
image = Image.open("BLIP/sample_img.png")
# Prepare the image
inputs = processor1(image, return_tensors="pt")
# Generate captions
outputs = model1.generate(**inputs)
caption = processor1.decode(outputs[0],skip_special_tokens=True)
print("Generated Caption:", caption)

# Load BLIP processor and model
processor2 = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model2 = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
# Image URL 
img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg'
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
# Specify the question you want to ask about the image
question = "What is in the image?"
# Use the processor to prepare inputs for VQA (image + question)
inputs = processor2(raw_image, question, return_tensors="pt")
# Generate the answer from the model
out = model2.generate(**inputs)
# Decode and print the answer to the question
answer = processor2.decode(out[0], skip_special_tokens=True)
print(f"Answer: {answer}")