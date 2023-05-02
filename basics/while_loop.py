num = 0

coordinate_list = [[0,0]]


coordinate = [0,1]

if coordinate in coordinate_list:
    print("already exist")
    num = num
else:
    coordinate_list.append(coordinate)
    print(coordinate_list)
    num = num + 1

print(num)