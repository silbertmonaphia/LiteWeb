#! /usr/bin/env python3
# encoding:utf-8

from pymongo import MongoClient
from pprint import pprint
import json

class User(object):
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.user_name=user_name


class Register(object):

    def __init__(self):
        client=MongoClient('localhost',27017)
        db=client.userdb
        self.userinfo=db.userinfo
        
    def register(self,reg_username,reg_password):
        reg_info={"username":reg_username,"password":reg_password}
        reg_info=json.dumps(reg_info)
        self.userinfo.insert(reg_info)


