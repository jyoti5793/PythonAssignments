set_1 = {2, 8, 19, 13, 24, 55, 48, 93}
set_2 = {7, 11, 55, 84, 8, 65, 73, 13}
inter_set = set_1.intersection(set_2)
for ele in inter_set:
    set_1.remove(ele)
print(set_1)