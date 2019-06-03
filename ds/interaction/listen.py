import socket
import sys
import threading
import json

sys.path.insert(0, '../../')
from ds.operation import operation,remoteWrite,localWrite
from ds import config

class Listen(threading.Thread):
    def __init__(self, parent=None):
        self.parent = parent
        super(Listen, self).__init__()
        self.isContinue = True

    def run(self, port=None):
        if port is None:
            port = config.listenPort
        host = ''

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(config.numNode)
        print("Server Socket Listen")
        while self.isContinue:
            conn, addr = self.socket.accept()
            communication = Communication(conn)
            communication.start()
            self.parent and self.parent.on_thread_finish()

    def stop(self):
        self.isContinue = False
        self.socket.close()



class Communication(threading.Thread):
    def __init__(self,_conn):
        super(Communication, self).__init__()
        self.conn=_conn

    def run(self):
        msg = self.conn.recv(1024)
        print("IN : ",f'{msg.decode()}')
        message = json.loads(msg.decode())
        result = self.operationMessage(message)
        res = {}
        if self.checkParticipate(result):
            res["data"] = result
            res["result"] = 1
        else:
            res["result"] = result
        res["source"] = config.ip
        print("OUT : ",res)
        self.conn.sendall(json.dumps(res).encode())
        self.conn.close()

    def operationMessage(self, _message):
        """
        operate function by opcode in message

        if operation success , return 1;
        if operation fail, return -1;
        if operation not exist, return 0;
        """
        if _message["opcode"] == "insert":
            res = operation.insert(_message["key"], _message["value"])
            if not (res is None):
                return 1
            else:
                return -1

        elif _message['opcode'] == 'primary':
            res = remoteWrite.primary(_message['source'], _message['key'], _message['value'])
            if not (res is None):
                return 1
            else:
                return -1

        elif _message['opcode'] == 'participate':
            print(_message['source']," wants to participate")
            res = operation.participate(_message['source'],None)
            return res

        elif _message['opcode'] == 'addParticipant':
            res = operation.addParticipant(_message['participant'])
            if not (res is None):
                return 1
            else:
                return -1
        
        elif _message['opcode'] == 'update':
            res = remoteWrite.update(_message['key'],_message['value'])
            if not (res is None):
                return 1
            else:
                return -1
        
        elif _message['opcode'] == 'primaryUpdate':
            res = remoteWrite.primaryUpdate(_message['key'],_message['value'])
            if not (res is None):
                return 1
            else:
                return -1

        elif _message['opcode'] == 'updateLocalWrite':
            res = localWrite.update(_message['key'],_message['value'],_message['version'])
            if not (res is None):
                return 1
            else:
                return -1
        
        elif _message['opcode'] == 'NewUpdateLocalWrite':
            res = localWrite.updatePrimary(_message['key'],_message['value'],_message['version'],_message['source'])
            if not (res is None):
                return 1
            else:
                return -1

        return 0

    def checkParticipate(self, _result):
        if not _result in [-1, 0, 1]:
            return True
        else:
            return False



if __name__ == '__main__':
    listen = Listen()
    listen.start()
