import socket
import sys
import threading
sys.path.insert(0,'../../')
from ds import config
import json
from ds.operation import operation
from ds import config


class Listen(threading.Thread):
    def __init__(self,parent=None):
       self.parent = parent
       super(Listen,self).__init__()
       self.isContinue = True


    def run(self,port=None):
        if port is None:
            port = config.listenPort
        host = ''

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))
        self.socket.listen(config.numNode)
        while self.isContinue:
            conn, addr = self.socket.accept()
            msg = conn.recv(1024)
            print(f'{msg.decode()}')
            message = json.loads(msg.decode())
            result = self.operationMessage(message)
            res = {}
            res["result"] =result
            res["source"] = config.ip
            conn.sendall(json.dumps(res).encode())
            conn.close()
            self.parent and self.parent.on_thread_finish()

    def stop(self):
        self.isContinue= False
        self.socket.close()

    def operationMessage(self,_message):
        """
        operate function by opcode in message

        if operation success , return 1;
        if operation fail, return -1;
        if operation not exist, return 0;
        """
        if _message["opcode"] == "insert":
            res = operation.insert(_message["message"])
            if not (res is None):
                return 1
            else:
                return -1
        return 0

if __name__ == '__main__':
    listen = Listen()
    listen.start()