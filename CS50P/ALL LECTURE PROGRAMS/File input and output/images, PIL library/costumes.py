# import command line argument sys
import sys
# from PIL library import Image and create a empty list to store the image.
from PIL import Image

images = []
# using slice in sys.argv 
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
