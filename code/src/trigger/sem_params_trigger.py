#!/usr/bin/env python
# -*- coding=utf-8 -*-

######################################################
#
#Copyright (c) 2017 ,Inc.All Right Reserved
#
######################################################
"""
Similar Test Trigger Extend DmpTrigger

File: sem_params_trigger.py
Author: 
Date: 2018/02/05 18:19
"""
from src.schemas import sem_parames_feature
from src.schemas import defines


import trigger


class SemParamsTrigger(trigger.Trigger):
    """
    Similar Test Trigger
    get request and return feature
    """

 

    def __init__(self): 
        """
        do init
        """
        super(SemParamsTrigger,self).__init__()
        # init class var
        self.managerlogger.logger.info("sem_params_triger trigger innit ")
        
        self.redis_dict_name = None
        self.sem_params_feature = sem_parames_feature.SemParamsFeature()
          
        self.conf_group_name='sem_redis_trigger'    


    def trigger(self):
        """
        get dmp_request and return feature_set
        """
        
        self.managerlogger.logger.info("start run trigger")    
       
        self.redis_dict_name = self.config_manager.get_key(self.conf_group_name,'redis_dict_name')
        self.access_dict_model.set_log_dic_key('redis_dict_name',self.redis_dict_name) 
        
        redis_dict = self.dict_manager.get_dict(self.redis_dict_name) 
        print dir(redis_dict)
        self.managerlogger.logger.info('get redis dict success')
             
        self.sem_params_feature = self.__run_detail(redis_dict,self.dmp_request)

        self.managerlogger.logger.info('generate feature success')
        self.access_dict_model.set_log_dic_key('sem_params_feature',str(self.sem_params_feature))
        
        return self.sem_params_feature


    def __run_detail(self, redis_dict, dmp_request):
        """
        get (request+20) similar test id from dict
        return dmp_feature_set
        """

        try:

            self.managerlogger.logger.info("start  rundetail  ")
                       
            
        
            type = dmp_request.type
            key =  dmp_request.key
            value = dmp_request.value
            request_id = dmp_request.request_id            
            timestamp = dmp_request.timestamp

            self.sem_params_feature.key = key
            self.sem_params_feature.request_id = request_id 
            self.sem_params_feature.type = type
            self.sem_params_feature.timestamp= timestamp
                       

            if type =='get':
                   self.sem_params_feature.value= redis_dict.find_by_key(key)
            elif type == 'set':
                   self.sem_params_feature.old_value = redis_dict.find_by_key(key)
                   redis_dict.set_by_key(key,value)
                   self.sem_params_feature.value = value
            else:
                   self.sem_params_feature.status=-1
                   return self.sem_params_feature
                
            self.sem_params_feature.status=1

            return self.sem_params_feature

        except Exception as e:
            self.managerlogger.logger.error(e)
            self.sem_params_feature.status=-1
            return self.sem_params_feature
            #return defines.ReturnCode.FAIL
