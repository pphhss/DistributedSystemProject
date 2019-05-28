import sys
sys.path.insert(0,'../../')
from ds.db import data as db_data
from ds.node import nodeList,data
from ds.interaction import send

def insert(_key,_value):
    res = db_data.insertData(_key,_value)
    return res

def primary():
   pass
    
def participate(_sourceIp,_test):
    ips = []
    for our_node in nodeList.NodeList.getNodeList():
        ips.append(our_node.getIp())
    res = send.SendManager.sendAddParticipant(_sourceIp)
    if not _test is None:
        _test["success"] = res["success"]
        _test["fail"] = res["fail"]
    
    nodeList.NodeList.insertNode(_sourceIp) # 새로운 노드 리스트에 추가
    return ips

def addParticipant(_sourceIp):
    nodeList.NodeList.insertNode(_sourceIp)
    return 1
        
