import socket
host = ''
port = 8080 # declaring variables
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating a socket in order to request or serve information (In this AF_NET is IPv4 socket family and SOCK_STREAM is socket type which is a TCP byte stream)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Setting socket options (Here setsockopt is a method and for socket level option we use SOL_SOCKET. To ensure reuseability of socket we use SO_USEADDR and 1 is the value for which request for socket is known in program)
c.bind((host,port)) #binding port to socket
c.listen(1) # waits and listen on the port
print " SERVER IS UP AND RUNNING"
while 1: #reference request by its value
	csock, caddr= c.accept() # server accepts request
	csock.sendall("""HTTP/1.0 200 OK
Content-Type: text/html
 
<html>
<head>
<title>Success</title>
</head>
<body>
Boo!
</body>
</html>
""")
	csock.close()

