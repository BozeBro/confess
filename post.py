from PIL import Image
from image_utils import ImageText
from cleantext import clean
from typing import List
from math import floor

# Cardo, bold, #8b0203
# returns a PIL Image
# Form link
def makeIMG(text: str) -> Image:
    w = 1080
    ORIGIN = (0, 0)
    WHITE = (255, 255, 255)
    heightEnd = 707
    heightBeg = 340
    diff = heightEnd - heightBeg
    color = (139, 2, 3)
    font = "Cardo-Bold.ttf"
    background = "confess.png"
    height = -float("inf")
    place = "center"
    position = "middle"
    text = clean(text.strip(), no_emoji=True).strip()

    left = 0
    right = 400
    size = 200
    while left < size < right:
        im = ImageText((w, diff), background=WHITE)
        _, height = im.write_text_box(
            ORIGIN,
            text,
            box_width=w,
            font_filename=font,
            font_size=size,
            color=color,
            place=place,
        )
        if height < diff:
            left = size
        else:
            right = size
        size = (left + right) // 2

    im = ImageText((w, diff), background=WHITE)
    im.write_text_box(
        ORIGIN,
        text,
        box_width=w,
        font_filename=font,
        font_size=size,
        color=color,
        place=place,
        position=position,
    )
    background = Image.open(background)
    background.paste(im.getImage(), (0, heightBeg), mask=im.getImage())
    return background


def makeManyIMG(texts: List):
    return map(makeIMG, filter(lambda x: x.strip() != "", texts))


def saveImgs(imgs):
    with open("counter.txt", "r") as f:
        val = f.read().strip()
        counter = 0
        if val.isnumeric():
            counter = int(val)
    for img in imgs:
        img.save(f"./confessions/img{counter}.png")
        counter += 1
    with open("counter.txt", "w") as f:
        f.write(str(counter))


if __name__ == "__main__":
    tes = r'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.'
    img = makeIMG(tes)
    img.show()
