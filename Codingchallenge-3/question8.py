list1 = []
for i in range(100,301):
    digits = str(i)
    j=0
    for digit in digits:
        if int(digit)%2!=0:
           break

        elif int(digit)%2==0:
                j+=1
    if j == len(digits):
        list1.append(digits)



print(list1)