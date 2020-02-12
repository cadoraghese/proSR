import tools.scale as scale
import os
from argparse import Namespace

path = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
folder_list = os.listdir(path)
tmp = []
for folder in folder_list:
    if folder.split('_')[2] == 'HR':
        tmp += [folder]
folder_list = tmp
print(folder_list)
folder_list = ['general_1000_HR', 'faces_1000_HR']
for folder in folder_list:
    for size in [16,32,64,128,256,512]:
        args = Namespace(input=path + folder + '\\', output=path + folder.split('HR')[0] + str(size) + '\\', max_size=size, ratio=None)
        scale.main(args)
