roll_numbers = {12, 7, 15, 23, 32, 30}
student_details = {12:'Judy', 30:'Shane', 23:'Aaron'}
list = []
for keys in student_details.keys():
    list.append(keys)
set1 = set(list)
print("Submitted applications",set1)
print("Pending applications",roll_numbers.difference(set1))
