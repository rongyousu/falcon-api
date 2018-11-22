#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Service Schedule Defination

File: dmp_service.py
Author
Date: 2017/05/05 16:35
"""

import json

from util import defines
from interface import dmp_feature
from interface import dmp_request
from interface import dmp_response
from trigger import dmp_trigger
from predictor import dmp_predictor
from display import dmp_display


class DmpService(object):
    """
    service API declarations
    """
    
    def __init__(self):
        pass

    def on_get(self, req, resp):
        """
        get request
        """
        return __search(req, resp)

    def on_post(self, req, resp):
        """
        post request
        """
        return __search(req, resp)
        
    def __search(self, req, resp):
        """
        do search
        init dmp request from falcon request
        make sure response sort&cut off
        """

        # init
        # request: DmpRequest
        request = self.__init_request(req)

        # trigger dmp feature list
        # features: DmpFeatureSet
        features = self.__do_trigger(request)

        # predict
        self.__do_predict(request, features)

        # display
        # response: DmpResponse
        response = self.__features2response(features)

        # to json
        resp.body = json.dumps(response)

        return defines.ReturnCode.SUCC
        

    def __init_request(self, req):
        """
        init request from url params
        """
        return defines.ReturnCode.SUCC

    def __do_trigger(self, request):
        """
        get feature from request
        """
        dmp_trigger.DmpTrigger().trigger(request)
        return defines.ReturnCode.SUCC

    def __do_predict(self, request, features):
        """
        use models to predict feature weight
        """
        dmp_predictor.DmpPredictor().predict(request, features)

        return defines.ReturnCode.SUCC

    def __features2response(self, features):
        """
        package features to response
        """
        dmp_display.DmpDisplay().display(features)

        return defines.ReturnCode.SUCC

