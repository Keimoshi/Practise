#!/bin/python
#coding: utf-8
import paramiko
import csv
import sys

AddUser = raw_input("Please enter Uername_add: ")
#LogServer = "192.168.0.100"
filepath = raw_input("Please enter Your IP list file:")
#filepath = 'IP.csv'

s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())


def init_errlogfile():
    with file('error.csv','w') as f1:
        f1.close()


def Add_User(ip,Username,Pwd):
    try:
        s.connect(hostname = ip , port = 22 , username = Username , password = Pwd,timeout = 5)

        s.exec_command(" adduser  %s " % AddUser )
#        s.exec_command("echo %s| passwd --stdin %s" %(setpasswd,AddUser) )
        s.close()
     
    except paramiko.ssh_exception.AuthenticationException:
        print "The host %s  Authentication failed . " % ip
        with file("error.csv",'ab')  as f2:
            data = csv.writer(f2, dialect='excel')
            data.writerow([ ip , "Authentication failed"])
    except :
        print "The host %s  timeout ,  Please check your network " % ip
        with file("error.csv",'ab')  as f2:
            data = csv.writer(f2, dialect='excel')
            data.writerow([ ip , "Timeout" ])

def Chmod(ip,Username,Pwd,setpasswd):
        s.connect(hostname = ip , port = 22 , username = Username , password = Pwd,timeout = 5)
        s.exec_command("echo %s| passwd --stdin %s" %(setpasswd,AddUser) )
        stdin,stdout,stderr=s.exec_command(" cat /etc/passwd | grep %s " % AddUser )
        userdetail = stdout.read()
        UserId = userdetail.split(':')[2]
        s.exec_command(" sed -i 's/%s/0/' /etc/passwd " % UserId )
#        print type(result)
        print UserId
        print userdetail


def main():
    with open(filepath,'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            ip = line[0]
            Username = line[1]
            Pwd = line[2]
            setpasswd = line[2]
            Add_User(ip,Username,Pwd)
            Chmod(ip,Username,Pwd,setpasswd)
            
if __name__ == "__main__":
    init_errlogfile()
    main()
