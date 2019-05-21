from . import node

class NodeList():
    __nodeList = []
    __idxCount = 0

    @classmethod
    def insertNode(cls,_ip):
        newNode = node.Node(cls.__idxCount,_ip)
        cls.__idxCount += 1

        cls.__nodeList.append(newNode)

    @classmethod
    def len(cls):
        return len(cls.__nodeList)

    @classmethod
    def clear(cls):
        cls.__idxCount = 0
        cls.__nodeList.clear()

    @classmethod
    def getNode(cls,_idx):
        cls.printNodes()
        for n in cls.__nodeList:
            if n.getIdx() == _idx:
                return n
        return None

    @classmethod
    def getNodeByIp(cls,_ip):
        for n in cls.__nodeList:
            if n.getIp() == _ip:
                return n
        return None

    @classmethod 
    def printNodes(cls):
        print("--- printNodes START ---")
        for n in cls.__nodeList:
            print(n.getIdx(),n.getIp())
        print("--- printNodes END ---")
            
