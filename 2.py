from random import randint
from PIL import Image
im = Image.new('RGB', (1080, 1080))
for x in range(1080):
    for y in range(1080):
        r = 0
        g = randint(0, 255)
        b = randint(0, 255)
        im.putpixel((x, y), (r, g, b))
im.show()
