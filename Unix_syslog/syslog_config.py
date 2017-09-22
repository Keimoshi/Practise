#!/bin/python
import paramiko
import csv
import sys

LogServer = raw_input("Please enter LogServer IP: ")

def Conn(ip,Username,Pwd):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname = ip , port = 22 , username = Username , password = Pwd)
    stdin,stdout,stderr=s.exec_command(" echo '*.*    @%s' >> /root/1.txt" % LogServer )
    stdin,stdout,stderr=s.exec_command("service rsyslog stop"  )
    stdin,stdout,stderr=s.exec_command("service rsyslog start"  )
    print  stdout.read()

def main():
	reader = csv.reader(file("ip.csv",'rb'))
	for lines in reader:
		ip = lines[0]
		Username = lines[1]
		Pwd = lines[2]
#		print ip , pwd
		Conn(ip,Username,Pwd)
if __name__ == "__main__":
    main()
