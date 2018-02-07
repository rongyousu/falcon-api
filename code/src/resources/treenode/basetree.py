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

import json
from src.schemas  import accessdictmodel
from src.systemlog import accesslog
import falcon
import requests


def validata_json_data(req, resp, kwargs):
    def hook(req,resp,resource,params):
        try:
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


class TreeResource():

    def __init__(self, db):
        self.db = db
        self.accesslogger=accesslog.AccessLog(__file__)
        self.name='test'
        self.accessDictModel=accessdictmodel.AccessDictModel()
        
    def format_body(self, data):
        return json.dumps(data)
