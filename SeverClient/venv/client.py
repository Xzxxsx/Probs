import socket
import uuid
import select

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostbyname(), 8000))

id=uuid.uuid1()
s.send(uuid.uuid1(id))
pas=s.recv(1024).decode("utf-8")

s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((socket.gethostbyname(), 8001))
s2.send([pas,id,mess].encode('utf-8'))