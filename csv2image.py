import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

data = np.loadtxt('./floor_data/floorm1.csv', delimiter = ',')
length = data.shape[0]
width = data.shape[1]
print(length)
print(width)
output = np.zeros((length, width))

for i in range(length):
    for j in range(width):
        if data[i, j] == 0: #Black 空地
            output[i, j] = 0
        elif data[i, j] <= 1: #White 墙壁
            output[i, j] = 255
        elif data[i, j] == 2: #gray134 楼梯
            output[i, j] = 100
        elif data[i, j] == 3: #不知道颜色 门
            output[i, j] = 200
        else: #可能会有过渡颜色
            output[i, j] = 1
# output = np.reshape(output, (width, length))
print(output.shape)
print(output[500])
# im = Image.fromarray(output)
plt.axis('off')
plt.imshow(output, cmap='gist_earth')
plt.savefig('./floor_new/floorm1.png')
