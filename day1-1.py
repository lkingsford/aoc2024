still_going = True

list_1 = []
list_2 = []

while still_going:
    line = input()
    if line == "":
        still_going = False
        break
    v1, v2 = line.split("   ")
    list_1.append(v1)
    list_2.append(v2)

list_1.sort()
list_2.sort()

distance = 0

for i, value in enumerate(list_1):
    distance += abs(int(list_2[i]) - int(value))

print(distance)
