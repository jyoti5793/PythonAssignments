myList = [2, 8, [10, 20, [40, 60, [90, 100], 30, 70], 80], 50]
list_part = myList[2][2][2]
list_part.insert(2,200)
print(list_part)
print(myList)