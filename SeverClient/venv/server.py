import socket
import logging
import uuid

logging.basicConfig(filename="logs", level=logging.DEBUG)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),8000))
s2.bind((socket.gethostname(),8001))
s.listen(50)
s2.listen(50)
uid= {}

while True:
    clientSocket,address=s.accept()
    clientSocket2,adress2=s2.accept()
    client_id=clientSocket.recv(1024).decode('utf-8')
    uid[client_id]=uuid.uuid1()
    clientsocket.send(bytes(uid[client_id]),'utf-8')
    client_info=clientSocket2.recv(1024).decode('utf-8')
    if client_info[0]==uid[client_info[1]]:
        logging.info(f"Connection from {adress}")
    else:
        clientSocket.close()
        clientSocket2.close()