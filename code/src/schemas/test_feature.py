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
Author
Date: 2017/05/05 18:49
"""

import dmp_feature


class TestFeature(dmp_feature.DmpFeature):
    """
    TestFeature of DmpFeature
    """

    img_url = ''


    def __init__(self):
        super(TestFeature, self).__init__()
        pass

    def reset(self):
        super(TestFeature, self).reset()
        self.img_url = ''
        vector = [] 
    def setvalue(self,id,weight):
        self.id=id
        self.weight=weight
