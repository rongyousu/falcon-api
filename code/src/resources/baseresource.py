#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
base resource

File: baseresource.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""
#import sys
#sys.path.append('../..')


import json
from src.schemas  import accessdictmodel
from src.systemlog import accesslog
from src.systemlog  import sysmanagerlog
from src.systemlog  import syserrorlog

import falcon
import requests




def validata_json_data(req, resp, kwargs):
    def hook(req,resp,resource,params):
        try:
                 print 'start vali'
                 raw_json = req.stream.read()
                 obj = json.loads(raw_json.decode('utf-8'))
                 print raw_json.decode('utf-8')
                 print 'validata end'
        except Exception:
                 raise falcon.HTTPBadRequest(
                      'Invalid data',
                      'Could not properly parse the provided data as JSON'
            )
    return hook
 
def validata_content_data(req, resp, kwargs):
     def hook(req, resp, resource, params):
        length = req.content_length
         
        req.stream.read()

        if length is not None and length > 500:
            msg = ('The size of the request is too large. The body must not '
                   'exceed ' + str(limit) + ' bytes in length.')

            raise falcon.HTTPRequestEntityTooLarge(
                'Request body is too large', msg)

     return hook


class BaseResource():

    def __init__(self,dbmanager,triggercfg,managercfg,displaycfg):
        self.dbmanager=dbmanager
        self.triggercfg=triggercfg
        self.managercfg=managercfg
        self.displaycfg=displaycfg        

        self.accesslogger=accesslog.AccessLog(__file__)
        self.managerlogger=sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger=syserrorlog.SysErrorLog(__file__)
        self.accessDictModel=accessdictmodel.AccessDictModel()
        
    def format_body(self, data):
        return json.dumps(data)

    def validata_app_data(self,app_name):
        check_result=False
        try:
            check_result=self.triggercfg.has_option('trigger',app_name)
        except Exception:
            pass
        if not check_result :
            raise falcon.HTTPBadRequest(
                'Bad app_name request',
                'the app_name  must be registered  in the api system.')
        

