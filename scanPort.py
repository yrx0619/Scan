#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import os
import threading
import time

mutex = threading.Lock()

def portScanner(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        #print('[+]%s %d open' % (host,port))
        s.close()
    except:
        #pass
        mutex.acquire()
        print('[-]%s %d close' % (host,port))
        mutex.release()

def ReadFile(filename):
    text=open(filename)

    line = text.readlines()

    text.close()
    return line

def Scanner(iplist):
    #print port
    #portScanner("10.16.12.52", port)
    for ipportlist in iplist:
        ipportlist = ipportlist.strip('\r\n')
        ip, portlist = ipportlist.split(':',1)
        portlist = portlist.split(',')
        for port in portlist:
            portScanner(ip, int(port)) 


def create_thread():
    Ipcontext = ReadFile('C:\Users\yeruoxi\Desktop\\txt\ipportlist.txt')

    #print Ipcontext


    #portlist = [9527,22,8360]
    #iplist = ['10.186.123.67','10.186.123.69']
    ip_count = len(Ipcontext)

    #print ip_count

    iplist = []

    for i in range(0, ip_count , 1):
        iplist.append(Ipcontext[i:i+1])



    setdefaulttimeout(1)

    #var = ['10.186.123.67','10.186.123.69']

    threads = []
    print len(iplist)
    for t in range(0,len(iplist)):
        threads.append(threading.Thread(target=Scanner, args=(iplist[t],)))

    return threads

def run_theads(threads):
    for t in threads:
        #print t
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

def Scanner_no_thread():
    Ipcontext = ReadFile('C:\Users\yeruoxi\Desktop\\txt\ipportlist.txt')
    Scanner(Ipcontext)


if __name__ == '__main__':
    print time.ctime()
    threads = create_thread()
    run_theads(threads)
    print time.ctime()
    #Scanner_no_thread()
    #print time.ctime()


