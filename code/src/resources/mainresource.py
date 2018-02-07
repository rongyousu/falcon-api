#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""


File: mainresource.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import json
import falcon
import requests
import datetime
import time
import baseresource


from src.trigger import *
from src.display import dmp_display
from src.util import jsonmanager
from src.util import request_to_dmprequest


class Main_Resource(baseresource.BaseResource):
    
 
   
    #@falcon.before(baseresource.validata_app_data)
    def on_post(self,req,resp,app_name):

        self.accessDictModel.reset()
        str_appid = req.get_param('appid')
        str_appkey = req.get_param('appkey')
        #request_id 用户接口请求唯一标识
        request_id= req.context['request_id']
        
        self.accessDictModel.set_log_dic_key('app_id',str_appid)
        self.accessDictModel.set_log_dic_key('app_key',str_appkey)

        self.accessDictModel.set_log_dic_key('request_id',req.context['request_id'])
        self.accessDictModel.set_log_dic_key('app_name',app_name)

        #start time
        start_time_value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.accessDictModel.set_log_dic_key('start_time',str(start_time_value))
        all_start_timestamp= int(round(time.time()*1000))
        self.accessDictModel.set_log_dic_key('all_start_timestamp',str(all_start_timestamp))
        
        result_str=''
        #trigger display区   
        trigger_name=''
        
        #chech the trigger
        self.validata_app_data(app_name)
         
        try:
                 
                 dmp_reqobj= request_to_dmprequest.RequestToDmpRequest(self.accessDictModel)
                 dmp_request=dmp_reqobj.transform_post_request_to_dmprequest(req)
                 #log
                 self.managerlogger.logger.info('request_id: %s  appid: %s  appkey %s  the dmp_request is innit'  %(request_id,str_appid,str_appkey) )           
                 
                 trigger_name=self.triggercfg.get_key('trigger',app_name)
                 
                 self.managerlogger.logger.info('request_id: %s  appid: %s  appkey %s    main_resource get the trigger_name: %s' %(request_id,str_appid,str_appkey,trigger_name)   )              
                 start_trigger= int(round(time.time()*1000))                
 
                 trigger = eval(trigger_name+"()")
                 trigger.load_dict(self.dbmanager,self.managercfg,dmp_request,self.accessDictModel)
       
                 feature_set = trigger.trigger()
                 end_trigger= int(round(time.time()*1000))
                 self.accessDictModel.set_log_dic_key('trigger_diff',str(end_trigger-start_trigger))
                    
                 self.managerlogger.logger.info('request_id: %s  appid: %s  appkey %s  the feature_set  is get ' %(request_id,str_appid,str_appkey) )
        
                 start_display = int(round(time.time()*1000))
                 #display
                 ds=dmp_display.DmpDisplay(self.displaycfg,self.accessDictModel)
                 response_result=ds.display(feature_set,dmp_request)

                 end_display = int(round(time.time()*1000))
                 self.accessDictModel.set_log_dic_key('display_diff',str(end_display-start_display))

                 
                 result_str=jsonmanager.get_message(response_result)
             
        except Exception as e:

                 try:
                       self.managerlogger.logger.error("main_resource: %s trigger: %s  error: %s" %(app_name,trigger_name, str(e)))
                       self.errorlogger.logger.error("main_resource: %s trigger: %s  error: %s" %(app_name,trigger_name, str(e)))
                 except Exception as ee:
                       raise falcon.HTTPBadRequest(
                          'logger error ',
                          'the error message is : %s' %(str(ee))
                       )
                 raise falcon.HTTPBadRequest(
                       'Bad  request',
                       'Please check whether the interface parameter is correct or not.')
         

        resp.set_header('Powered-By', 'xes-api-server')
        resp.status = falcon.HTTP_200
        
        #end time
        end_time_value=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.accessDictModel.set_log_dic_key('end_time',str(end_time_value))
        all_end_timestamp= int(round(time.time()*1000))
        self.accessDictModel.set_log_dic_key('all_end_timestamp',str(all_end_timestamp))

        self.accessDictModel.set_log_dic_key('all_time',str(all_end_timestamp-all_start_timestamp))  

        self.accesslogger.info(self.accessDictModel.format_body())
        resp.body = result_str


    #@falcon.before(baseresource.validata_json_data)
    def on_get(self, req, resp, app_name):
        self.on_post(req,resp,app_name)

