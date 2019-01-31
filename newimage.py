# import sys,os
from PIL import Image
import numpy as np

image = Image.open('./floor_new/floor2.png')  # 打开一个图片对象
image = image.convert("RGB")
print(image.format)  # 查看图片的格式
print(image.size)  # 查看图片的大小，结果表示宽和高的像素
print(image.mode)  # 查看图片的模式，结果为'RGB',其他模式还有位图模式、灰度模式、双色调模式等等
data = image.getdata()
data = np.matrix(data)
print(data.shape)

width = image.size[0]
height = image.size[1]
for i in range(0, width):
    for j in range(0, height):
        data = (image.getpixel((i, j)))
        # if not ((data[0] == 200 and data[1] == 202 and data[2] == 203)
        #         or (data[0] == 122 and data[1] == 122 and data[2] == 122)):
        #     image.putpixel((i, j), (255, 255, 255))
        if data[0] == 253 and data[1] == 250 and data[2] == 250:
            image.putpixel((i, j), (255, 255, 255))
        if data[0] == 61 and data[1] == 144 and data[2] == 93:
            image.putpixel((i, j), (150, 150, 150))
        # elif data[0] == 0 and data[1] == 0 and data[2] == 0:
        #     image.putpixel((i, j), (0, 0, 0))
        # else:
        #     image.putpixel((i, j), (150, 150, 150))
image.show()
image.save('./floor_new/floor2.png')
