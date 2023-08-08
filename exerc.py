# CODIO SOLUTION BEGIN
import os
import openai
from PIL import Image,ImageOps
from io import BytesIO
import requests
import secret

# Set API key and prompt
openai.api_key = secret.key

def generate_image(user_input):
  # Generate more descriptive text with GPT-3
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"Create a more descriptive scene based on this user input: '{user_input}'.",
      max_tokens=50,
      n=1,
      stop=None,
      temperature=0.7)
  descriptive_text = response.choices[0].text.strip()
  response = openai.Image.create(
    prompt=descriptive_text,
    n=1,
    size="512x512")
  #Write your code above this line
  image_url=(response['data'][0]['url'])
  img_data = requests.get(image_url).content
  with open('my_img.png', 'wb') as handler:
      handler.write(img_data)
# CODIO SOLUTION END


