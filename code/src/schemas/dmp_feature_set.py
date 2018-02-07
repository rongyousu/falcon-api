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

import defines
import dmp_feature


class DmpFeatureSet(object):
    """
    a set of features
    provide sort/add/remove
    """
    # store all features
    __feature_list = None
    # store all feature id->index
    # for dedup
    __feature_id_dict = None
    # feature size
    __feature_size = 0


    def __init__(self):
        self.__feature_list = []
        self.__feature_id_dict = {}

    def __del__(self):
        self.clear()

    def feature(self, feature_id):
        """
        get feature by feature id
        """
        if feature_id not in self.__feature_id_dict:
            return None
        else:
            return self.__feature_list[self.__feature_id_dict[feature_id]]

    def feature_at(self, feature_index):
        """
        get feature by index
        """
        if feature_index < 0 or feature_index >= self.__feature_size:
            return None
        else:
            return self.__feature_list[feature_index]

    def push_feature(self, feature, is_overwrite = False):
        """
        add feature at behind
        """
        if (feature is None) \
            or (not isinstance(feature, dmp_feature.DmpFeature)):
            return defines.ReturnCode.ERROR

        if feature.id in self.__feature_id_dict:
            if not is_overwrite:
                return defines.ReturnCode.FAIL
            
            self.__feature_list[self.__feature_id_dict[feature.id]].update(feature)
        else:
            self.__feature_id_dict[feature.id] = self.__feature_size
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
        if feature is None or not isinstance(feature, dmp_feature.DmpFeature):
            return defines.ReturnCode.FAIL

        if feature.id not in self.__feature_id_dict:
            return defines.ReturnCode.FAIL

        del self.__feature_list[self.__feature_id_dict[feature.id]]
        del self.__feature_id_dict[feature.id]
        self.__feature_size -= 1

        self.__udpate_feature_id_dict()

        return defines.ReturnCode.SUCC

    def clear(self):
        """
        remove all features
        """
        if self.__feature_list is not None:
            del self.__feature_list[:]
        if self.__feature_id_dict is not None:
            self.__feature_id_dict.clear()
        self.__feature_size = 0
        return defines.ReturnCode.SUCC

    def sort(self):
        """
        sort features according to weight
        """
        if self.__feature_size > 1:
            self.__feature_list.sort()
            self.__udpate_feature_id_dict()
        
        return defines.ReturnCode.SUCC

    def __udpate_feature_id_dict(self):
        """
        update feature_id_dict according to __feature_list
        """
        for i in range(self.__feature_size):
            self.__feature_id_dict[self.__feature_list[i].id] = i
        
        return defines.ReturnCode.SUCC

    def __len__(self):
        return self.__feature_size

    def __iter__(self):
        for feature in self.__feature_list:
            yield feature

