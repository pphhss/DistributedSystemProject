from . import node,data


class NodeList():
    __nodeList = [] # our group node's data except me
    __idxCount = 0
    __me = [] # My Node 's data

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
        cls.__me.clear()

    @classmethod
    def getNode(cls,_idx):
        #cls.printNodes()
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
    def getNodeList(cls):
        return cls.__nodeList

    @classmethod
    def getMe(cls):
        return cls.__me

    @classmethod
    def insertMe(cls,_key,_version):
        new_data = data.Data()
        new_data.setKey(_key)
        new_data.setVersion(_version)
        cls.__me.append(new_data)

    @classmethod
    def isMe(cls,_key):
        for me_data in cls.__me:
            if me_data.getKey() == _key:
                return True
        return False

    @classmethod
    def getVersionInOtherNode(cls,_key):
        for n in cls.__nodeList:
            if not (n.getData(_key) is None):
                return n.getData(_key).getVersion()
            
    @classmethod
    def getVersionInMe(cls,_key):
        for me_data in cls.__me:
            if me_data.getKey() == _key:
                return me_data.getVersion()
        return None

    @classmethod
    def updateVersion(cls,_key,_version):
        for me_data in cls.__me:
            if me_data.getKey() == _key:
                me_data.setVersion(_version)

    @classmethod
    def updateNewPrimary(cls,_key,_version,_sourceIp):
        for n in cls.__nodeList:
            if not (n.getData(_key) is None):
                n.deleteData(_key)
        cls.insertDataInNode(_sourceIp,_key,_version)


    
    @classmethod
    def insertDataInNode(cls,_sourceIp,_key,_version=0):
        node = cls.getNodeByIp(_sourceIp)
        new_data = data.Data()
        new_data.setKey(_key)
        new_data.setVersion(_version)
        node.addData(new_data)
        
    @classmethod
    def findPrimary(cls,_key):
        for n in cls.__nodeList:
            if not (n.getData(_key) is None):
                return n
        return None

    @classmethod 
    def printNodes(cls):
        print("--- printNodes START ---")
        for n in cls.__nodeList:
            print(n.getIdx(),n.getIp())
        print("--- printNodes END ---")
            
