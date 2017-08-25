#!/usr/bin/python
#-*- coding: UTF-8 -*-


import sys
import time
import cPickle as p

timer = time.strftime('%Y-%m-%d %H:%M')

def spendMoney():
	str1 = "消费/存款：" ; str2 = "备注："
	str1_1 = str1.decode('UTF-8').encode('GBK')
	str2_1 = str2.decode('UTF-8').encode('GBK')
	UseMoeny = int(raw_input(str1_1))
	comment = raw_input(str2_1)
	with file('money.data','r') as f1:
		balance = p.load(f1) - UseMoeny
		f1.close()

	with file('money.data','w') as f2:
		p.dump(balance,f2)
		f2.close()

	with file('tally.log','a') as f3:
		str3 = "%-20s-%-14s%-10s%-40s\n" %(timer,UseMoeny,balance,comment)
		f3.write(str3)
		f3.close






def saveMoney():
	str1 = "消费/存款：";str2 = "备注："
	str1_1 = str1.decode('UTF-8').encode('GBK')
	str2_1 = str2.decode('UTF-8').encode('GBK')
	saveMoney = int(raw_input(str1_1))
	comment = raw_input(str2_1)
	with file('money.data','r') as f1:
		balance = p.load(f1) + saveMoney
		f1.close()

	with file('money.data','w') as f2:
		p.dump(balance,f2)
		f2.close

	with file('tally.log','a') as f3:
		str3 = "%-20s+%-14s%-10s%-40s\n" %(timer,saveMoney,balance,comment)
		f3.write(str3)
		f3.close()


def queryInfo():
	with file('tally.log','r') as f1:
		for line in f1:
			print line 
	f1.close()
	



def logger():
	pass


CMDs = {'1':spendMoney,'2':saveMoney,'3':queryInfo}


def main():
	prompt = """Choose your choice:
1.Record spend money
2.Record save money
3.Query info
4.Quit
"""
	
	while True:
		choice = raw_input(prompt)
		if choice not in '1 2 3 4':
			print '''Please input 1/2/3/4'''
			continue
		if choice == '4':
			sys.exit()
		CMDs[choice]()


if __name__ == "__main__":
	main()