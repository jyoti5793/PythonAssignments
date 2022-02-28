mySet = {2, 4, 6}
myDict = {'A':'John', 'B':'Emma', 'C':'Sam'}

for keys in myDict.keys():
    mySet.update(keys)
print(mySet)
