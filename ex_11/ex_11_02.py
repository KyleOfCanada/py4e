import re

inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

counter = 0
total = 0.0
for line in fhand:
    lst = re.findall('New Revision: (\d+)', line)
    for i in lst:
        counter = counter + 1
        num = float(lst[0])
        total = total + num

print(int(total / counter))
