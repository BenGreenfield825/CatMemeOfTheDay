import datetime
from PIL import Image, ImageDraw, ImageShow
import instaloader  # https://instaloader.github.io/as-module.html#python-module-instaloader
from instaloader.structures import Profile
import random, os
import display

# kingcattos, cat.shitpost


imageList = []
for file in os.listdir('./kingcattos'):
    imageList.append('./kingcattos/' + file)
for file in os.listdir('./cat.shitpost'):
    imageList.append('./cat.shitpost/' + file)

randomIndex = random.randint(0, len(imageList))

# print(imageList)
# print(imageList[randomIndex])

image = Image.open(imageList[randomIndex])
# image.show()

display.write_to_screen(image)