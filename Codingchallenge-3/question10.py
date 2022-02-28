num_list = [31, 24, 2, 16, 19, 45, 75, 63, 79]
n=3
x = [num_list[i:i + n] for i in range(0, len(num_list), n)]
print(x)
