###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Dict Creator Definition

File: dict_creator.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/08 15:40
"""

from util.defines import ReturnCode
from util.annoy_dict import AnnoyDict


class DictCreator(object):
    """
    dict factory
    create dict by type
    """

    @staticmethod
    def create_dict(dict_type):
        if dict_type == 'annoy_dict':
            return AnnoyDict()
        else:
            return None

