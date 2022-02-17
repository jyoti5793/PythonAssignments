#question10
myList = ['Red', 'Blue', 'Orange', 'White', 'Black', 'Yellow']
list = []
for i in range(len(myList)):
    if i%2!=0:
        list.append(myList[i])
print(list)