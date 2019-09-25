#!/usr/bin/python
#auther: chenye
# read ip list file and ping 
import os,sys
import subprocess,cmd

def subping():
    f = open("ip_list.txt","r")

    lines = f.readlines()
    for line in lines:
        # print(line)
        ret = os.popen("ping -c 2 -w 5 %s" % line).read()
        if "ttl" in ret:
            print("\033[32m[+]"+line+"\033[0m")
        else:
            print("\033[31m[-]"+line+"\033[0m")
    f.close()

subping()
