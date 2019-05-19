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
        cls.__nodeList.clear()

    @classmethod
    def getNode(cls,_idx):
        for n in cls.__nodeList:
            if n.getIdx() == _idx:
                return n
        return None

    

