inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

hours = {}
for line in fhand:
    if not line.startswith('From '):
        continue
    time = line.split()[5]
    hour = time.split(':')[0]
    hours[hour] = hours.get(hour, 0) + 1

lst = sorted([(k, v) for k, v in hours.items()])

for i in lst:
    print(i[0], i[1])
