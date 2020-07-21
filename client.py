import socket
 
host = '10.0.0.251.'
port = 50008
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
print("Connected to "+(host)+" on port "+str(port))
initialMessage = input("Send: ")
change=initialMessage.encode()
s.sendall(change)
 
while True:
 data = s.recv(1024)
 print("Recieved: "+str(data)) #del str
 response = input("Reply: ")
 tom=response.encode()
 if response == "exit":
     break
 s.sendall(tom)
s.close()
