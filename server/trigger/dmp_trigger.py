#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Trigger Defination

File: dmp_trigger.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 19:13
"""

from util import defines
from interface import dmp_request
from interface import dmp_feature

class DmpTrigger(object):
    """
    do trigger
    """

    def __init__(self):
        pass

    def trigger(self, request):
        """
        Main API
        trigger features
        """

        # do reset
        self.__reset(request)

        # do trigger
        features = self.__do_trigger(request)

        # cut off & return
        self.__pack_feature(features)

        return defines.ReturnCode.SUCC

    def __reset(self, request):
        return defines.ReturnCode.SUCC

    def __do_trigger(self, request):
        return dmp_feature.DmpFeature()

    def __pack_feature(self, features):
        return defines.ReturnCode.SUCC

