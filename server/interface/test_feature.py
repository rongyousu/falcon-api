#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Test Feature Defination

File: test_feature.py
Author:
Date: 2017/05/05 18:49
"""

from interface import dmp_feature


class TestFeature(dmp_feature.DmpFeature):
    """
    TestFeature of DmpFeature
    """

    test_img_url = ''


    def __init__(self):
        pass

