#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
treenode reload model

File: ***.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog

class BaseDBManager():
         
        def __init__(self):
             
             self.dbmanager = None
             self.db_cmd=''
             # init log
             self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
             self.errorlogger = syserrorlog.SysErrorLog(__file__)
             
             self.managerlogger.logger.info('the basemanager innit..')

        def load_dic(self,dbmanager,db_cmd):
             self.dbmanager=dbmanager
             self.db_cmd = db_cmd

        def reload(self):
             right_num=0
             try:
                  right_num=self.dbmanager.reload(self.db_cmd)
             except Exception as e:
                  self.managerlogger.logger.error('the cmd [%s] reload is error:[%s]'  %(self.db_cmd,str(e)) )
                  self.errorlogger.logger.error('the cmd [%s] reload is error:[%s]' %(self.db_cmd,str(e)) )
             self.managerlogger.logger.info('the cmd [%s] done . the right_num [%d]' %(self.db_cmd,int(right_num)) )
             return right_num
             
               
