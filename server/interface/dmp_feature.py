#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Feature Defination

File: dmp_feature.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 17:42
"""

class DmpFeature(object):
    """
    Define base feature
    """

    # uniq id
    id = 0          # required
    # for sort
    weight = 0      # required
    # timestamp
    timestamp = 0   # required


    def __init__(self):
        pass

    def __cmp__(self, other):
        if self.weight < other.weight:
            return 1
        elif self.weight > other.weight:
            return -1
        elif self.timestamp < other.weight:
            return 1
        elif self.timestamp > other.weight:
            return -1
        elif self.id > other.id:
            return 1
        elif self.id < other.id:
            return -1
        else:
            return 0
