#!/usr/bin/python
#auther: chenye

import os,sys
import subprocess,cmd

def subping():
    f = open("ip_list.txt","r")
    fout = open("tong.txt","a+")
    lines = f.readlines()
    for line in lines:
        # print(line)
        ret = os.popen("ping -c 2 -w 2 %s" % line).read()
        if "ttl" in ret:
            print("\033[32m[+]"+line+"\033[0m")
            fout.write(line+"\n")
        else:
            print("\033[31m[-]"+line+"\033[0m")
    f.close()
    fout.close()
subping()
