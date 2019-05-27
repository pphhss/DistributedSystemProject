import sys
sys.path.insert(0,'../../')
from ds.node import nodeList
from ds.db import data
from ds.interaction import send

def insert(_key,_value):
    data.insertData(_key,_value)
    nodeList.NodeList.insertMe(_key,0)
    res = send.SendManager.sendPrimaryToAllNode(_key,_value)
    return res
