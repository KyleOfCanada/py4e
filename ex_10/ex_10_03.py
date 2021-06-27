inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

letters = {}
for line in fhand:
    for letter in line:
        letter = letter.lower()
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1

lst = sorted([(v, k) for k, v in letters.items()], reverse=True)

for i in lst:
    print(i[1])
