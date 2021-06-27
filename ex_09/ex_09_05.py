inp = input('Enter a file name: ')

try:
    fhand = open(inp)
except IOError:
    print('File not found!')
    quit()

domains = {}
for line in fhand:
    if line.startswith('From '):
        domain = line.split()[1]
        domain = domain.split('@')[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)
