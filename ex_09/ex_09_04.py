inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

senders = {}
for line in fhand:
    if line.startswith('From '):
        sender = line.split()[1]
        senders[sender] = senders.get(sender, 0) + 1

maxValue = 0
maxHandle = None
for handle, value in senders.items():
    if value > maxValue:
        maxValue = value
        maxHandle = handle

print(maxHandle, maxValue)
