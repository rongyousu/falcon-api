#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
试题排重实现类

File: test_dis_test.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import json
import falcon
import requests

import basetree




class Test_Dis_Resource(basetree.TreeResource):
    
    def __init__(self,db):
          basetree.TreeResource.__init__(self,db)
   
    @falcon.before(basetree.validata_json_data)
    #@falcon.before(basetree.validata_content_data)
    def on_post(self,req,resp,tn_name):
       
       # try:
        raw_json = req.stream.read()
        print raw_json.decode('utf-8')
        obj = json.loads(raw_json.decode('utf-8'))
       # except Exception:
       #     raise falcon.HTTPBadRequest(
       #               'post  data',
       #               'Could not properly parse the provided data as JSON'
       #     )
        

        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200
        
        resp.body = self.format_body({
            "status_test_dis": 'ok',
            "tree_sourse_id": str(tn_name)
        })


    #@falcon.before(basetree.validata_json_data)
    def on_get(self, req, resp, tn_name):
        bz = req.get_param('bz') or ''
        print 'bz:'+str(bz)
        test_id=req.get_param('test_id') or '0'
        print 'tn_name:'+str(tn_name)
        print self.db.find_by_key(int(test_id))
        print req.context['request_id']
        self.accessDictModel.set_log_dic_key('request_id',req.context['request_id'])


        print self.name
        self.accessDictModel.set_log_dic_key('name',self.name)
        try:

            self.accesslogger.info(str(bz))
        except Exception as ex:
            self.accesslogger.error(ex)
            description = ('Aliens have attacked our base! We will '
                           'be back as soon as we fight them off. '
                           'We appreciate your patience.')

            raise falcon.HTTPServiceUnavailable(
                'Service Outage',
                description,
                30)

        # An alternative way of doing DRY serialization would be to
        # create a custom class that inherits from falcon.Request. This
        # class could, for example, have an additional 'doc' property
        # that would serialize to JSON under the covers.
        req.context['result'] = 'surongyou'

        resp.set_header('Powered-By', 'Falcon')
        resp.status = falcon.HTTP_200
        
        print self.accessDictModel.format_body()

        resp.body = self.format_body({
            "status_test_dis": 'ok',
            "tree_sourse_id": self.accessDictModel.format_body()
        })

