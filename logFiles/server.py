# python
import socket

host = "127.0.0.1"  # Server address
port = 12345  # Port of Server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  # bind server
s.listen(2)

senha = 10

while True:
    conn, addr = s.accept()
    # print(addr, "Now Connected")
    # conn.send("Thank you for connecting")
    # conn.send(str(senha))
    conn.send(str(senha))
    print(conn.recv(1024))
    conn.close()
    senha += 1
