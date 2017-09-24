#!/bin/python
#coding: utf-8
import paramiko
import csv
import sys

LogServer = raw_input("Please enter LogServer IP: ")
#LogServer = "192.168.0.100"
filepath = raw_input("Please enter Your IP list file:")
#filepath = 'IP.csv'


def init_errlogfile():
    with file('error.csv','w') as f1:
        f1.close()


def check_version(ip,Username,Pwd):
    try:
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = ip , port = 22 , username = Username , password = Pwd,timeout = 5)


        stdin,stdout,stderr=s.exec_command(" lsb_release -a | grep -c -e 'Red Hat' -e 'Centos' "  )
        result = int(stdout.read())
#        print type(result)
#        print result
        if result >= 1:
            Centos_RedHat(s,ip)
        else:
            print "Please check your system version is Redhat/Centos ?"          
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






def Centos_RedHat(s,ip):
    stdin,stdout,stderr=s.exec_command("ls /etc | grep -c ^rsyslog.conf$"  )
    result1 =  int(stdout.read())
    stdin,stdout,stderr=s.exec_command("ls /etc | grep -c ^syslog.conf$"  )
    result2 =  int(stdout.read())
#    print type(result)
#    print result
    if result1 >= 1:
#        print "rsyslog"
        s.exec_command(" echo '*.*    @%s' >> /etc/rsyslog.conf " % LogServer )
#        s.exec_command(" date  >> /root/rsyslog.txt"  )
        stdin,stdout,stderr = s.exec_command(" service rsyslog restart "  )
        print stdout.read()
        print "%s rsyslog configuration successful" %ip
    elif result2 >= 1:
        print "syslog"
        s.exec_command(" echo '*.*    @%s' >> /etc/syslog.conf" % LogServer )
#        s.exec_command(" date  >> /root/syslog.txt"  ) 
        stdin,stdout,stderr = s.exec_command(" service syslog restart "  )
        print stdout.read() 
        print "%s syslog configuration successful" %ip
    else:
        print "Don't find rsyslog.conf/syslog.conf. Please check your system version is Redhat/Centos ."
        with file("error.csv",'ab')  as f2:
            data = csv.writer(f2, dialect='excel')
            data.writerow([ ip , "Don't find rsyslog.conf/syslog.conf." ])



def Aix():
    pass


def main():
    with open(filepath,'rb') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            ip = line[0]
            Username = line[1]
            Pwd = line[2]
            check_version(ip,Username,Pwd)
            
if __name__ == "__main__":
    init_errlogfile()
    main()
