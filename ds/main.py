import sys
sys.path.insert(0,'../')
from ds.interaction import listen
from ds.node import participate
from ds import ip
def main():
    print("Server Start")
    listen.Listen().start()

    if ip.isNotLeader():
        participate.participate()


if __name__ == '__main__':
    main()