###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
Request defination

File: dmp_request.py
Author: 
Date: 2017/05/05 14:56
"""

from util import defines
from interface import test_feature


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
    _request_test = test_feature.TestFeature() # optional

    """ params for identifing user """
    # user identity
    user_id = ''        # optional
    # student identity
    xes_id = ''         # optional
    stu_id = ''         # optional
    # tearch identity
    teacher_id = ''     # optional

    def __init__(self):
        self.request_id = ''
        self.request_mask = defines.FeatureType.UNKNOWN

    def valid(self):
        if self.request_id == '' \
            or self.request_mask == defines.FeatureType.UNKNOWN:
            return False

        return True

