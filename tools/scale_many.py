from tools import scale         # remove 'from tools' on the gcloud version
import os
from argparse import ArgumentParser
from argparse import Namespace


def parse_args():
    parser = ArgumentParser(description='Downscale many')
    parser.add_argument('-i', '--input', help='Input')

    args_in = parser.parse_args()

    return args_in


args = parse_args()

path = args.input
folder_list = os.listdir(path)
tmp = []
print(folder_list)
for folder in folder_list:
    if folder.split('_')[2] == 'HR':
        tmp += [folder]
folder_list = tmp
print(folder_list)
# folder_list = ['general_1000_HR', 'faces_1000_HR']
for folder in folder_list:
    for size in [16, 32, 64, 128, 256, 512]:
        print('scale {} to {}px'.format(folder, size))
        args = Namespace(input=path + folder + os.sep, output=path + folder.split('HR')[0] + str(size) + os.sep,
                         max_size=size, ratio=None)
        scale.main(args)
