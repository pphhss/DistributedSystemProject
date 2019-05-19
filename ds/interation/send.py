import socket
import json

def send(message):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 8888))
    a={}
    a['message']=message
    
    s.sendall(json.dumps(a).encode())
    resp = s.recv(1024)
    print(f'>{resp.decode()}')

if __name__ == '__main__':
    send("hell")
