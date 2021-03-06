import socket
from Crypto.PublicKey import RSA
from Crypto import Random
import select 
import sys 

random_generator = Random.new().read

key = RSA.generate(1024, random_generator)

my_private_key = key.exportKey()

my_public_key = key.publickey().exportKey()

def setupAsClient():
  
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    IP_address = input("Please insert the disnation IP: ") 
    Port = 444 
    server.connect((IP_address, Port)) 
  
    while True: 
  
        # maintains a list of possible input streams 
        sockets_list = [sys.stdin, server] 
  
        """ There are two possible input situations. Either the 
        user wants to give  manual input to send to other people, 
        or the server is sending a message  to be printed on the 
        screen. Select returns from sockets_list, the stream that 
        is reader for input. So for example, if the server wants 
        to send a message, then the if condition will hold true 
        below.If the user wants to send a message, the else 
        condition will evaluate as true"""
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
        for socks in read_sockets: 
            if socks == server: 
                message = socks.recv(2048) 
                print (str(message)) 
            else: 
                message = sys.stdin.readline() 
                #server.send(message)
                server.sendall(message.encode('utf-8'))
                sys.stdout.write("<You>") 
                sys.stdout.write(message) 
                sys.stdout.flush() 
    server.close()  
setupAsClient()
