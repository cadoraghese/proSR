import matplotlib.pyplot as plt
import numpy as np


def moving_average(rewards, T):
    array = np.zeros(T)
    window = 5
    for x in range(0, T):
        sum = 0
        tmp_window = window
        y = x - tmp_window
        null_window = 0
        while y <= x + tmp_window:
            if y < 0:
                tmp_window -= 1
            elif y >= T:
                null_window += 1
            else:
                sum = sum + rewards[y]
            y += 1
        array[x] = sum / (2 * tmp_window + 1 - null_window)
    return array


name = 'fac_8x_16_128_low.txt'
f = open("errors_files/"+name, "r")
data_array = [[], [], []]

for line in f:
    if len(line.split(' ')) >= 8 and float(line.split(' ')[7]) != 0.0:
        data_array[0] += [float(line.split(' ')[7])]
    if len(line.split(' ')) >= 10 and float(line.split(' ')[9]) != 0.0:
        data_array[1] += [float(line.split(' ')[9])]
    if len(line.split(' ')) >= 12 and float(line.split(' ')[11]) != 0.0:
        data_array[2] += [float(line.split(' ')[11])]

plt.title(name)
for data in data_array:
    plt.plot(moving_average(data, len(data)))
plt.show()
