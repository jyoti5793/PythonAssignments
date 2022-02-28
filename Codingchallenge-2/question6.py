list = []
for i in range(20,60):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)
