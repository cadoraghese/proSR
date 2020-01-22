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


f = open("error_overfit_500.txt", "r")
data = []
for line in f:
    data += [float(line.split(' ')[7])]

plt.plot(data)
plt.show()
