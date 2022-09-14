import os
import random
import display

imageList = []
for file in os.listdir('./kingcattos'):
    imageList.append('./kingcattos/' + file)
for file in os.listdir('./cat.shitpost'):
    imageList.append('./cat.shitpost/' + file)

randomIndex = random.randint(0, len(imageList))
image_to_show = imageList[randomIndex]
display.write_to_screen(image_to_show)
