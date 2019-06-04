import sys
sys.path.insert(0,'../')
from ds.interaction import listen, externalListen, externalListenLocalWrite
from ds.node import participate
from ds import ip, config
from ds.db import data
def main():

    data.deleteAllData()
    
    print("Server Start")
    listen.Listen().start()


    externalListen.Listen().start()

    
    if ip.isNotLeader():
        participate.participate()


if __name__ == '__main__':
    main()