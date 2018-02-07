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

from src.db.treenode import annoy_dict


class DictCreator(object):
    """
    dict factory
    create dict by type
    """

    @staticmethod
    def create_dict(dict_conf):
        if dict_conf.dict_type == 'annoy_dict':
            return annoy_dict.AnnoyDict(dict_conf)
        else:
            return None

