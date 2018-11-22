#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
user level config manager file

File: configmanager.py
Author:
Date: 2017/05/08 16:28
"""
import ConfigParser

from src.systemlog  import sysmanagerlog
from src.systemlog  import syserrorlog


class ConfigManager():

    
    def __init__(self, configfile):
        self.configfile=configfile      
        self.managerlogger=sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger=syserrorlog.SysErrorLog(__file__)
        self.configP=self.init_config(self.configfile,self.managerlogger)

   
    def init_config(self,configfile,logger):
            self.managerlogger.logger.info('Start innit the config.....')                  

            conf=ConfigParser.ConfigParser()
            conf.read(configfile)
       
            self.managerlogger.logger.info('End init the config.....')
          
            return conf


    def get_key(self,group,key):
                
        return self.configP.get(group,key)
      
    def get_keys(self,group):
      
        return self.configP.items(group)

    def get_float(self,section, option):

        return self.configP.getfloat(section, option)

    def has_option(self, section, option):
        
        return self.configP.has_option(section, option)
    
    
    def __iter__(self):
        for section in self.configP.sections():
            yield section
