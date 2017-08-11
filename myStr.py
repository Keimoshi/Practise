#!/usr/bin/env  python
#coding:utf-8

whitespace = ' \t\n\r\v\f'
MyStr = '    hellon    '

def LmyStrip(char):
    stringlen = len(char)
    if stringlen == 0:
        return char

    for i in range(stringlen):
        if char[i] not in whitespace:
            break
    else:
        return ''
    return char[i:]

def RmyStrip(char):
    stringlen = len(char)
    for i in range(-1,-(stringlen + 1),-1):
        if char[i] not in whitespace:
            break
    else:
        return ''

    return char[:i+1]
    



if __name__ == "__main__":
    print '|' + MyStr + '|'
    print '|' + LmyStrip(MyStr) + '|'
    print '|' + RmyStrip(MyStr) + '|'
