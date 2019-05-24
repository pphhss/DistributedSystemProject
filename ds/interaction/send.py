import socket
import json
import sys
sys.path.insert(0,'../../')
from ds.node import nodeList
from ds import config


class SendManager():
    __socket=None

    @classmethod
    def sendMessageToNode(cls,_idx,_message):
        mes = {}
        mes["message"]=_message
        res = send(_idx,mes)
        return res

    @classmethod
    def sendOperationToNode(cls,_idx,_opcode,_key,_value):
        mes={}
        mes["opcode"] = _opcode
        mes["key"]  = _key
        mes["value"] = _value
        mes["source"] = config.ip
        res = cls.send(_idx,mes)
        return res

    @classmethod
    def sendPrimaryToAllNode(cls,_key,_value):
        mes = {}
        mes["opcode"] = "primary"
        mes["key"]  = _key
        mes["value"] = _value
        mes["source"] = config.ip
        res = {}
        res["success"] = 0
        res["fail"] = 0
        for node in nodeList.NodeList.getNodeList():
            result = cls.send(node.getIdx(),mes)
            if result['result'] == 1:
                res['success'] +=1
            else:
                res['fail'] +=1
        return res

    @classmethod
    def sendParticipate(cls):
        mes = {}
        mes["opcode"] = "participate"
        mes["source"] = config.ip

        res = cls.send(0,mes)

        return res

    @classmethod
    def send(cls,_idx,_mes):
        targetNode = nodeList.NodeList.getNode(_idx)
        resp = None
        with cls.getSocket() as s:
            s.connect((targetNode.getIp(),config.listenPort))
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
