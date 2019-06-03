import sys
sys.path.insert(0,'../')
from ds.interaction import listen, externalListen, externalListenLocalWrite
from ds.node import participate
from ds import ip,config
def main():
    print("Server Start")
    listen.Listen().start()

    if config.mode == config.REMOTEWRITE:
        externalListen.Listen().start()
    else:
        externalListenLocalWrite.Listen().start()
    
    if ip.isNotLeader():
        participate.participate()


if __name__ == '__main__':
    main()