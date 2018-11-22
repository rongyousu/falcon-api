#!/usr/bin/env python
# -*- coding=utf-8 -*-

import json

class SemParamsRequest(object):
    """
    Define base feature
    """
    def __init__(self):
        self.request_id = ''
        self.key = ''
        self.value = ''
        self.type = ''  #get /set
        self.timestamp=0
        self.status= 0
    
    def init_by_req(self,req):
        #change request to requet_json
        request_json = req.get_param('params')
        print request_json

        request_object = json.loads(request_json.decode('utf-8'))
        request_object =  request_object['query']
      
        self.request_id = req.context['request_id']
        if 'key' in request_object.keys():
                self.key = request_object['key']
        else :
                self.key = ''
        
        if 'value' in request_object.keys():
                self.value = request_object['value']
        else: 
                self.value = ''
        
        if 'type' in request_object.keys():
                self.type = request_object['type']
        else:
                self.type =''

        if 'timestamp' in  request_object.keys():
                self.timestamp = request_object['timestamp']
        else: 
                self.timestamp =''

    
    def reset(self):
        self.request_id = ''
        self.key = ''
        self.value = ''
        self.type = ''  #get /set
        self.timestamp=0
        self.status= 0

