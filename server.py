import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.42', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
#	print('waitig for a connection')
	connection, client_address = sock.accept()
	
	try:
		print('connection from', client_address)		
		while True:
			data = connection.recv(100)
			if data:
				print(data.decode())
#				print('sending data back to the client')
#				connection.sendall(data)
			else:
				print('no more data from', client_address)
				break
				
	finally:
		connection.close()
		print("closing connection")