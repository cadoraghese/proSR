import tools.scale as scale
import os
from argparse import Namespace

path = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\'
folder_list = os.listdir(path)
folder_list = ['general_all_HR','general_400_HR','general_100_HR']
for folder in folder_list:
    for size in [64,128,256,512]:
        args = Namespace(input=path + folder + '\\', output=path + folder.split('HR')[0] + str(size) + '\\', max_size=size, ratio=None)
        scale.main(args)
