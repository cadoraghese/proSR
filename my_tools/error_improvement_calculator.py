import matplotlib.pyplot as plt
import numpy as np

def moving_average(rewards, T):
    array = np.zeros(T)
    window = 5
    for x in range(0, T):
        tmp = 0
        for y in range(x-window, x+window+1):
            if y < 0 or y >= T:
                tmp = tmp + rewards[x]
            else:
                tmp = tmp + rewards[y]
        array[x] = tmp / (2 * window + 1)
    for x in range(0, T):
        rewards[x] = array[x]
    return rewards


f = open("errors_files/gen_8x_32_256.txt", "r")
data_array = [[], [], []]

for line in f:
    if len(line.split(' ')) >= 7 and float(line.split(' ')[7]) != 0.0:
        data_array[0] += [float(line.split(' ')[7])]
    if len(line.split(' ')) >= 9 and float(line.split(' ')[9]) != 0.0:
        data_array[1] += [float(line.split(' ')[9])]
    if len(line.split(' ')) >= 11 and float(line.split(' ')[11]) != 0.0:
        data_array[2] += [float(line.split(' ')[11])]

for data in data_array:
    plt.plot(moving_average(data, len(data)))
plt.show()
