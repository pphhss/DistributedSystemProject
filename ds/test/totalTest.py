import unittest
import sys
sys.path.insert(0, '../../')
from ds.interaction import send

def sendMessage(_ip, _mes):
    res = send.SendManager.sendExternal(_ip, _mes)
    if res["result"] == 1:
        print("Update : ", _mes['key']," - ",_mes["value"])
    else:
        print("Read : ", _mes["key"]," - ",res["result"])


def makeMessage(_opcode, _key, _value):
    mes = {}
    mes["opcode"] = _opcode
    mes["key"] = _key
    mes["value"] = _value
    return mes

nodeList = [
    "15.164.166.41"#, "15.164.102.73"#, "15.164.165.83", "13.209.49.42"
]
keys = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
]

values = [
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
]


#초기화
node = 0
for key in keys:
    node = (node+1)%len(nodeList)
    mes = makeMessage("insert",key,"x")
    sendMessage(nodeList[node],mes)

print("---START---")

#update
for value in values:
    for key in keys:
        node = (node+1)%len(nodeList)
        mes = makeMessage("update",key,value)
        sendMessage(nodeList[node],mes)



