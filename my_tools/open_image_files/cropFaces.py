from PIL import Image
import os

limit = 256

train_set = "train_5"

path = "D:" + os.sep + "Downloads" + os.sep + "ADL Dataset" + os.sep
#list_of_images = os.listdir(path + train_set + os.sep)

count = 0

with open("faces.txt") as infile:
    for line in infile:

        count = count + 1
        if count % 10000 == 0:
            print(count)
#        if line.split(',')[0] + ".jpg" in list_of_images:
        try:
            img = Image.open(path + train_set + os.sep + line.split(',')[0] + ".jpg")
            width, height = img.size
            minX = float(line.split(',')[4])*width
            maxX = float(line.split(',')[5])*width
            minY = float(line.split(',')[6])*height
            maxY = float(line.split(',')[7])*height
            deltaX = maxX - minX
            marginX = deltaX/4
            deltaY = maxY - minY
            marginY = deltaY/4

            left = max(0, round(minX - marginX))
            upper = max(0, round(minY - marginY))
            right = min(width, round(maxX + marginX))
            lower = min(height, round(maxY + marginY))

            if right - left >= limit and lower - upper >= limit:
                area = (left, upper, right, lower)
                img = img.crop(area)
                counter = 0
                if not os.path.exists(path + train_set + "_cropped"):
                    os.makedirs(path + train_set + "_cropped")
                while os.path.isfile(path + train_set + "_cropped" + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg"):
                    counter = counter + 1
                img.save(path + train_set + "_cropped" + os.sep + line.split(',')[0] + "." + str(counter) + ".jpg")
        except IOError:
            pass
