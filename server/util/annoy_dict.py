###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
Annoy Dict Definition

File: annoy_dict.py
Author: 
Date: 2017/05/08 15:35
"""

from util.defines import ReturnCode
from util.unit_dict import UnitDict


class AnnoyDict(UnitDict):
    """
    implement annoy UnitDict
    search all vectors to find K Nearrest Neightbors
    """

    __dict_conf = None

    @property
    def identity(self):
        if self.__dict_conf is None:
            return ''
        else:
            return "name[%s], type[%s]" %(self.__dict_conf.dict_name, self.__dict_conf.dict_type)

    def load(self, dict_conf):
        if self._dict is None:
            print "Create AnnoyDict[%s]" %(dict_conf.dict_name)
        print "In AnnoyDict: load"

        self.__dict_conf = dict_conf
        return ReturnCode.SUCC

    def destroy(self):
        if self._dict is not None:
            print "Destroy AnnoyDict"
        print "In AnnoyDict: destroy"

        return ReturnCode.SUCC

