#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""


File: managerresource.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import json
import falcon
import requests

from src.resources.manager import basemresource
from src.trigger.managertrigger import *

class Manager_Resource(basemresource.BaseManagerResource):
    
 
   
   
    def on_post(self,req,resp,app_name,app_cmd):
       
        #app_name 某种请求需求


        #trigger display区   
        db_nums=0
        try:
             trigger_name=self.triggercfg.get_key('trigger_manager',app_name)

             trigger = eval(trigger_name+"()")
             trigger.load_dic(self.dbmanager,app_cmd)
             db_nums=trigger.reload()
        except Exception as e:
                self.managerlogger.logger.error("trigger: %s cmd: %s  error: %s" %(app_name,app_cmd, str(e)))
                self.errorlogger.logger.error("trigger: %s cmd: %s  error: %s" %(app_name,app_cmd, str(e)) )

        resp.set_header('Powered-By', 'xes-api-server')
        resp.status = falcon.HTTP_200
    
        
        resp.body = self.format_body({
            "app_name":str(app_name),
            "app_cmd": str(app_cmd),
            "db_nums": str(db_nums)
        })


    
    def on_get(self, req, resp, app_name,app_cmd):

         self.on_post(req,resp,app_name,app_cmd)
             
        
   

