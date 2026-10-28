# r - read
# w - write
# a - append
# "r+" - read and write
# w+ - read and write override or create
# a+ - read and append

with open("students.txt", "r")as file:
    # data = file.read()
    # data = file.readline()
    # data = file.readlines()
    # print(data)

    for line in file:
        print(line.strip())