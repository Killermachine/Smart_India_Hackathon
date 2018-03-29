from client import *
import asynchat
import asyncore
import socket
import threading
 
sender = Sender()
while True:
	sender.send_message("hi")