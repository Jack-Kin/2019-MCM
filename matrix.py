from PIL import Image
import numpy as np


# image = Image.open('D:/jinh/桌面/matrix/floor/floor-1.png')  # 打开一个图片对象
image = Image.open('./floor_new/floorm1.png')
print(image.format)  # 查看图片的格式
print(image.size)  # 查看图片的大小，结果表示宽和高的像素
print(image.mode)  # 查看图片的模式，结果为'RGB',其他模式还有位图模式、灰度模式、双色调模式等等

length = image.size[0]
width = image.size[1]

data = image.getdata()
data = np.matrix(data)
print(data.shape)

sel = data[:, 0]

data = np.reshape(sel, (length, width))
output = np.zeros((length, width))
ite1 = 0
ite2 = 0
x = 0
for i in range(length):
    for j in range(width):
        if 134 > data[i, j] >= 0: #Black 空地
            output[i, j] = 0
            ite1 = ite1 + 1
        elif 200 < data[i, j] <= 255: #White 墙壁
            output[i, j] = 1
            ite2 = ite2 + 1
        elif data[i, j] == 134: #gray134 楼梯
            output[i, j] = 2
        elif data[i, j] == 200: #不知道颜色 门
            output[i, j] = 3
        else: #可能会有过渡颜色
            output[i, j] = 1

print(ite1)
print(ite2)

output = np.reshape(output, (width, length))
print(output.shape)


# np.save('D:/jinh/桌面/matrix/floor_data/floor-1.npy', output)
np.save('./floor_data_new/floorm1.npy', output)
np.savetxt('./floor_data_new/floorm1.csv', output, delimiter=',')
