f = open("faces.txt", "w+")
with open("box-position.txt") as infile:
    for line in infile:
        if line.split(',')[2] == "/m/0dzct" \
                and line.split(',')[9] == "0" and line.split(',')[10] == "0" and line.split(',')[11] == "0":
            f.write(line)
f.close()
