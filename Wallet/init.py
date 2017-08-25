#!/usr/bin/python
#-*- coding: UTF-8 -*-
import cPickle as p
import sys
#定义初始余额

str1 = "请定义你的初始余额："
str2 = str1.decode("UTF-8").encode("GBK")
inital = int(raw_input(str2))


#创建钱包数据文件，并将初始余额记录
with file('money.data','w') as f:
	p.dump(inital,f)



#创建初始记账本
with file('tally.log','w') as f:
	str1 = "时间" ; str2 = "消费/存款" ; str3 = "余额" ;str4 = "备注"
	str1_1 = str1.decode("UTF-8").encode("GBK")
	str2_1 = str2.decode("UTF-8").encode("GBK")
	str3_1 = str3.decode("UTF-8").encode("GBK")
	str4_1 = str4.decode("UTF-8").encode("GBK")
	str5 = "%-20s%-15s%-10s%-40s\n" %(str1_1,str2_1,str3_1,str4_1)
	print str5
	f.write(str5)
	f.close() 



