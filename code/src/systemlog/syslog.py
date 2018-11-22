#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
base log

File: syslog.py
Author:
Date: 2017/05/08 16:2
"""


import os
import logging
import logging.config

from src.schemas import defines
from src.util  import jsonmanager

class SysLog():
    __info_dict = None
    
    def __init__(self,filename,name,conf='././config/log.conf'):
       
        logging.config.fileConfig('././config/log.conf') 
        self.name=name
        self.filename=filename
        self.logging=logging.getLogger(self.name)

        self.__info_dict = {}

    def __del__(self):
        if self.__info_dict is not None:
            self.__info_dict.clear()

    @property
    def logger(self):
        return self.logging

    def info(self,message):
        self.logging.info(message)
   
    def error(self,message):
        self.logging.error(message)

    def debug(self,message):
        self.logging.debug(message)
            
    def warning(self,message):
        self.logging.warning(message)

    def push_info(self, info_key, info_value):
        if info_key in self.__info_dict:
            self.warning("key[%s] already exist in log" %(info_key))
            return defines.ReturnCode.FAIL

        self.__info_dict[info_key] = info_value

    def print_info(self):
        self.logging.info(str(self.filename) + ':' + str(self.__info_dict))

    def object_info(self,message):
        json_str=jsonmanager.get_message(message)
        self.info(json_str)

    def object_debug(self,message):
        json_str=jsonmanager.get_message(message)
        self.debug(json_str)

    def object_warning(self,message):
        json_str=jsonmanager.get_message(message)
        self.warning(json_str)
 
    def object_error(self,message):
        json_str=jsonmanager.get_message(message)
        self.error(json_str)

