import socket
import sys
import threading
import json
sys.path.insert(0, '../../')
from ds import config
from ds.externalOperation import externalOperation as exop


class Listen(threading.Thread):
    def __init__(self, parent=None):
        self.parent = parent
        super(Listen, self).__init__()
        self.isContinue = True

    def run(self, port=None):
        if port is None:
            port = config.listenOutPort
        host = ''

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen(config.numNode)
        print("Server External Socket Listen")
        while self.isContinue:
            conn, addr = self.socket.accept()
            msg = conn.recv(1024)
            print(f'{msg.decode()}')
            message = json.loads(msg.decode())

            res = {}
            result = self.operationMessage(message, res)

            res["result"] = result
            res["source"] = config.ip
            conn.sendall(json.dumps(res).encode())
            conn.close()
            self.parent and self.parent.on_thread_finish()

    def stop(self):
        self.isContinue = False
        self.socket.close()

    def operationMessage(self, _message, _res):
        """
        operate function by opcode in message

        if operation success , return 1;
        if operation fail, return -1;
        if operation not exist, return 0;
        """
        if _message["opcode"] == "insert":
            res = exop.insert(_message["key"], _message["value"])
            if res['fail'] == 0:
                return 1
            else:
                return -1

        elif _message['opcode'] == 'select':
            pass
        elif _message['opcode'] == 'update':
            pass
        return 0

    def checkParticipate(self, _result):
        if not _result in [-1, 0, 1]:
            return True
        else:
            return False


if __name__ == '__main__':
    listen = Listen()
    listen.start()
