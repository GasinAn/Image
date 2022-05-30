from random import randint
from PIL import Image
im = Image.new('RGB', (1080, 1080))
for x in range(1080):
    for y in range(1080):
        c = randint(128, 255)
        r = 0
        g = c
        b = c
        im.putpixel((x, y), (r, g, b))
im.show()
