#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Trigger Defination

File: dmp_trigger.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 19:13
"""
from src.systemlog import sysmanagerlog
from src.systemlog import syserrorlog


class Trigger(object):
    """
    base trigger class
    """
 

    def __init__(self):
        """
        do init
        """
        #print 'base trigger'
        self.access_dict_model = None
        self.dmp_request = None
        self.config_manager = None
        self.dict_manager = None
        self.feature_set = None

        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)

    def load_dict(self,dict_manager,config_manager,request,access_dict_model):
        self.dict_manager = dict_manager 

        self.config_manager = config_manager

        self.dmp_request = request

        self.access_dict_model = access_dict_model

        self.managerlogger.logger.info("trigger load dict success")
    def trigger(self):
        """
        Main API
        trigger features
        """
        pass
