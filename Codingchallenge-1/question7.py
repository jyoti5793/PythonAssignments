num_list = [[2, 8, 11], [4, 5, 7, 12], [8, 9, 10, 11], [19, 13, 7], [2, 5, 16]]
dictionary = {}
for i in num_list:
    x = sum(i)
    dictionary.update({x:str(i)})
sorted_list = sorted(dictionary)
min = min(sorted_list)
max = max(sorted_list)
for i in sorted(dictionary):
    if i == min:
        print("The list with the minimum sum of elements:",dictionary[i])
    if i == max:
        print("The list with the maximum sum of elements:", dictionary[i])

