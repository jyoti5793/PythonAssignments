poem = '''Centre of equal daughters, equal sons,
All, all alike endeared, grown, ungrown, young or old,
Strong, ample, fair, enduring, capable, rich,
Perennial with the Earth, with Freedom, Law and Love,
A grand, sane, towering, seated Mother,
Chaired in the adamant of Time.'''
statement = poem.split()
list = []
vowels = ['a', 'e', 'i', 'o', 'u']
for words in statement:
    for letter in words:
        if letter.lower() not in vowels:
            list.append(letter)
#result = [letter for letter in words for words in statement if letter.lower() not in vowels]
final_result = ''.join(list)

print(final_result)
