import socket
import config
import threading



class Listen(threading.Thread):
    def __init__(self,parent=None):
       self.parent = parent
       super(Listen,self).__init__()
       self.isContinue = True


    def run(self,port=None):
        if port is None:
            port = config.listenPort
        host = ''

        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind((host,port))
        self.socket.listen(config.numNode)
        while self.isContinue:
            conn, addr = self.socket.accept()
            msg = conn.recv(1024)
            print(f'{msg.decode()}')
            conn.sendall(msg)
            conn.close()
            self.parent and self.parent.on_thread_finish()

    def stop(self):
        self.isContinue= False
        self.socket.close()

if __name__ == '__main__':
    listen = Listen()
    listen.start()
