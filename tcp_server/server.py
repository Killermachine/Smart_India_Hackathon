import socket
import threading
import time

class ThreadedServer(object):
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.send = False
		self.receive = False
		self.received_data = None
		self.transmission_data = None
		self.EOF = "ENDOFPACKET\n"
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind((self.host, self.port))

	def communicate(self):
		self.sock.listen(5)
		while True:
			client, address = self.sock.accept()
			client.settimeout(60)
			threading.Thread(target = self._listen_to_client,args = (client,address)).start()
			threading.Thread(target = self._send_to_client,args = (client,address)).start()
			threading.Thread(target = self._commands).start()

	def _show_received_data(self):
		print self.received_data

	def _show_transmismitted_data(self):
		print self.transmission_data

	def _commands(self):
		while True:
			command = 
			pass


	def _send_to_client(self,client,address):
		while True:
			if self.send:
				try:
					self.sock.send(self.transmission_data)
				except:
					client.close()
					return False

	def _listen_to_client(self, client, address):
		size = 2000
		while True:
			if self.receive:
				try:
					self.received_data  = client.recv(size)
					self.received_data = self.received_data.split("ENDOFPACKET\n")[0]
				except:
					client.close()
					return False

port = 8000
t = ThreadedServer('',port)
t.communicate()
print("ho")