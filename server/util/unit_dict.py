###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Dual Dict Definition

File: dual_dict.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/08 14:30
"""

from annoy import AnnoyIndex

from util.defines import ReturnCode


class UnitDict(object):
    """
    dict operating implement
    """

    # dict instance
    _dict = None

    def __init__(self):
        self._dict = None

    @property
    def instance(self):
        return self._dict

    def load(self, dict_conf):
        print "In UnitDict: load dict[%s]" %(dict_conf.dict_name)
        return ReturnCode.SUCC

    def destroy(self):
        print "In UnitDict: destroy dict[%s]" %(dict_conf.dict_name)
        return ReturnCode.SUCC

