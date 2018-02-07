#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Test Predictor Defination

File: test_predictor.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 20:04
"""

from util import defines
from interface import dmp_request
from interface import dmp_feature

from predictor import dmp_predictor


class TestPredictor(dmp_predictor.DmpPredictor):
    """
    inherit from DmpPredictor
    do test feature predict
    """

    def __init__(self):
        pass

    def __do_predict(self, request, features):
        print "In TestPredictor: __do_predict"
        return defines.ReturnCode.SUCC

