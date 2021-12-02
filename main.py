f = open("adatok_2_day","r")

depth = 0
horizontal = 0
aim = 0
for i in f:
    y,x = i.split(" ")
    if y == "forward":
        horizontal += int(x)
        depth += aim * int(x)
    elif y == "down":
        aim += int(x)
    else:
        aim -= int(x)

print(depth * horizontal)