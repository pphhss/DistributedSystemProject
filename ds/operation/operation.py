import sys
sys.path.insert(0,'../../')
from ds.db import data as db_data
from ds.node import nodeList,data

def insert(_key,_value):
    res = db_data.insertData(_key,_value)
    return res

def primary(_sourceIp,_key,_value):
    node = nostList.NodeList.getNodeByIp(_sourceIp)
    new_data = data.Data()
    new_data.setKey(_key)
    new_data.setVersion(0)

    node.addData(new_data) # add data(key,version) to node

    res = db_data.insertData(_key,_value)
    return res
    
def participate(_sourceIp):

    for out_node in nodeList.NodeList.
