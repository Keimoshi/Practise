#!/usr/bin/env  python
#coding:utf8
import getpass
import sys
import os


def load_file_from_dict(filepath):
    with open(filepath,'r') as dict_file:
        for line in dict_file:
            (key,value) = line.strip().split(',')
            db[key] = value
    return db

def save_file_as_dict():
    try:
        with open(filepath,'w') as dict_file:
            for (key,value) in db.items():
                dict_file.write('%s,%s\n' % (key,value))
    except(KeyboardInterrupt,EOFError):
        print "文件 %s 保存失败" % filepath
        


def newUser():
    try:
        username = raw_input('Please enter your Username:')
        if username  in db:
            print "%s already exists " % username
        password1 = getpass.getpass('Please enter your password:')
        password2 = getpass.getpass('Retry your password:')
    except(KeyboardInterrupt,EOFError):
        sys.exit()
    if password1 != password2:
        print 'The paaswords not match!'
    else:
        db[username] = password1
    save_file_as_dict()

def oldUser():
    try:
        username = raw_input("Username:")
        if username not in db:
            print "Login failed! The user not in db !"
            return()
        password = getpass.getpass("Password:")
    except(KeyboardInterrupt,EOFError):
        sys.exit()
    if db.get(username) == password:
        print "Login successful!"
    else:
            print "Login failed!The password is incorrect!"


cmdDict = {'n':newUser,'o':oldUser,'s':save_file_as_dict,'r':load_file_from_dict}


def main():
    prompt = """
Please input your choice:
(N)ewUser
(O)ldUser
(S)avefile
(R)eadfile
(Q)uit
"""
    while True:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except(KeyboardInterrupt,EOFError):
            sys.exit()
        if choice not in 'noqsr':
            continue
        if choice == 'q':
            break
        cmdDict[choice]()

db = {}
filepath = raw_input("The file path :")
if os.path.exists(filepath):
    load_file_from_dict(filepath)
else:
    print "文件  %s 不存在, 现在即将创建 %s "   % (filepath,filepath)
    os.mknod(filepath)


if __name__ == "__main__":
    main()
