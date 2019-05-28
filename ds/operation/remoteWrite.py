import sys
sys.path.insert(0, '../../')
from ds.db import data as db_data
from ds.node import nodeList,data
from ds.interaction import send



def primary(_sourceIp,_key,_value,_testCode=False):
    if _testCode:
        nodeList.NodeList.insertNode(_sourceIp)
    node = nodeList.NodeList.getNodeByIp(_sourceIp)
    new_data = data.Data()
    new_data.setKey(_key)
    new_data.setVersion(0)

    node.addData(new_data) # add data(key,version) to node

    res = db_data.insertData(_key,_value)
    return res


