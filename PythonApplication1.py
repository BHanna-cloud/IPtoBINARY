from ast import Str
from ctypes.wintypes import INT
from pickle import BINBYTES
import socket
from sqlite3 import Binary
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)

# Convert IP to Binary

X1 = int(input('Enter 1st Octet of IPv4 address: '))
X2 = int(input('Enter 2nd Octet of IPv4 address: '))
X3 = int(input('Enter 3rd Octet of IPv4 address: '))
X4 = int(input('Enter 4th Octet of IPv4 address: '))

print ("The Binary is: ", bin(X1)[2:],'.',bin(X2)[2:],'.',bin(X3)[2:],'.',bin(X4)[2:])

