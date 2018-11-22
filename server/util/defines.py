###########################################################
#
# Copyright (c) 2017  Inc. All Rights Reserved
#
###########################################################
"""
Common Structure Definition

File: defines.py
Author: 
Date: 2017/05/05 16:00
"""


class ReturnCode(object):
    """
    code for response status
    """

    ERROR   = -1
    SUCC    = 0
    FAIL    = 1


class FeatureType(object):
    """
    feature identity code
    """

    UNKNOWN         = 0
    KNN_TEST        = 1
    STUDENT_INFO    = 2
    COURSE_INFO     = 4

class DictConf(object):
    """
    configure for dicts
    """

    dict_type = ''
    dict_name = ''
    dict_md5 = ''
    reload_cmd = ''

    def __init__(self, t, n, m, rc):
        self.dict_type = t
        self.dict_name = n
        self.dict_md5 = m
        self.reload_cmd = rc

    def valid(self):
        return (self.dict_type != '' \
                and self.dict_name != '' \
                and self.dict_md5 != '' \
                and self.reload_cmd != '')

