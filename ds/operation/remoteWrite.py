import sys
sys.path.insert(0, '../../')
from ds.db import data as db_data
from ds.node import nodeList,data
from ds.interaction import send



def primary(_sourceIp,_key,_value,_testCode=False):
    if _testCode:
        nodeList.NodeList.insertNode(_sourceIp)
    
    nodeList.NodeList.insertDataInNode(_sourceIp,_key) # add data(key,version) to node

    res = db_data.insertData(_key,_value)
    return res

def update(_key,_value):    
    res = db_data.updateValue(_key,_value)
    return res

def primaryUpdate(_key,_value):
    res = send.SendManager.sendUpdateToAllNode(_key,_value)
    update(_key,_value)
    return res

