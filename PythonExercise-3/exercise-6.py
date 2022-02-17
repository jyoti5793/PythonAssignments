#question6
num_tuple = (5, 8, 13, 2, 17, 1)
list = list(num_tuple)
max = max(list)
list.remove(max)
list.sort()
print(list)