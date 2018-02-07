###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Response defination

File: dmp_response.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/05 14:56
"""

from src.schemas import defines
from src.schemas import test_feature


class DmpResponse(object):
    """
    Represents an HTTP response to a client request
    """

    """ response status """
    # response status
    status = True           # required
    # response status msg
    msg = ''                # optional

    """ response data """
    request_id = ''         # required
    # test feature list
    test_features = None    # optional

    def __init__(self):
        self.test_features = []

    def __del__(self):
        self.reset()

    def reset(self):
        self.status = True
        self.msg = ''
        self.request_id = ''
        if self.test_features is not None:
            del self.test_features[:]
