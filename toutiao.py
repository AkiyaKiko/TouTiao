import requests
import json
from PIL import Image, ImageFont, ImageDraw

toutiao_url = "https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc"
Field1 = "data"
Field2 = "Title"
data = []

def getToutiao(url:str, field1:str, field2:str):
    x = requests.get(url) # Send Request
    x = json.loads(x.content).get(field1) # Get Content
    length = len(x)
    for i in range (0,20):
        print(i+1,end=' ')
        title = x[i].get(field2) # Get Title of Toutiao
        print(title)
        data.append(f"{i+1}. "+title) # Append each title to be ready to print

def create_image_with_text(data, image_size=(800, 1200), font_path="font/simhei.ttf", font_size=30, input_path="image/origin.png",output_path="image/output.png"):
    image = Image.open(input_path) # Open Template
    draw = ImageDraw.Draw(image)
    
    # Load Font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print("Font file not found. Using default font.")
        font = ImageFont.load_default()

    # Centered and Align left
    line_len = len(data[0])
    front = int(line_len/2 * font_size)
    x = (image_size[0])/2 - front
    y = 300
    line_spacing = font_size + 5
    
    # Writing into the image
    for line in data:
        draw.text((x, y), line, font=font, fill=(0, 0, 0))
        y += line_spacing
        if y + line_spacing > image_size[1]:  # Exceed the Image and break
            break

    # Save Image
    image.save(output_path)

# External Calling
def getToutiaoUpdate():
    getToutiao(url = toutiao_url, field1 = Field1, field2 = Field2)
    create_image_with_text(data)    


if __name__ == "__main__":
    getToutiaoUpdate()