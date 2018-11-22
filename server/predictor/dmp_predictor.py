#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Predictor Defination

File: dmp_predictor.py
Author: 
Date: 2017/05/05 19:59
"""

from util import defines
from interface import dmp_request
from interface import dmp_feature


class DmpPredictor(object):
    """
    do predict
    """

    def __init__(self):
        pass

    def predict(self, request, features):
        """
        Main API
        predict feature weight
        """

        # do reset
        self.__reset(request, features)

        # do predict
        self.__do_predict(request, features)

        return defines.ReturnCode.SUCC

    def __reset(self, request, features):
        return defines.ReturnCode.SUCC

    def __do_predict(self, request, features):
        return defines.ReturnCode.SUCC

