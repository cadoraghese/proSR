from PIL import Image
import os

train_set_number = str(6)
train_set = "train_6"

path = "D:" + os.sep + "Downloads" + os.sep + "ADL Dataset" + os.sep

with open("rotations_old_sorted.txt") as infile:
    for line in infile:
        counter = 0
        condition = True
        while condition and line[0] == train_set_number:
            try:
                img = Image.open(path + train_set + "_cropped" + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")
                img = img.rotate(round(float(line.split(',')[1])), expand=True)
                if not os.path.exists(path + train_set + "_cropped_rotated"):
                    os.makedirs(path + train_set + "_cropped_rotated")
                img.save(path + train_set + "_cropped_rotated" + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")
                counter = counter + 1
            except IOError:
                condition = False
                pass
