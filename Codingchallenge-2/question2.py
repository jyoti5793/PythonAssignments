num_1 = {'a' : 5, 's' : 7, 'x' : 11, 'm' : 12, 'o' : 8}
num_2 = {'r' : 12, 'x' : 9, 'n' : 8, 'm' : 12, 'q' : 10}

ans_1 = {keys1 for keys1 in num_1.keys() for keys2 in num_2.keys() if keys1==keys2 }
print(ans_1)
ans_2 = {keys1:values1 for keys1,values1 in num_1.items() for keys2,values2 in num_2.items() if keys1==keys2 and values1==values2}
print(ans_2)

z= {key1 for key1 in num_1.keys()}
y = {key2 for key2 in num_2.keys()}
ans_3 = z.symmetric_difference(y)
print(ans_3)
ans_4 = z.difference(y)
print(ans_4)

ans_5 = {key:value for key,value in num_1.items() if key in ans_4}
print(ans_5)
