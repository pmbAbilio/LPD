import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345
s.connect((host, port))
# print(s.recv(1024))
senha = s.recv(1024)

# senha = s.recv(1024)
print("A minha senha é: " + str(senha))
s.send("Recebido do client N: ", senha)

s.close()
