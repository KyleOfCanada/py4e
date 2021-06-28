import urllib.request, urllib.parse, urllib.error
import re

inp = input('Enter URL: ')

if re.search('^http://', inp):
    inp = re.findall('^http://(\S+)', inp)[0]


if not re.search('\S+\.\S+/\S+', inp):
    print('Not a proper URL!')
    quit()

host = inp.split('/')[0]
doc = inp.split('/')[1:]
document = str()
for i in doc:
    document = document + i


fhand = urllib.request.urlopen('http://' + host + '/' + document)

counter = 0
for line in fhand:
    data = line.decode().strip()
    counter = counter + len(data)
    if counter <= 3000:
        print(data)
print(counter)
