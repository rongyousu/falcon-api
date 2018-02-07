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

from util.defines import ReturnCode
from util.defines import DictConf
from util.unit_dict import UnitDict
from util.dict_creator import DictCreator


class DualDict(object):
    """
    0/1 dict container
    return current usefull dict operator
    """

    # dict size = 2
    DICT_SIZE = 2

    # dict array, size = 2
    __dict = []

    # current usefull dict index
    __dict_index = -1
    # current used dict conf
    __dict_conf = None


    @property
    def unit_dict(self):
        """
        return current dict
        """
        if self.__dict_index == -1:
            print "Index out of range for DualDict[idx=%d]" %(self.__dict_index)
            return None

        return self.__dict[self.__dict_index]

    @property
    def dict_type(self):
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_type

    @property
    def dict_name(self):
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_name

    @property
    def reload_cmd(self):
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.reload_cmd

    def reload(self):
        return self.reload(self.__dict_conf)

    def reload(self, dict_conf):
        """
        reload dict and set __dict_index
        """
        if self.__dict_index == -1:
            # do init
            if self.__init(dict_conf.dict_type) != ReturnCode.SUCC:
                print "Fail to init dict[%s:%s]" %(dict_conf.dict_type, dict_conf.dict_name)
                return ReturnCode.ERROR

        elif not self.__need_update(dict_conf.dict_md5):
            # old dict file, do not need update
            print "Dict[%s] do not neet update" %(self.__dict[self.__dict_index].dict_name)
            return ReturnCode.FAIL

        # load dict at next dict index
        next_dict_index = (self.__dict_index + 1) % self.DICT_SIZE
        if ReturnCode.SUCC != self.__dict[self.__dict_index].load(dict_conf):
            print "Dict load error"
            return  ReturnCode.FAIL

        # set current dict index
        self.__dict_index = next_dict_index
        self.__dict_conf = dict_conf

        # destroy pre dict
        # self.__dict[self.__dict_index].destry()

        print "Done dict[%s] reload on cmd[%s]" %(dict_conf.dict_name, dict_conf.reload_cmd)

        return ReturnCode.SUCC

    def __init(self, dict_type):
        # init dict array
        for i in range(self.DICT_SIZE):
            unit_dict = DictCreator.create_dict(dict_type)
            if unit_dict is None:
                print "Error DictConf.dict_type[%s]" %(dict_type)
                return ReturnCode.ERROR

            self.__dict.append(unit_dict)

        # empty dict array
        self.__dict_index = 0
        return ReturnCode.SUCC

    def __need_update(self, dict_md5):
        if dict_md5 == self.__dict_conf.dict_md5:
            return False
        return True

