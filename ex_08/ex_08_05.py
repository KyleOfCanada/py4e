inp = input('Enter file: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

counter = 0
for line in fhand:
    if line.startswith('From '):
        print(line.split()[1])
        counter = counter + 1

print("There were", counter, 'lines in the file with From as the first word.')
