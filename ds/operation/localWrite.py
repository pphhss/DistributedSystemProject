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

def update(_key,_value,_version):
    nodeList.NodeList.updateVersion(_key,_version)
    res = db_data.updateValue(_key,_value)
    return res

def updatePrimary(_key,_value,_version,_sourceIp):
    nodeList.NodeList.updateNewPrimary(_key,_version,_sourceIp)
    res = db_data.updateValue(_key,_value)
    return res

def primaryUpdate(_key,_value):
    version = nodeList.NodeList.getVersionInMe(_key)
    version += 1
    res = send.SendManager.sendUpdateToAllNodeLocalWrite(_key,_value,version)
    update(_key,_value,version)
    return res

def primaryNewUpdate(_key,_value):
    version = nodeList.NodeList.getVersionInOtherNode(_key)
    version +=1
    res = send.SendManager.sendNewUpdateToAllNodeLocalWrite(_key,_value,version)

