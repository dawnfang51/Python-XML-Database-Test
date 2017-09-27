from lxml import etree
import socket
import os
import pickle

def main():
    host = "127.0.0.1"
    port = 1234
    
    FN = raw_input("Enter your first name: ")
    LN = raw_input("Enter your last name: ")
    AD = raw_input("Enter your email address: ")
    UN = raw_input("Enter your user name: ")
    PS = raw_input("Enter your password: ")
    
    userinfo = [FN, LN, AD, UN, PS]
    
    root = etree.Element("root")
    
    for data in userinfo:
        root.insert(userinfo.index(data), etree.Element(data))
    
    for child in root:
        print child.tag
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(pickle.dumps(userinfo), (host, port))
    
    print "user info sent"
    
    s.close()
    
    

if __name__ == "__main__":
    main()
