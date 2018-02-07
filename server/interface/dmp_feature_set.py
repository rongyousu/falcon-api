#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
FeatureSet Defination

File: dmp_feature_set.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 17:42
"""

from util import defines
from interface import dmp_feature


class DmpFeatureSet(object):
    """
    a set of features
    provide sort/add/remove
    """

    # store all features
    __feature_list = []
    # store all feature id->index
    # for dedup
    __feature_id_dict = {}
    # feature size
    __feature_size = 0

    def __init__(self):
        __feature_size = 0

    def push_feature(self, feature, is_overwrite=False):
        """
        add feature at behind
        """
        if feature.id in self.__feature_id_dict:
            if not is_overwrite:
                return defines.ReturnCode.FAIL
            
            self.update_feature(self.__feature_id_dict[feature.id])
        else:
            self.__feature_id_dict[feature.id] = len(self.__feature_list)
            self.__feature_list.append(feature)
            self.__feature_size += 1

        return defines.ReturnCode.SUCC

    def pop_feature(self):
        """
        delete feature from tail
        """

        if self.__feature_size <= 0:
            return defines.ReturnCode.FAIL

        self.__feature_size -= 1
        del self.__feature_id_dict[self.__feature_list[self.__feature_size].id]
        del self.__feature_list[self.__feature_size]

        return defines.ReturnCode.SUCC

    def del_feature(self, feature):
        """
        del feature cause feature id dict update
        not call it at all!
        """
        if feature.id not in self.__feature_id_dict:
            return defines.ReturnCode.ERROR

        del self.__feature_list[__feature_id_dict[feature.id]]
        del self.__feature_id_dict[feature.id]
        self.__feature_size -= 1

        self.__udpate_feature_id_dict()

        return defines.ReturnCode.SUCC

    def sort(self):
        """
        sort features according to weight
        """
        self.__feature_list.sort()
        self.__udpate_feature_id_dict()
        
        return defines.ReturnCode.SUCC

    def __udpate_feature_id_dict(self):
        """
        update feature_id_dict according to __feature_list
        """
        for i in range(self.__feature_list):
            self.__feature_id_dict[self.__feature_list[i].id] = i
        
        return defines.ReturnCode.SUCC
