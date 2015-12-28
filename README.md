# DomainUrls  
****************************************************  
Title:DomainUrls  
Author:mOon  
Team:mOon Securite Team  
Blog:www.moonsec.com  
Version 1.0  
*****************************************************  
Usage: DomainUrls.py [options] target.com  

Options:  
  -h, --help            show this help message and exit  
  -f NAMES_FILE, --file=NAMES_FILE  
                        Dict file used to brute urldomain  
  -o OUTPUT, --output=OUTPUT  
                        Output file name. default is {target}.txt  
  
【1】  脚本主要用来收集子域名。  
【2】  DomainUrls.py 主文件 host.txt 里面存放 要收集的网页。  
【3】  方法：DomainUrls.py qq.com  qq.com   #程序自动递归搜刮有关qq.com的子域名。  

效果： 
host.txt:  
http://imgcache.qq.com  
http://weixin110.qq.com  
http://exp.qq.com  
http://110.qq.com  
http://adver.qq.com  
http://pinghot.qq.com  
http://isdspeed.qq.com  
http://t.qq.com  
http://service.qq.com  
http://i.qq.com  
http://btrace.qq.com  
http://qzs.qq.com  
http://connect.qq.com  
http://support.qq.com  
http://qzone.qq.com  
http://pingfore.qq.com  
http://pingjs.qq.com  
http://www.qq.com  

qq.com.txt:  

service.qq.com   59.37.96.218  
adver.qq.com   183.60.118.89  
aq.qq.com   183.57.48.84  
b.qq.com   183.61.38.179  
connect.qq.com   183.60.38.51  
support.qq.com   123.151.139.114  
pingfore.qq.com   14.17.41.173  
kf.qq.com   59.37.96.218  
110.qq.com   183.57.48.84  
pinghot.qq.com   14.17.41.173  
v.qq.com   183.56.150.150  
btrace.qq.com   183.57.48.67  
www.qq.com   14.17.42.40  
pingjs.qq.com   113.105.73.142  
qzone.qq.com   119.147.33.32  
imgcache.qq.com   183.56.150.149  
weixin110.qq.com   183.61.49.165  
exp.qq.com   180.163.32.150  
open.qq.com   14.17.32.228  
tajs.qq.com   121.14.125.21  
qzs.qq.com   119.147.33.32  
wj.qq.com   180.163.32.150  
isdspeed.qq.com   119.147.194.249  
t.qq.com   113.108.7.237  
i.qq.com   183.61.46.177  
weixin.qq.com   61.151.224.41  
