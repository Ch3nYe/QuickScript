#!/usr/bin python
#-*-coding:utf-8-*-

f = open("ip_list.txt","a+")

for i in range(0,255):

	f.write('192.168.'+str(i)+'.1\n')

	f.write('192.168.'+str(i)+'.2\n')

	f.write('192.168.'+str(i)+'.100\n')
