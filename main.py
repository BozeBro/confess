# Cardo, bold, #8b0203
from PIL import Image, ImageDraw, ImageFont

w, h = 220, 190
shape = [(0, 372), (1080, 707)]
with Image.open("confess.png") as im:
    draw = ImageDraw.Draw(im) 
    draw.rectangle(shape, fill="white")
    im.show()
