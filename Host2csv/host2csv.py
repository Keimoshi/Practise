#/usr/bin/python
#-*-encoding:utf-8-*-
import csv,os

filepath = raw_input('Please input your filename:')

#判断是否存在文件，如果存在的话。清空内容
if os.path.exists("Newhost.csv"):
    f1 = open('Newhost.csv', 'w')
    f1.close()


#将源文件读取每行,对每个表格内的内容都加入"""括起来，达到要求
def main():
    reader = csv.reader(file(filepath,'rb'))
    for lines in reader:
        IP = "\"%s\"" % lines[0]
        Hostname = "\"%s\"" % lines[1]
        HostType = "\"%s\"" % lines[2]
        Listing = "\"%s\"" % lines[3]
#        print "%s%s%s"%(IP,Hostname,HostType)
        write_file(IP, Hostname, HostType,Listing)


def write_file(IP,Hostname,HostType,Listing):
        with file('Newhost.csv', 'ab') as f2:
            data = csv.writer(f2, dialect='excel')
            data.writerow([IP, Hostname, HostType, Listing])


if __name__ == '__main__':
    main()
