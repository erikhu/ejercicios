queries = input()
x = 0
y = 1
end = "0"
while(queries != end):
    coordinates = str.split(input())
    for i in range(int(queries)):
        position = str.split(input())
        ln = int(position[x]) - int(coordinates[x])
        lt = int(position[y]) - int(coordinates[y])
        r = "no found"
        if 0 in [lt, ln]: r = "divisa"
        elif lt > 0 and ln > 0: r = "NE"
        elif lt < 0 and ln < 0: r = "SO"
        elif lt > 0 and ln < 0: r = "NO"
        elif lt < 0 and ln > 0: r = "SE"
        print(r)
    queries = input()
