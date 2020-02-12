f = open("rotations.txt", "w+")
list_of_names = set()
with open("faces.txt") as infile:
    for line in infile:
        list_of_names.add(line.split(',')[0])
        count = 0
with open("id-rotation.txt", encoding="utf8") as infile2:
    for line2 in infile2:
        length = len(line2.split(','))
        if line2.split(',')[0] in list_of_names \
                and line2.split(',')[length-1] != "0.0\n" and line2.split(',')[length-1] != "\n":
            f.write(line2.split(',')[0] + "," + line2.split(',')[length-1])
f.close()
