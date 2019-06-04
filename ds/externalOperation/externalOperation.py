import sys
sys.path.insert(0,'../../')
from ds.node import nodeList
from ds.db import data
from ds.interaction import send
from ds.operation import remoteWrite,localWrite
from ds import config

def insert(_key,_value):
    if config.mode == config.REMOTEWRITE:
        data.insertData(_key,_value)
        nodeList.NodeList.insertMe(_key,0)
        res = send.SendManager.sendPrimaryToAllNode(_key,_value)
        return res
    elif config.mode == config.BASIC:
        data.insertData(_key,_value)
        res = {}
        res["fail"] = 0
        return res
        
def update(_key,_value):
    res = {}
    res["success"] = 0
    res["fail"] = 0
    
    if config.mode == config.REMOTEWRITE:
        if nodeList.NodeList.isMe(_key) :
            remoteWrite.primaryUpdate(_key,_value)
        else:
            res = send.SendManager.sendUpdateToPrimary(_key,_value)
        return res

    elif config.mode == config.BASIC:
        res = data.updateValue(_key,_value)
        return 1

    '''   
    elif config.mode == config.LOCALWRITE:
        if nodeList.NodeList.isMe(_key):
            localWrite.primaryUpdate(_key,_value)
        else:
            localWrite.primaryNewUpdate(_key,_value)
    '''

def read(_key):
    result = data.getDataFromKey(_key)
    return result["v"]

