#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Test Trigger Defination

File: test_trigger.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 19:55
"""

from interface import test_feature

from trigger import dmp_trigger


class TestTrigger(dmp_trigger.DmpTrigger):
    """
    do test trigger
    """

    def __init__(self):
        pass

    def __do_trigger(self, request):
        return test_feature.TestFeature()

