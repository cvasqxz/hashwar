from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as s:
	s.bind(('', 8888))
	s.listen(1)
	conn, addr = s.accept()
	with conn:
		print('> Connection accepted (%s)' % addr[0])
		while True:
			data = conn.recv(1024)
			print("\t* DATA: %s" % data.decode().strip())
			if not data: break
			conn.sendall(data)
	print("> Connection ended (%s)" % addr[0])
	s.close()
