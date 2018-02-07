#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Display Defination

File: dmp_display.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 20:12
"""

from util import defines
from interface import dmp_feature
from interface import dmp_request
from interface import dmp_response


class DmpDisplay(object):
    """
    trans features to response
    """

    def __init__(self):
        pass

    def display(self, features):
        """
        Main API
        trans features to response
        """
        print "In DmpDisplay: display"

        # sort
        self.__do_rank(features)

        # merge to response
        self.__features2response(features)

        return defines.ReturnCode.SUCC

    def __do_rank(self, features):
        """
        sort features according to demand
        """
        print "In DmpDisplay: __do_rank"
        return defines.ReturnCode.SUCC

    def __features2response(self, features):
        """
        merge all features to a response
        """
        print "In DmpDisplay: __features2response"
        return defines.ReturnCode.SUCC
