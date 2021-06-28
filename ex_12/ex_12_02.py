import socket
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

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host, 80))
except:
    print('Host not found!')
    quit()
cmd = ('GET http://' + host + '/' + document + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

counter = 0
while True:
    data = mysock.recv(512)
    counter = counter + len(data)
    if (len(data) < 1):
        break
    if counter <= 3000:
        print(data.decode())
mysock.close()
print(counter)
