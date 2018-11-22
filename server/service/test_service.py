#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Test Service Schedule Defination

File: test_service.py
Author: 
Date: 2017/05/05 18:58
"""

from interface import dmp_request

from service import dmp_service


class TestService(dmp_service.DmpService):
    """
    inherit from DmpService
    process KNN tests request
    """

    def __init__(self):
        pass

    def __init_request(self, req):
        """
        init request test
        """
        request = dmp_request.DmpRequest()
        request._request_test.test_img_url = req.get_param('img_url')
        
        return request
