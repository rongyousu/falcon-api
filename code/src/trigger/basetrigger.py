#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Trigger Defination

File: basetrigger.py
Author: 
Date: 2017/05/05 19:13
"""

from src.systemlog import accesslog

from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog


class BaseTrigger(object):

          def __init__(self):
               # init log
               self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
               self.errorlogger = syserrorlog.SysErrorLog(__file__)
             
               self.dbmanager = None
               self.cfgmanager = None
               self.req = None
               self.accessDictModel = None

          def load_dic(self,dbmanager,cfgmanager,req,accessDictModel):
               self.dbmanager = dbmanager
               self.cfgmanager = cfgmanager
               self.req = req
               self.accessDictModel = accessDictModel

   
