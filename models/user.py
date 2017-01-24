#! /usr/bin/env python3
# encoding:utf-8

from pymongo import MongoClient
from pprint import pprint
import json

class User(object):
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name


class loginRegister(object):

    def __init__(self):
        conn=MongoClient('192.168.1.106',27017)
        db=conn.local
        self.userinfo=db.user
        
    def register(self,reg_username,reg_password):
        reg_info={"username":reg_username,"password":reg_password}
        self.userinfo.insert(reg_info)

    def query(self,log_username,log_password):
        log_info={"username":log_username,"password":log_password}
        res=list(self.userinfo.find(log_info))
        print (res)
        if len(res)==0:
            return False
        else: 
            return True
            
