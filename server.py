import socket
 
host = '10.0.0.251.' #127.0.0.1
port = 50008
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
print("hello starting program")
conn, addr = s.accept()
print ("Connection from", addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print("Recieved: "+str(data))  #del str
    conn.send("I am server")
    response = input("Reply: ")
    jim=response.encode()
    if response == "exit": 
        break
    conn.sendall(jim)
conn.close()
