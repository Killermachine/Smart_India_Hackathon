
import asynchat
import asyncore
import socket
import threading
 
class ChatClientSender(asynchat.async_chat): 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator('\n')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        pass
 
    def found_terminator(self):
        pass

class ChatClientReceiver(asynchat.async_chat): 
    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
 
        self.set_terminator('\n')
        self.buffer = []
 
    def collect_incoming_data(self, data):
        self.buffer.append(data)
 
    def found_terminator(self):
        msg = ''.join(self.buffer)
        print 'Received:', msg
        self.buffer = []


class Sender(asynchat.async_chat):
    def __init__(self):
        self.client = ChatClientSender("localhost", 5051)
        self.comm = threading.Thread(target=asyncore.loop)
        self.comm.daemon = True
        self.comm.start()

    def send_message(self,msg):
        self.client.push(msg+ '\n')

class Receiver(asynchat.async_chat):
    def __init__(self):
        self.client = ChatClientReceiver('localhost', 5051)
    
    def start_listening(self):
        asyncore.loop()

