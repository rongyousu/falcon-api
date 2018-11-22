#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Test Display Defination

File: test_display.py
Author: 
Date: 2017/05/05 20:19
"""

from util import defines
from interface import dmp_feature
from interface import dmp_request
from interface import dmp_response

from display import dmp_display


class TestDisplay(dmp_display.DmpDisplay):
    """
    inherit from DmpDisplay
    do test display
    """

    def __init__(self):
        pass

    def __feature2response(self, feature):
        """
        merge a feature to a response
        """
        print "In TestDisplay: __feature2response"

        return defines.ReturnCode.SUCC
