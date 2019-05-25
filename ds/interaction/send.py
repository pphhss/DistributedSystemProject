from ds import config
from ds.node import nodeList
import socket
import json
import sys
sys.path.insert(0, '../../')


class SendManager():
    __socket = None

    @classmethod
    def sendMessageToNode(cls, _idx, _message):
        mes = {}
        mes["message"] = _message
        res = cls.send(_idx, mes)
        return res

    @classmethod
    def sendOperationToNode(cls, _idx, _opcode, _key, _value):
        mes = {}
        mes["opcode"] = _opcode
        mes["key"] = _key
        mes["value"] = _value
        mes["source"] = config.ip
        res = cls.send(_idx, mes)
        return res

    @classmethod
    def sendPrimaryToAllNode(cls, _key, _value):
        mes = {}
        mes["opcode"] = "primary"
        mes["key"] = _key
        mes["value"] = _value
        mes["source"] = config.ip
        res = {}
        res["success"] = 0
        res["fail"] = 0
        for node in nodeList.NodeList.getNodeList():
            result = cls.send(node.getIdx(), mes)
            if result['result'] == 1:
                res['success'] += 1
            else:
                res['fail'] += 1
        return res

    @classmethod
    def sendParticipate(cls): # 이것은 리더노드가 받는 것임.
        mes = {}
        mes["opcode"] = "participate"
        mes["source"] = config.ip

        res = cls.send(0, mes)

        return res

    @classmethod
    def sendAddParticipant(cls, _sourceIp): # 이것은 leaderNode가 보내는 것
        mes = {} #message to send to our node
        mes["opcode"] = "addParticipant"
        mes["participant"] = _sourceIp
        mes["source"] = config.ip

        ret = {} # object for return value
        ret["success"] = 0
        ret["fail"] = 0

        # send addParticipant message to all node
        for our_node in nodeList.NodeList.getNodeList():
            res = cls.send(our_node.getIdx(), mes)
            if res["result"] == 1:
                ret["success"] += 1
            else:
                ret["fail"] += 1
        return ret

    @classmethod
    def send(cls, _idx, _mes):
        targetNode = nodeList.NodeList.getNode(_idx)
        resp = None
        with cls.getSocket() as s:
            s.connect((targetNode.getIp(), config.listenPort))
            s.sendall(json.dumps(_mes).encode())
            resp = s.recv(1024)
        return json.loads(resp.decode())

    @staticmethod
    def getSocket():
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


'''
def send(message):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 8888))
    a={}
    a['message']=message
    
    s.sendall(json.dumps(a).encode())
    resp = s.recv(1024)
    print(f'>{resp.decode()}')
'''
