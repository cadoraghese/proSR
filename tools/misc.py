import numpy as np
import matplotlib.pyplot as plt

array_prev_general = np.array([1.86, 2.57, 2.33, 2.09])[::-1]
array_prev_faces = np.array([-1.37, -0.23, 3.04, 3.99])[::-1]
array_aft_general = np.array([4.71, 3.51, 3.04, -2.28])[::-1]
array_aft_faces = np.array([9.9, 7.65, 4.95, 1.86])[::-1]

array_prev_linear_general = []
array_prev_db_general = []
array_prev_linear_faces = []
array_prev_db_faces = []
array_aft_linear_general = []
array_aft_db_general = []
array_aft_linear_faces = []
array_aft_db_faces = []

with open("manytests_original.txt") as infile:
    faces = 1
    for line in infile:
        if len(line) > 132:
            if faces:
                faces = 0
                array_prev_linear_faces += [float(line[86:92])]
                array_prev_db_faces += [float(line[96:101])]
                array_aft_linear_faces += [float(line[122:128])]
                array_aft_db_faces += [float(line[132:137])]
            else:
                faces = 1
                array_prev_linear_general += [float(line[86:92])]
                array_prev_db_general += [float(line[96:101])]
                array_aft_linear_general += [float(line[122:128])]
                array_aft_db_general += [float(line[132:137])]

array_prev_linear_general = array_prev_linear_general[::-1]
array_prev_db_general = array_prev_db_general[::-1]
array_prev_linear_faces = array_prev_linear_faces[::-1]
array_prev_db_faces = array_prev_db_faces[::-1]
array_aft_linear_general = array_aft_linear_general[::-1]
array_aft_db_general = array_aft_db_general[::-1]
array_aft_linear_faces = array_aft_linear_faces[::-1]
array_aft_db_faces = array_aft_db_faces[::-1]

array_total_linear = np.concatenate((array_prev_linear_faces, array_aft_linear_faces))
array_total_linear = np.concatenate((array_total_linear, array_prev_linear_general))
array_total_linear = np.concatenate((array_total_linear, array_aft_linear_general))

array_total_db = np.concatenate((array_prev_db_faces, array_aft_db_faces))
array_total_db = np.concatenate((array_total_db, array_prev_db_general))
array_total_db = np.concatenate((array_total_db, array_aft_db_general))

graphs = ['prev_linear', 'aft_linear', 'prev_db', 'aft_db']

for name in graphs:
    array_general = []
    array_faces = []
    array_total = []
    if name == 'prev_linear':
        array_general = array_prev_linear_general
        array_faces = array_prev_linear_faces
        array_total = array_total_linear
    if name == 'prev_db':
        array_general = array_prev_db_general
        array_faces = array_prev_db_faces
        array_total = array_total_db
    if name == 'aft_linear':
        array_general = array_aft_linear_general
        array_faces = array_aft_linear_faces
        array_total = array_total_linear
    if name == 'aft_db':
        array_general = array_aft_db_general
        array_faces = array_aft_db_faces
        array_total = array_total_db

    res = np.arange(len(array_general))
    assert len(res) == 7
    ticks = ['4X{:16}\n16->64'.format(''), '32->128', '64->256', '128->512',
             '8X{:16}\n16->128'.format(''), '32->256', '64->512'][::-1]

    array_red = np.zeros(len(res))
    array_green = array_faces
    array_green_2 = np.zeros(len(res))
    array_white = np.zeros(len(res))

    for i in res:
        if array_faces[i] > array_general[i]:
            array_white[i] = array_general[i]
        else:
            array_white[i] = 0
    for i in res:
        if array_faces[i] < array_general[i]:
            array_red[i] = array_faces[i]
        else:
            array_red[i] = 0
    for i in res:
        if array_general[i] < 0 and array_faces[i] > 0:
            array_green_2[i] = array_general[i]
        else:
            array_green_2[i] = 0

    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.barh(res, array_general, color='r')
    plt.barh(res, array_green, color='g')
    plt.barh(res, array_red, color='r')
    plt.barh(res, array_white, color='w')
    plt.barh(res, array_green_2, color='g')
    plt.axvline(linestyle='--', x=0)
    plt.axvline(x=array_general[6], ymin=0.84, ymax=0.97, linewidth=2, color='k')
    plt.axvline(x=array_general[5], ymin=0.70, ymax=0.84, linewidth=2, color='k')
    plt.axvline(x=array_general[4], ymin=0.57, ymax=0.70, linewidth=2, color='k')
    plt.axvline(x=array_general[3], ymin=0.43, ymax=0.57, linewidth=2, color='k')
    plt.axvline(x=array_general[2], ymin=0.3, ymax=0.43, linewidth=2, color='k')
    plt.axvline(x=array_general[1], ymin=0.17, ymax=0.3, linewidth=2, color='k')
    plt.axvline(x=array_general[0], ymin=0.03, ymax=0.17, linewidth=2, color='k')
    plt.xlim(np.floor(min(array_total))*1.1, np.ceil(max(array_total))*1.1)
    plt.yticks(res, ticks)
    plt.savefig('graphs/'+name+'.png', format='png', bbox_inches='tight')
    plt.show()

# Last column of manytests_1.txt
# text = ''
# psnr = []
# values = []
# tmp = 0
# with open("manytests_1.txt") as infile:
#     for line in infile:
#         if len(line) > 1:
#             print(line[75:80])
#             psnr += [float(line[75:80])]
# for i in range(0, len(psnr), 2):
#     value = 10 ** ((psnr[i] - psnr[i+1]) / 10) * 100.0 - 100.0 + 2.73
#     values += [value]
# print(values)
# with open("manytests_1.txt") as infile:
#     for line in infile:
#         if len(line) > 1:
#             if line[59] == 'f':
#                 print(line.split('\n')[0] + '{:>8.2f}%'.format(values[tmp]))
#                 tmp += 1
#             if line[59] == 'g':
#                 print(line.split('\n')[0])
