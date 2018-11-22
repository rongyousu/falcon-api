#!/usr/bin/env python
# -*- coding=utf-8 -*-



import json

from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog

import falcon
import requests


def validata_json_data(req, resp, kwargs):
    def hook(req,resp,resource,params):
        try:
                 raw_json = req.stream.read()
                 obj = json.loads(raw_json.decode('utf-8'))

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


class BaseManagerResource():

    def __init__(self,dbmanager,triggercfg):
        self.dbmanager=dbmanager
        self.triggercfg=triggercfg

        # init log
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)

       
        
    def format_body(self, data):
        return json.dumps(data)
