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

   
    def __init__(self):
        self.id = 0
        self.weight = 0.0
        self.timestamp = 0


    def __cmp__(self, other):
        if self.weight < other.weight:
            return 1
        elif self.weight > other.weight:
            return -1
        elif self.timestamp < other.timestamp:
            return 1
        elif self.timestamp > other.timestamp:
            return -1
        elif self.id > other.id:
            return 1
        elif self.id < other.id:
            return -1
        else:
            return 0

    def update(self, other):
        if isinstance(other, DmpFeature):
            self.weight = other.weight
            self.timestamp = other.timestamp

    def reset(self):
        self.id = 0
        self.weight = 0.0
        self.timestamp = 0

    def __str__(self):
        return "%s|%s|%s" %(self.id, self.weight, self.timestamp)

