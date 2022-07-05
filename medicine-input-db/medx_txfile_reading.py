file = open("../assets/medx.txt", "r")
# print(file.readline(3))

for x in file:
    y = x.split(' | ')
    for i in range(len(y)):
        print(y[i])
