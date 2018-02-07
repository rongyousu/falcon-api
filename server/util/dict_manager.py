###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Dict Manager Definition

File: dict_manager.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/08 14:20
"""

from util.defines import ReturnCode
from util.defines import DictConf
from util.singleton import Singleton
from util.dual_dict import DualDict


class DictManager(Singleton):
    """
    manage all dicts
    implement dict load/get/reload
    """

    # DualDict list
    __dicts = {}

    def __init__(self):
        print "In DictManager: __init__"

    def load_dicts(self, dict_conf_list):
        load_error_num = 0
        for dict_conf in dict_conf_list:
            if (not isinstance(dict_conf, DictConf)) or (not dict_conf.valid()):
                try:
                    load_error_num += 1
                    print "Fail to load dict[%s]: conf error" %(dict_conf.dict_name)
                except Exception, e:
                    print "Fail to load dict, Unknown conf"
                
                load_error_num += 1
                continue
            
            if dict_conf.dict_name in self.__dicts:
                print "Fail to load dict[%s]: duplicated" %(dict_conf.dict_name)
                load_error_num += 1
                continue

            dual_dict = DualDict()
            if dual_dict.reload(dict_conf) != ReturnCode.SUCC:
                print "Fail to load dict[%s]: load error" %(dict_conf.dict_name)
                load_error_num += 1
                continue

            self.__dicts[dict_conf.dict_name] = dual_dict
            print dict_conf.dict_name
            print id(dual_dict)
            print id(self.__dicts[dict_conf.dict_name])

        return load_error_num

    def reload(self, reload_cmd):
        if (reload_cmd is None) or (reload_cmd == ''):
            print "Empty reload_cmd"
            return ReturnCode.FAIL

        for dual_dict in self.__dicts.values():
            if dual_dict.reload_cmd == dual_dict:
                dual_dict.reload()

    def get_dict(self, dict_name):
        if (dict_name is None) or (dict_name == ''):
            print "Empty dict name"
            return ReturnCode.FAIL

        if dict_name in self.__dicts:
            return self.__dicts[dict_name].unit_dict
        else:
            return None

