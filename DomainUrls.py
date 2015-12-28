# encoding: UTF-8
import re
import time
import urllib2
import hashlib
import base64
import string
import sys
import socket
import os
import urlparse
import httplib
import datetime
import re
from optparse import OptionParser

def getUrlRespHtml(url):
    respHtml=''
    try:
        heads = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset':'GB2312,utf-8;q=0.7,*;q=0.7',
                'Accept-Language':'zh-cn,zh;q=0.5',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Keep-Alive':'115',
                'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.14) Gecko/20110221 Ubuntu/10.10 (maverick) Firefox/3.6.14'}

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(opener)
        req = urllib2.Request(url)
        opener.addheaders = heads.items()
        respHtml = opener.open(req).read()
    except Exception:
        pass
    return respHtml


def logfile(log,logfile):
    f=open(logfile,'a')
    f.write(log+"\n")
    f.close

def getbiying(domain,ip):
    urlfile=".pan.txt"
    respHtml=getUrlRespHtml("http://www.bing.com/search?q=ip:'+ip+'&count=50")
    match = re.findall(r'<li class=\"b_algo\"><h2><a href=\"(.*?)\"', respHtml)
    if  os.path.exists(os.getcwd()+"/"+domain+urlfile):
        for val in match:
             logfile(ip+"  "+val,domain+urlfile)
    else:
        fwfile(domain+urlfile)





def readfile(log):
    listdoamin=[]
    fd = file(log, "r" )
    for line in fd.readlines():
        line=line.strip()
        listdoamin.append(line)
    fd.close()
    return listdoamin

def fwfile(filname):
    fd = open(filname ,"a" )
    fd.close()

def getip(domain):
    ip=""
    try:
        ip=socket.gethostbyname(domain)
    except Exception:
        pass
    return ip

#getbiying(domain,ip)
def main():
    print "\n****************************************************"
    print "Title:DomainUrls"
    print "Author:mOon"
    print "Team:mOon Securite Team"
    print "Blog:www.moonsec.com"
    print "Version 1.0"
    print "*****************************************************"
    parser = OptionParser('usage: %prog [options] target.com')
    parser.add_option('-f', '--file', dest='names_file', default='host.txt',type='string', help='Dict file used to brute urldomain')
    parser.add_option('-o', '--output', dest='output', default=None, type='string', help='Output file name. default is {target}.txt')
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)
    getdoamin(options.names_file,options.output,args[0])







def getdoamin(name_file,name_out,domain):
    fd = file( "host.txt", "r" )
    httpurl=[]
    for line in fd.readlines():
        html=getUrlRespHtml(line)
        preg= r"(http://\w+.%s)" %domain
        match=re.findall(preg,html)
        url=list(set(match))
        for i in url:
            print i
            httpurl.append(i)
    myurl=list(set(httpurl))
    if len(myurl)> 1:
        for x in myurl:
            x=string.replace(x,"https://","")
            x=string.replace(x,"http://","")
            x=string.replace(x,"/","")
            ip=getip(x)
            xip="%s   %s" %(x,ip)
            print xip
            logfile(xip,domain+".txt")







if __name__ == '__main__':
    main()







