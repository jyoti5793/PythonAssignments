list_1 = [1, 5, 8]
list_2 = [3, 2, 5]
list_3 = [2, 3, 6]
def find_sum(list_1,list_2,list_3):
    sum_of_lists = list(map(lambda i : sum(i),list(zip(list_1,list_2,list_3))))
    print(sum_of_lists)

find_sum(list_1,list_2,list_3)