from PIL import Image
import os

limit = 512
train_set_number = str("2")
train_set = "train_" + train_set_number
path = "D:" + os.sep + "Downloads" + os.sep + "ADL Dataset" + os.sep + "OpenImage" + os.sep
count = 0
folder_name_for_cropped_images = '_512'
folder_name_for_rotated_images = '_cropped_rotated'
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


# Crop faces from images
count = 0
with open("faces.txt") as infile:
    for line in infile:

        count = count + 1
        if count % 10000 == 0:
            print(count)
        try:
            img = Image.open(path + train_set + os.sep + line.split(',')[0] + ".jpg")
            width, height = img.size
            minX = float(line.split(',')[4])*width
            maxX = float(line.split(',')[5])*width
            minY = float(line.split(',')[6])*height
            maxY = float(line.split(',')[7])*height
            deltaX = maxX - minX
            marginX = deltaX/10
            deltaY = maxY - minY
            marginY = deltaY/10

            left = max(0, round(minX - marginX))
            upper = max(0, round(minY - marginY))
            right = min(width, round(maxX + marginX))
            lower = min(height, round(maxY + marginY))

            if right - left >= limit and lower - upper >= limit:
                area = (left, upper, right, lower)
                img = img.crop(area)
                counter = 0
                if not os.path.exists(path + train_set + folder_name_for_cropped_images):
                    os.makedirs(path + train_set + folder_name_for_cropped_images)
                while os.path.isfile(path + train_set + folder_name_for_cropped_images + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg"):
                    counter = counter + 1
                img.save(path + train_set + folder_name_for_cropped_images + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")
        except IOError:
            pass


# Rotate faces
with open("rotations_old_sorted.txt") as infile:
    for line in infile:
        counter = 0
        condition = True
        while condition and line[0] == train_set_number:
            try:
                # Remove the images
                img = os.remove(path + train_set + folder_name_for_cropped_images + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")

                # Rotate them and save them in another directory
                # img = Image.open(path + train_set + folder_name_for_cropped_images + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")
                # img = img.rotate(round(float(line.split(',')[1])), expand=True)
                # if not os.path.exists(path + train_set + folder_name_for_rotated_images):
                #     os.makedirs(path + train_set + folder_name_for_rotated_images)
                # img.save(path + train_set + folder_name_for_rotated_images + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")

                # Needed in both cases
                counter = counter + 1
            except IOError:
                condition = False
                pass
