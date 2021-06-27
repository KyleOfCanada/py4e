import re

inp = input('Enter a regular expression: ')

fhand = open('../ex_07/mbox.txt')

counter = 0
for line in fhand:
    lst = re.findall(inp, line)
    counter = counter + len(lst)

print('mbox.txt had', counter, 'lines that matched', inp)
