inp = input('Enter file: ')

try :
    fhand = open(inp)
except :
    print('File not found!')
    quit()

words = list()
for line in fhand :
    word = line.split()
    for i in range(len(word)) :
        if len(words) == 0 :
            words.append(word[i].lower())
            continue
        if word[i].lower() in words :
            continue
        words.append(word[i].lower())

words.sort()
print(words)
