inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

addresses = {}
for line in fhand:
    if not line.startswith('From '):
        continue
    address = line.split()[1]
    addresses[address] = addresses.get(address, 0) + 1

lst = sorted([(v, k) for k, v in addresses.items()], reverse=True)[0]

print(lst[1], lst[0])
