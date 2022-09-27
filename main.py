from PIL import Image
from image_utils import ImageText
from cleantext import clean

# Cardo, bold, #8b0203
# returns a PIL Image
def makeIMG(text):
    w = 1080
    ORIGIN = (0, 0)
    WHITE  = (255, 255, 255)
    heightEnd      = 707
    heightBeg      = 340
    diff           = heightEnd - heightBeg
    color          = (139, 2, 3)
    font           = "Cardo-Bold.ttf"
    background     = "confess.png"
    height         = -float("inf")
    place          = "center"
    position       ='middle'
    text = clean(text.strip(), no_emoji=True).strip()
    left = 0
    right = 400
    size = 200
    params = {
        "xy" : ORIGIN,
        "text" : text, 
        "box_width" : w,
        "font_filename" : font, 
        "font_size" : left,
        "color" : color,
        "place" : place,
    }

    while left < size < right :
        im = ImageText((w, diff), background=WHITE)
        _, height = im.write_text_box(
            ORIGIN, text, box_width=w, font_filename=font, 
            font_size=size, color=color, place=place)
        if height < diff:
            left = size
        else:
            right = size 
        size = (left + right) // 2

    im = ImageText((w, diff), background=WHITE)
    im.write_text_box(
        ORIGIN, text, box_width=w, font_filename=font, 
        font_size=size, color=color, place=place, position=position)
    im.show()
    quit()
    #background = Image.open(background)
    #background.paste(im.getImage(), (0, heightBeg), mask=im.getImage())
    return background

if __name__ == "__main__":
    img = makeIMG("123 💬")
    img.show()