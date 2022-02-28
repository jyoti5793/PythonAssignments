sample_text = "Learning Journal 2020"
z = sample_text.split()
count=0
count1=0
for letter in z:
    if letter.isdigit():
        count1=len(letter)
    if letter.isalpha():
        count+=len(letter)

print("Number of digits:",count1)
print("Number of letters:",count)