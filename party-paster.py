from PIL import ImageGrab
from io import BytesIO
import requests
import base64
import pyperclip
from json import loads

def handle_image(image):
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_str = base64.b64encode(buffered.getvalue())
    
    url = "https://api.imgur.com/3/upload"
    headers = {"Authorization": "Client-ID 09f3e475410f242"}
    form = {"image": image_str}
    response = requests.post(url, form, headers=headers)
    
    pyperclip.copy(loads(response.text)["data"]["link"])
    

def handle_text():
    url = "https://bpaste.net"
    form = {"code": pyperclip.paste(), "lexer": "text", "expiry": "1day"}
    response = requests.post(url, form)
    pyperclip.copy(response.url)

if __name__ == "__main__":
    im = ImageGrab.grabclipboard()

    if im:
        response = handle_image(im)
    else:
        handle_text()
