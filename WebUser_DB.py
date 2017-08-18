#!/usr/bin/env python
#coding:utf-8
import os
import sys


def Write_Data_To_file():
    Create_file(filepath)
    with open(filepath,'w') as tempdata:
        for (key , value) in db.items():
            tempdata.write( '%s,%s \n'%(key,value))


def load_data_from_file():
    with open(filepath,'r') as tempdata:
        for line in tempdata:
            (key,value1,value2) = line.strip().split(',')
            db[key] = [value1,value2]
        print db
        return db

def Enter_Data():
    try:
        key = raw_input("Web url:")
        value1 = raw_input("Username :")
        value2 = raw_input("password: ")
    except(KeyboardInterrupt,EOFError):
        print "The Data Upload failed !"
        sys.exit()
#    db[key] = [value1,value2]
    Write_Data_To_file()
#    return db



def Read_Data():
    load_data_from_file()
    try:
        url = raw_input("Url :")
        print db[url]
    except(KeyError,KeyboardInterrupt,EOFError):
        print "No this url"

def Create_file(filepath):
    if os.path.exists(filepath):
        print "%s already created ! " % filepath
    else:
        os.mknod(filepath)

    
db = {}
CmdDict = {'1':Enter_Data,'2':Read_Data}
filepath = raw_input("The filepath: ")

def main():
    prompt =  """Choose Your choise:
1.Enter the new data
2.Find the data 
3.Quit
"""
    while True:
        try:
            choice = raw_input(prompt).strip()[0].lower()
            if choice not in '1,2,3':
                continue
            if choice == '3':
                sys.exit()
            CmdDict[choice]()
        except(KeyboardInterrupt,EOFError):
            print "The choose over . Quit"
            sys.exit()



if __name__ == "__main__":
    main()
