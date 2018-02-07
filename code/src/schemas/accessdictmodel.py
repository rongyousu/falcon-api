#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
访问日志模型封装

File: accessdictmodel.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/10 20:28
"""

import json
import datetime

class AccessDictModel():

    def __init__(self):
        self.acc_Logger_Dict={}

    def format_body(self):
        json_str=json.dumps(self.acc_Logger_Dict,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_str=json_str.replace('\n','').replace('\t','')
        return json_str

    def get_log_dic(self):
         return self.acc_Logger_Dict

    def set_log_dic_key(self,key,value):
         self.acc_Logger_Dict[key]=value
         self.set_log_dic_key_time(key)

    def set_log_dic_key_time(self,key):
         key_time=str(key)+'_time'  
         time_value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
         self.acc_Logger_Dict[key_time]=time_value

    def reset(self):
        if self.acc_Logger_Dict is not None:
            self.acc_Logger_Dict.clear()