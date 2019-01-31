import numpy as np
import matplotlib.pyplot as plt

inf = 999
rho = 0.5
length, width = 75, 150
passage, wall, door, stair, man = 0, 1, 2, 3, 4
#todo 加了stair改了man


floorm1 = np.loadtxt('./All_Data/floorm1.csv', delimiter=',')
# floor0 = np.loadtxt('./All_Data/floor0.csv', delimiter=',')
# floor1 = np.loadtxt('./All_Data/floor1.csv', delimiter=',')
# floor2 = np.loadtxt('./All_Data/floor2.csv', delimiter=',')
floorm1_stair = np.loadtxt('./All_Data/floorm1_stair.csv', delimiter=',')
# floor0_stair = np.loadtxt('./All_Data/floor0_stair.csv', delimiter=',')
# floor1_stair = np.loadtxt('./All_Data/floor1_stair.csv', delimiter=',')
# floor2_stair = np.loadtxt('./All_Data/floor2_stair.csv', delimiter=',')



stair_pos = [(67,10),(68,10),(69,10),(70,10)]

class GameOfLife(object):
    def __init__(self, cells_shape):
        self.cells = np.zeros(cells_shape) #  0没人 1有人
        self.timer = 0
        self.k1 = 0.1
        self.k2 = 2
        self.N = np.zeros(cells_shape) #kesi 函数
        self.D = np.zeros(cells_shape)  # people following
        self.P = np.zeros(cells_shape)  # choose ways
        self.S = np.loadtxt('S{ij}.csv', delimiter=',')  # distance
        self.floor = floorm1
        #todo 新增的 0,1,2,3 上右下左
        self.d = -1

        #初始化人群分布
        for i in range(cells_shape[0]):
            for j in range(cells_shape[1]):
                if self.floor[i][j] == 0:
                    self.cells[i][j] = 1 if np.random.randint(100 + 100 * rho) / 100 > 1 else 0


    def update_state(self):
        # buf = np.zeros(self.cells.shape)
        cells = self.cells
        self.D = self.D / 2



        #算每个cell的P
        for i in range(cells.shape[0]):
            for j in range(cells.shape[1]):
                self.P[i][j] = 0
                if self.floor[i][j] == passage:
                    #todo 概率公式
                    self.P[i][j] = (self.k1 * self.S[i][j]) * (1 - cells[i][j]) * (1- self.N[i][j])
                    # self.P[i][j] = np.exp(self.k1 * self.S[i][j] + self.k2 * self.D[i][j])
                elif self.floor[i][j] == door:
                    self.P[i][j] = inf
                elif self.floor[i][j] == stair:
                    self.P[i][j] = inf

        #算四个P
        for i in range(cells.shape[0]):
            for j in range(cells.shape[1]):
                if self.cells[i][j] == 1:
                    direction = -1
                    maxP = 0
                    P_u, P_r, P_l, P_d = 0, 0, 0, 0
                    #todo 通过四个方向概率 算预运动方向direction
                    if i - 1 >= 0:
                        P_u = self.P[i - 1][j]
                    else:
                        P_u = 0
                    if j + 1 < width:
                        P_r = self.P[i][j + 1]
                    else:
                        P_r = 0
                    if i + 1 < length:
                        P_l = self.P[i + 1][j]
                    else:
                        P_l = 0
                    if j - 1 >= 0:
                        P_d = self.P[i][j - 1]
                    else:
                        P_d = 0
                    arr = np.array([P_u, P_r, P_l, P_d])
                    direction = np.argmax(arr)


                    # choose here
                    #todo 最好能够随机
                    if direction == 0 and self.floor[i - 1][j] == 0:   # 想往上走而且上面没人
                        cells[i - 1][j] = 1
                        cells[i][j] = 0
                        self.floor[i - 1][j] = man
                        self.floor[i][j] = 0
                        self.D[i - 1][j] += 10
                        self.d = 0
                    elif direction == 1 and self.floor[i][j + 1] == 0:
                        cells[i][j + 1] = 1
                        cells[i][j] = 0
                        self.floor[i][j + 1] = man
                        self.floor[i][j] = 0
                        self.D[i][j + 1] += 10
                        self.d = 1
                    elif direction == 2 and self.floor[i + 1][j] == 0:
                        cells[i + 1][j] = 1
                        cells[i][j] = 0
                        self.floor[i + 1][j] = man
                        self.floor[i][j] = 0
                        self.D[i + 1][j] += 10
                        self.d = 2
                    elif direction == 3 and self.floor[i][j - 1] == 0:
                        cells[i][j - 1] = 1
                        cells[i][j] = 0
                        self.floor[i][j - 1] = man
                        self.floor[i][j] = 0
                        self.D[i][j - 1] += 10
                        self.d = 3
                    elif direction == 0 and (self.floor[i - 1][j] == 2 or self.floor[i - 1][j] == 3):  #
                        cells[i - 1][j] = 0
                        cells[i][j] = 0
                        self.floor[i][j] = 0
                        self.D[i - 1][j] += 10
                        self.d = 0
                    elif direction == 1 and (self.floor[i][j + 1] == 2 or self.floor[i][j + 1] == 3):
                        cells[i][j + 1] = 0
                        cells[i][j] = 0
                        self.floor[i][j] = 0
                        self.D[i][j + 1] += 10
                        self.d = 1
                    elif direction == 2 and (self.floor[i + 1][j] == 2 or self.floor[i + 1][j] == 3):
                        cells[i + 1][j] = 0
                        cells[i][j] = 0
                        self.floor[i][j] = 0
                        self.D[i + 1][j] += 10
                        self.d = 2
                    elif direction == 3 and (self.floor[i][j - 1] == 2 or self.floor[i][j - 1] == 3):
                        cells[i][j - 1] = 0
                        cells[i][j] = 0
                        self.floor[i][j] = 0
                        self.D[i][j - 1] += 10
                        self.d = 3
                    else: #不动 direction = -1
                        cells[i][j] = 1
                        self.floor[i][j] = man
                        self.D[i][j] += 10
                        self.d = -1

        # clear the man in the door
        for i in stair_pos:
            x = i[0]
            y = i[1]
            cells[x][y] = 0
            self.floor[x][y] = 0

        self.timer += 1
        # cells[67][10] = cells[68][10] = cells[69][10] = cells[4][29] = cells[9][29] = 0
        # self.floor[26][1] = self.floor[27][1] = self.floor[28][1] = self.floor[4][29] = self.floor[9][29] = 0
        # # self.cells = buf
        # self.timer += 1




    def update_and_plot(self, n_iter):
        plt.ion()
        print(game.cells.shape)

        for i in range(game.cells.shape[0]):
            for j in range(game.cells.shape[1]):
                if self.floor[i][j] == 1:
                    self.N[i][j] == 1
                else:
                    self.N[i][j] == 0

        # for _ in range(n_iter):
        for _ in range(1):
            plt.title('Iter :{}'.format(self.timer))
            self.update_state()
            plt.axis('off')
            plt.imshow(self.floor)
            plt.savefig('./photo/floor%d_%d.png'%(-1,7))
            plt.pause(0.1)
        plt.ioff()


if __name__ == '__main__':
    rho = 0.02
    game = GameOfLife(cells_shape=(length, width))
    game.update_and_plot(60)


#todo 1. 下方 向下走有问题
#todo 2. 下方cell要一个空一个才能pass | 瞬移