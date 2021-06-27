inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('FIle not found!')
    quit()

wordsDic = {}
counter = 0

for line in fhand:
    words = line.split()
    for word in words:
        if word not in wordsDic:
            wordsDic[word] = counter
            counter = counter + 1

print(wordsDic)
