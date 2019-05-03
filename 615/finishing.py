#coding:utf8
import csv,sys,re

db = {}
whitespace = ' \n\r'

def read_file():
    with open("username.csv",'rb') as f:
        dataLine = f.readlines()
#        global username
        username = {}.fromkeys(dataLine).keys() #去重
        with file("user.csv","wb") as f2:
            f2.writelines(username)
            f2.close()
        f.close()

def list_Dict():
    with file('old.csv','rb') as f1:
        reader = csv.reader(f1)
        for i in  f1.readlines():
#        for i,rows in enumerate(reader):
#            if i == 4:
#                print rows
            username = i.split(',')[0].strip("\"\n\r")
            user = re.sub('\n','',username)
            print user




def limits_of_authority():
    f3 = open("user.csv","rb")
    for i in f3.readlines():
       if i not in username:
           print "1"

def load_file_from_dict(filepath):
    with open(filepath,'r') as dict_file:
        for line in dict_file:
            (key,value) = line.strip().split(',')
            db[key] = value
    return db
if __name__ =="__main__" :
#    load_file_from_dict("old.csv")
    list_Dict()
#    read_file()
#    limits_of_authority()



