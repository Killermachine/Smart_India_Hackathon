from client import *
import asynchat
import asyncore
import socket
import threading

 
receiver = Receiver()
receiver.start_listening()
#print "buffer " + receiver.buffer
