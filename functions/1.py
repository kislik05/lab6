my_list = [1, 2, 3, 4, 5]
s = 1

for i in range(len(my_list)):
    s = s * my_list[i]

print(''.join(map(str, [s])))
