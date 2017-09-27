from lxml import etree
import socket
import os
import pickle

def main():
    host = "127.0.0.1"
    port = 1234
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    print "waiting to recieve data. \n"
    
    data = s.recv(1024)
    
    userinfo = pickle.loads(data)
    
    root = etree.Element("root")
    
    for data in userinfo:
        root.insert(userinfo.index(data), etree.Element(data))
        
    for child in root:
        print child.tag
    
    print "successfully recieved data"
    
    s.close()
    
if __name__ == "__main__":
    main()
