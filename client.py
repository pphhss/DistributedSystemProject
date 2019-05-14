import socket
import json

def run():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('15.164.97.72', 8888))
    a={}
    a['hello']=1
    
    s.sendall(json.dumps(a).encode())
    resp = s.recv(1024)
    print(f'>{resp.decode()}')

if __name__ == '__main__':
  run()
