from . import data

class Node():
    
    def __init__(self,_idx,_ip):
        self.__idx = _idx
        self.__ip = _ip
        self.__dataList = []

    def getIdx(self):
        return self.__idx

    def getIp(self):
        return self.__ip

    def setIdx(self,_idx):
        self.__idx = _idx

    def setIp(self,_ip):
        self.__ip = _ip
    
    def addData(self,_data):
        self.__dataList.append(_data)

    def getData(self,_key):
        
        for data in self.__dataList:
            if data.getKey() == _key:
                return data
        return None

    def deleteData(self,_key):
        for idx in range(len(self.__dataList)):
            data = self.__dataList[idx]
            if data.getKey() == _key:
                del self.__dataList[idx]
                return
        
