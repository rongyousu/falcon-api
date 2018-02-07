######################################################
#
#Copyright (c) 2017 xueersi.com,Inc.All Right Reserved
#
######################################################
"""
transform request to dmp_request 

File: .py
Author: wubo(wubo@100tal.com)
Date: 2017/05/17 15:28
"""
import json

from src.schemas import dmp_request
from src.systemlog  import sysmanagerlog
from src.systemlog  import syserrorlog


import img2vector 

class RequestToDmpRequest(object):
    """
    transform request strean to instance of class DmpRequest
    """
    def __init__(self,access_dict_model):
        """
        init dmp_request
        """
        self.dmp_request = dmp_request.DmpRequest()
        self.managerlogger=sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger=syserrorlog.SysErrorLog(__file__)
        self.access_dict_model = access_dict_model        

    def transform_post_request_to_dmprequest(self,req):
        """
        transform request to class DmpRequest
        """
        try:
          
            #change request to requet_json
            request_json = req.get_param('params')
            

            request_object = json.loads(request_json.decode('utf-8'))
            request_object =  request_object['query']
          
            self.managerlogger.logger.info('get rquest object success')
            self.access_dict_model.set_log_dic_key('request_object',str(request_object))

            #get requried var from json object
            self.dmp_request.request_id = req.context['request_id']
   

    
            if 'request_src' in request_object.keys():
                self.dmp_request.request_src = request_object['request_src']  
            else :
                self.dmp_request.request_src = ''
            
            self.access_dict_model.set_log_dic_key('tmp_request.request_src', str(self.dmp_request.request_src))
 
            if 'request_mask' in request_object.keys():
                self.dmp_request.request_mask = request_object['request_mask']  
            else :
                self.dmp_request.request_mask = ''

            self.access_dict_model.set_log_dic_key('tmp_request.request_mask', str(self.dmp_request.request_mask))


            if 'request_num' in request_object.keys():
                self.dmp_request.request_num = request_object['request_num']  
            else :
                self.dmp_request.request_num = ''

            self.access_dict_model.set_log_dic_key('tmp_request.request_num',  str(self.dmp_request.request_num))

             #get optional var fom json object
           
            if 'pic_url' in request_object.keys():
               
                self.dmp_request.test_request.img_url = request_object['pic_url']
            else :
                self.dmp_request.test_request.img_url=''
         
            self.access_dict_model.set_log_dic_key('dmp_request.test_request.img_url',self.dmp_request.test_request.img_url)

            if 'user_id' in request_object.keys():
                self.dmp_request.user_id = request_object['user_id']
            else :
                self.dmp_request.user_id = ''
            self.access_dict_model.set_log_dic_key('dmp_request.user_id',self.dmp_request.user_id)

            if 'xes_id' in request_object.keys():
                self.dmp_request.xes_id = request_object['xes_id']
            else :
                self.dmp_request.xes_id= ''
            self.access_dict_model.set_log_dic_key('dmp_request.xes_id',self.dmp_request.xes_id)


            if 'stu_id' in request_object.keys():
                self.dmp_request.stu_id = request_object['stu_id']
            else:
                self.dmp_request.stu_id = ''
            self.access_dict_model.set_log_dic_key('dmp_request.stu_id',self.dmp_request.stu_id)

            if 'teacher_id' in request_object.keys():
                self.dmp_request.teacher_id = request_object['teacher_id']
            else :
                self.dmp_request.teacher_id = ''
            self.access_dict_model.set_log_dic_key('dmp_request.teacher_id',self.dmp_request.teacher_id)
        
            self.managerlogger.logger.info("dmp_request is innit, the request_id ")
        except Exception as e:
            self.managerlogger.logger.error("_dmp_request is error: %s" %(str(e)))
            self.errorlogger.logger.error("_dmp_request is error: %s" %(str(e)))
        

        return self.dmp_request
