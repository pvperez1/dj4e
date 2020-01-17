import socket

# make a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
mysock.connect(('data.pr4e.org',80))
# this is the command that will be sent to the server
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()
# send the command
mysock.send(cmd)

# while the server is still responding
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
