import os
import openai
from PIL import Image,ImageOps
from io import BytesIO
import requests

# Set API key and prompt
openai.api_key = os.getenv('OPENAI_KEY')
### write your code below this line
# CODIO SOLUTION BEGIN



prompt = "A futuristic city skyline with flying cars and skyscrapers"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)
# CODIO SOLUTION END
#Write your code above this line
image_url=(response['data'][0]['url'])
img_data = requests.get(image_url).content
with open('att.jpg', 'wb') as handler:
    handler.write(img_data)

