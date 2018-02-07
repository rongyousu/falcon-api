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

from util import defines
from interface import test_feature


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
    _test_features = []     # optional

    def __init__(self):
        pass

