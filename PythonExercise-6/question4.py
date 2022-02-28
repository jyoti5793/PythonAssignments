n = [2, 3, 5, 6, 8, 9]

def odd(n):
    return [n[i] for i in range(len(n)) if i%2!=0]
print(odd(n))