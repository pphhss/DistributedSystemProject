import sys
sys.path.insert(0,"../")

from ds import ip

ip = ip.ip
listenPort = 8888
numNode = 4
listenOutPort = 8887

REMOTEWRITE=0
LOCALWRITE=1

mode = LOCALWRITE

db={
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'root',
    'db' : 'ds',
    'charset' : 'utf8'
        }
