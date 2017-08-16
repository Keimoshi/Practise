#!/usr/bin/env  python
#coding:utf8
import getpass
import sys
db = {}

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


cmdDict = {'n':newUser,'o':oldUser}


def main():
    prompt = """
Please input your choice:
(N)ewUser
(O)ldUser
(Q)uit
"""
    while True:
        try:
            choice = raw_input(prompt).strip()[0].lower()
        except(KeyboardInterrupt,EOFError):
            choice = 'q'
        if choice not in 'noq':
            continue
        if choice == 'q':
            break
        cmdDict[choice]()


if __name__ == "__main__":
    main()
