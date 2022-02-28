list1 = [2,3,4,"saturday"]
list2 = [4,5,"wednesday",9,"Sunday","MOnday"]

def add_two_list(list1,list2):
    try:
        for i,j in zip(list1,list2):
            print(i+j)
    except IndexError as e:
        return e
    except TypeError as e:
        return e
print(add_two_list(list1,list2))