import os

train_set = "train_5"
path = "D:" + os.sep + "Downloads" + os.sep + "ADL Dataset" + os.sep
count = 0

list_of_images = os.listdir(path + train_set + os.sep)
list_of_names = set()

# Remove all images without faces boxes
with open("faces.txt") as infile:
    for line in infile:
        list_of_names.add(line.split(',')[0] + ".jpg")
for file in list_of_images:
    if file not in list_of_names:
        os.remove(path + train_set + os.sep + file)
    count = count + 1
    if count % 10000 == 0:
        print(count)


