with open("box-position.txt") as infile:
    for line in infile:
        if line.split(',')[0] == "2b93ea0ea91bef64":
            print(line)
