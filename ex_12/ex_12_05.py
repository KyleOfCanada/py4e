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

doubleLine = False
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    data = data.decode()
    if doubleLine:
        print(data)
    else:
        startPos = re.search('\r\n\r\n', data)
        if startPos:
            doubleLine = True
            print(data[startPos.end():])
mysock.close()
