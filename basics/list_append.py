a_list = [1,2,3]
b_list = []

#うまくいくバージョン
#num_list = [0,1,2]
#b_list = [ a_list[x] for x in num_list ]

#うまくいくバージョン？
lenA = len(a_list)
b_list = [ a_list[x] for x in range(lenA) ]

#ダメなバージョン
#b_list = a_list

b_list.append(4)

print(a_list)
print(b_list)





