list_1 = [5, 10, 15, 20, 25, 30, 35]
list_2 = [7, 14, 21, 28, 35, 42, 49]

odd_index = [list_1[x ]for x in range(len(list_1)) if x%2!=0]
even_index = [list_2[y]for y in range(len(list_2)) if y%2==0]
print(odd_index+even_index)