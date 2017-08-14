#!/usr/bin/python
#-*-encoding:utf-8-*-
def ip2int(ipadd):
	iplist = ipadd.split('.')
	num =0 
	for i in range(4):
		num += int(iplist[i]) * 256 ** (3-i)
	return num



def int2ip(num):
	iplist = []
	for i in range(3):
		num ,modnum = divmod(num ,256)
		iplist.insert(0,str(modnum))
	iplist.insert(0,str(modnum))
	return '.'.join(iplist)
	
def test():
	ipadd = raw_input('Please input your ipaddress:')
	print ip2int(ipadd)
	num = int(raw_input('Please input your num:'))
	print int2ip(num)
	
if __name__ == '__main__':
	test()