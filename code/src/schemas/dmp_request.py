###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Request defination

File: dmp_request.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 14:56
"""

import defines
import test_feature


class DmpRequest(object):
    """
    Represents a client's HTTP request
    """

    """ params for identifing request """
    # uniq request identity
    # log id as usual
    request_id = ''     # required
    # mark the request source
    # such as UA, APP...
    request_src = ''    # required
    # data selection mask
    # such as : 
    #   00000001 for k nearest neighbors for tests 
    #   00000010 for students info
    request_mask = 0    # required
    # value num
    request_num = 0     # required

    """ params for tests """
    # test info
    test_request = None # optional
    
    # user identity
    user_id = ''        # optional
    # student identity
    xes_id = ''         # optional
    stu_id = ''         # optional
    # tearch identity
    teacher_id = ''     # optional

    def __init__(self):
        self.test_request = test_feature.TestFeature()
        self.request_mask = defines.FeatureType.UNKNOWN

    def __del__(self):
        self.reset()

    def reset(self):
        self.request_id = ''
        self.request_src = ''
        self.request_mask = 0
        self.request_num = 0
        self.test_request.reset()
        self.user_id = ''
        self.xes_id = ''
        self.stu_id = ''
        self.tearcher_id = ''

    def valid(self):
        return ((self.request_id != '') \
                and (self.request_mask != defines.FeatureType.UNKNOWN))

