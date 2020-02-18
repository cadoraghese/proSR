from PIL import Image
import os
import numpy as np


path = 'D:\\Documents\\Workspace\\ADL_proSR\\data\\datasets\\open_image\\general_100_512\\'
files = os.listdir(path)
total = np.zeros(3)
for file in files:
    print(str(file))
    tmp = np.zeros(3)
    img = Image.open(path + file)
    w, h = img.size
    rgb_img = img.convert('RGB')
    for x in range(w):
        for y in range(h):
            r, g, b = rgb_img.getpixel((x, y))
            tmp[0] += r/255
            tmp[1] += g/255
            tmp[2] += b/255
    tmp = np.divide(tmp, w * h)
    total = np.add(total, tmp)
total = np.divide(total, len(files))
print(total)