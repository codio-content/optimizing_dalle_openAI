## Conditional Image Generation with DALL-E 2 API


Conditional image generation using DALL-E 2 API allows developers to control various attributes of the generated images by specifying them in the prompt. This powerful feature enables users to create images with desired characteristics, such as specific styles, colors, or content. In this page, we will explore how to control image attributes using the DALL-E 2 API, providing examples and explanations of how the prompts can be crafted to achieve specific results.

As we go through the examples. We are going to keep the libraries we import and our API key. 
```python-hide-clipboard
import os
import openai
from PIL import Image,ImageOps
from io import BytesIO
import requests
import secret

# Set API key and prompt
openai.api_key = secret.key
```



At the bottom of our page will be the code to generate, save and visualize our images.
```python-hide-clipboard
image_url=(response['data'][0]['url'])
img_data = requests.get(image_url).content
with open('att.jpg', 'wb') as handler:
    handler.write(img_data)
```
 We want to keep that. All the following examples should go in the middle of the two codes. 

**Example 1: Controlling style**
```python


prompt = "A cubist painting of a cat"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)


```
{Try it !}(python3 imageATT.py)
[Click here to refresh your image](close_file att.jpg panel=1; open_file att.jpg panel=1) 


In this example, we specify the desired style of the generated image ("cubist painting") along with the subject ("a cat"). By including the style in the prompt, DALL-E 2 will generate an image of a cat in the cubist painting style.

**Example 2: Controlling color**
```python

prompt = "A red sports car on a blue background"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)

```
{Try it !}(python3 imageATT.py 2)
[Click here to refresh your image](close_file att.jpg panel=1; open_file att.jpg panel=1) 
In this example, we specify the desired colors of the generated image by including "red sports car" and "blue background" in the prompt. DALL-E 2 will generate an image of a red sports car with a blue background, as requested.

### Example 3: Controlling content

```python
prompt = "A futuristic city skyline with flying cars and skyscrapers"

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="512x512"
)

```
{Try it !}(python3 imageATT.py 3)
[Click here to refresh your image](close_file att.jpg panel=1; open_file att.jpg panel=1) 

In this example, we specify the desired content of the image by describing a futuristic city skyline with flying cars and skyscrapers. DALL-E 2 will generate an image that matches the provided description, creating a scene with the specified elements.


Controlling image attributes using the DALL-E 2 API is a powerful way to generate images that match specific requirements or artistic visions. By crafting prompts that include the desired attributes, developers can guide DALL-E 2 to create images with specific styles, colors, and content. Experimenting with different prompts and combinations of attributes can lead to diverse and creative results.




{Check It!|assessment}(multiple-choice-2181403027)
