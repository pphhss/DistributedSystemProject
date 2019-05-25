import sys
sys.path.insert(0,'../../')

from ds.interaction import send
from ds import ip
from ds.node import nodeList

def participate():
    nodeList.NodeList.insertNode(ip.leaerIp)
    res = send.SendManager.sendParticipate()
    new_ips = res["data"]

    for new_ip in new_ips:
        nodeList.NodeList.insertNode(new_ip)
    print("participating success")
    return 1
