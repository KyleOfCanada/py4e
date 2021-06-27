inp = input('Give me a file: ')

try :
    fhand = open(inp)
except :
    print('File not found!')
    quit()

count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    print(words[2])
