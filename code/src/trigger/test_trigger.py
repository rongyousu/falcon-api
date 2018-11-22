#!/usr/bin/env python
# -*- coding=utf-8 -*-

######################################################
#
#Copyright (c) 2017,Inc.All Right Reserved
#
######################################################
"""
Similar Test Trigger Extend DmpTrigger

File: similar_test_trigger.py
Author: 
Date: 2017/05/14 23:19
"""
from src.schemas import test_feature
from src.schemas import dmp_feature_set
from src.schemas import defines
from src.util import request_to_dmprequest
from src.util import img2vector

import trigger


class TestTrigger(trigger.Trigger):
    """
    Similar Test Trigger
    get request and return feature_set
    """

 

    def __init__(self): 
        """
        do init
        """
        super(TestTrigger,self).__init__()
        # init class var
        self.managerlogger.logger.info("testtriger trigger innit ")
        
        self.img_dict_name = None
   
        self.test_max_weight = None
        self.img_dimension = None
        self.test_feature = test_feature.TestFeature()
        self.feature_set = dmp_feature_set.DmpFeatureSet()
       
        self.conf_group_name='trigger_test'    


    def trigger(self):
        """
        get dmp_request and return feature_set
        """
        
        self.managerlogger.logger.info("start run trigger")
    
        self.reset()
        self.test_max_weight = self.config_manager.get_key(self.conf_group_name,'test_max_weight')
        self.access_dict_model.set_log_dic_key('test_max_weight',self.test_max_weight) 
    
        self.img_dimension = self.config_manager.get_key(self.conf_group_name,'dimension')
 
        
        self.access_dict_model.set_log_dic_key('img_dimension',str(self.img_dimension)) 
 
        self.img_dict_name = self.config_manager.get_key(self.conf_group_name,'img_dict_name')
        self.access_dict_model.set_log_dic_key('img_dict_name',self.img_dict_name) 
        
        img_dict = self.dict_manager.get_dict(self.img_dict_name) 
        self.managerlogger.logger.info('get img dict success')
             
        self.feature_set = self.get_similar_test(img_dict,self.dmp_request)
        self.managerlogger.logger.info('generate feature success')
        #self.access_dict_model.set_log_dic_key('feature_set',str(self.feature_set))
        
        return self.feature_set

    def reset(self):
        """
        reset protected var
        """
        self.managerlogger.logger.info("reset feature set and test feature")

        if defines.ReturnCode.SUCC !=  self.feature_set.clear():
           self.managerlogger.logger.error("fail to claer feature set")
        
        return defines.ReturnCode.SUCC

    def get_similar_test(self, img_dict, dmp_request):
        """
        get (request+20) similar test id from dict
        return dmp_feature_set
        """

        try:

            self.managerlogger.logger.info("get similar test ")
            img_url = dmp_request.test_request.img_url
            self.access_dict_model.set_log_dic_key('img_url',img_url)
            
            img = img2vector.Img2Vector(self.img_dimension,img_url)
            self.managerlogger.logger.info("load img_url to vector success")
            
            vector = img.get_vector()
            if vector == None:
                self.access_dict_model.set_log_dic_key('img_vector','the image is error')
                return defines.ReturnCode.FAIL
            self.managerlogger.logger.info("get vector success")
           
            request_num = dmp_request.request_num + 2 
            self.access_dict_model.set_log_dic_key('request_num',request_num)
                      
            similar_test_id_list,similar_weight_list = img_dict.find_by_vector(vector,request_num) 
        
            for similar_test_id,similar_weight in zip(similar_test_id_list,similar_weight_list):
                
                tmp_f=test_feature.TestFeature()
                tmp_f.setvalue(int(similar_test_id),float(similar_weight) )
                 
                self.feature_set.push_feature(tmp_f)
 
            self.managerlogger.logger.info("push feature to feature success")

            self.feature_set = self.filter_by_weight(self.feature_set)
            self.managerlogger.logger.info("filter feature success")
            
            return self.feature_set

        except Exception as e:
            self.managerlogger.logger.error(e)
            return defines.ReturnCode.FAIL

    def filter_by_weight(self,feature_set):
        """
        filter result where item > test_max_weight(15)
        """

        try:
            self.managerlogger.logger.info("filter feature set by weight")

            tmp_feature_set = dmp_feature_set.DmpFeatureSet()
            self.managerlogger.logger.info("init tmp_feature set success")

            for feature in feature_set:
                if float(feature.weight) <=float( self.test_max_weight):
                    
                    feature.weight = 100 - feature.weight
                    if defines.ReturnCode.SUCC !=  tmp_feature_set.push_feature(feature):
                        self.managerlogger.logger.error('fail to push test feature to feature set')
            
            self.access_dict_model.set_log_dic_key('tmp_feature_set',tmp_feature_set)

            return tmp_feature_set
      
        except Exception as e:
            self.managerlogger.logger.error(e)
            return defines.ReturnCode.FAIL
