#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests



class Spider:

    def get(self,Pgnum):
        
        f=open('Comment.txt','w')
        for page in range(Pgnum):


            page=str(page)        
            url='http://sclub.jd.com/productpage/p-1302677-s-3-t-3-p-'+page+'.html'

            headers={

                'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36',
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Language':'zh-CN,zh;q=0.8',
                'Accept-Encoding':'gzip, deflate, sdch',
                'Connection':'keep-alive',
                'X-Requested-With':'XMLHttpRequest',
            
            }

            
            res=requests.get(url)        
            
            comment_div=res.json()['comments']

            for each in comment_div:
                
                com=each['content']+'\n'
                f.write(com)
            print ('完成了'+page+'页')


jd=Spider()
jd.get(2000)
