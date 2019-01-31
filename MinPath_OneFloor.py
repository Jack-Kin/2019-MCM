import numpy as np
floor = -1
m = 6
S1 = np.loadtxt("./All_Data/S_current_%d_%d.csv"%(floor,1), delimiter = ',')
S2 = np.loadtxt("./All_Data/S_current_%d_%d.csv"%(floor,2), delimiter = ',')
S3 = np.loadtxt("./All_Data/S_current_%d_%d.csv"%(floor,3), delimiter = ',')
S4 = np.loadtxt("./All_Data/S_current_%d_%d.csv"%(floor,4), delimiter = ',')
S6 = np.loadtxt("./All_Data/S_current_%d_%d_d.csv"%(floor,1), delimiter = ',')
S7 = np.loadtxt("./All_Data/S_current_%d_%d_d.csv"%(floor,2), delimiter = ',')

length = S1.shape[0]
width = S2.shape[1]
print('load Done')
S = np.zeros((length, width))
for k in np.arange(1, m + 1):
    for i in range(length):
        for j in range(width):
            S[i,j] = -1
            S[i,j] = min(S1[i,j], S2[i,j],S3[i,j],S4[i,j],S6[i,j],S7[i,j])

np.savetxt("./All_Data/S_ij_%d.csv"%floor, S, delimiter = ',')


