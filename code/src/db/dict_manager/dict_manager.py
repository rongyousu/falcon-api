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

from src.schemas import defines
from src.schemas import sem_redis_dict_conf

from src.util import configmanager
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog

import dual_dict
import redis_dict

class DictManager(object):
    """
    manage all dicts
    implement dict load/get/reload
    """

    # DualDict list
    __dicts = None
    __dicts_conf = None

    def __init__(self):
        # init log
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)

        self.managerlogger.logger.info("Done DictManager init")
        self.__dicts = {}
        self.__dicts_conf = []

    def __del__(self):
        if self.__dicts is not None:
            self.__dicts.clear()
        if self.__dicts_conf is not None:
            del self.__dicts_conf[:]

    def load_dicts(self, dict_conf_file):
        """
        load all dicts from configure file
        return load error num
        """
        self.managerlogger.logger.info("Start to load all dicts")

        load_error_num = 0

        # load dict conf from file
        if defines.ReturnCode.SUCC != self.__init_dicts_conf(dict_conf_file):
            self.managerlogger.logger.error("Fail to load dict conf[%s]" %(dict_conf_file))
            return load_error_num

        for dict_conf in self.__dicts_conf:
            if (not isinstance(dict_conf, (defines.DictConf,sem_redis_dict_conf.SemRedisDictConf)) ) or (not dict_conf.valid()):
                try:
                    load_error_num += 1
                    self.managerlogger.logger.error("Fail to load dict[%s]: conf error" %(dict_conf.dict_name))
                except Exception as e:
                    self.managerlogger.logger.error("Fail to load dict, Unknown conf:" %(str(e)))
                    self.errorlogger.logger.error("Fail to load dict, Unknown conf:" %(str(e)))
                
                load_error_num += 1
                continue
            
            if dict_conf.dict_name in self.__dicts:
                self.managerlogger.logger.error("Fail to load dict[%s]: duplicated" %(dict_conf.dict_name))
                load_error_num += 1
                continue

            if dict_conf.dict_name =="img_tests_annoy_dict":
                 new_dict = dual_dict.DualDict()
            elif dict_conf.dict_name =="auto_sem_redis_dict":
                 new_dict = redis_dict.RedisDict()

            if defines.ReturnCode.SUCC != new_dict.load(dict_conf):
                self.managerlogger.logger.error("Fail to load dict[%s]: load error" %(dict_conf.dict_name))
                load_error_num += 1
                continue

            self.__dicts[dict_conf.dict_name] = new_dict

        self.managerlogger.logger.info("Done load dict, succ[%d] fail[%d]" %(len(self.__dicts), load_error_num))

        return load_error_num

    def reload(self, reload_cmd):
        """
        reload all dicts which reload cmd matches
        return succ reload num
        """
        if (reload_cmd is None) or (reload_cmd == ''):
            self.managerlogger.logger.warning("Empty reload_cmd")
            return defines.ReturnCode.FAIL

        self.managerlogger.logger.info("Starting to reload dict[%s]" %(reload_cmd))

        need_reload_num = 0
        real_reload_num = 0
        for v_dict in self.__dicts.values():
            self.managerlogger.logger.debug("current dict reload cmd[%s:%s]" \
                    %(v_dict.reload_cmd, reload_cmd))
            if v_dict.reload_cmd == reload_cmd:
                need_reload_num += 1
                if defines.ReturnCode.SUCC == v_dict.reload():
                    real_reload_num += 1
        self.managerlogger.logger.info("Done reload: needed[%d], real[%d]" %(need_reload_num,real_reload_num))
        return real_reload_num

    def get_dict(self, dict_name):
        """
        get dict by dict name
        if not found, return None
        """
        if (dict_name is None) or (dict_name == ''):
            self.managerlogger.logger.warning("Empty dict name")
            return None

        if dict_name in self.__dicts:
            return self.__dicts[dict_name].unit_dict
        else:
            self.managerlogger.logger.debug("Dict[%s] not exist" %(dict_name))
            return None

    def __init_dicts_conf(self, dict_conf_file):
        # reset
        if self.__dicts_conf is None:
            self.__dicts_conf = []
        else:
            del self.__dicts_conf[:]

        dict_conf_manager = configmanager.ConfigManager(dict_conf_file)
        if dict_conf_manager is None:
            self.managerlogger.logger.error("Fail to load dict conf: file[%s] not exist" %(dict_conf_file))
            return defines.ReturnCode.FAIL
                 
     

        for dict_conf in dict_conf_manager:
            try:
                all_conf_params = {}
                for k, v in dict_conf_manager.get_keys(dict_conf):
                    all_conf_params[k] = v
                print dict_conf
                print all_conf_params
                if all_conf_params["dict_type"] == "annoy_dict":
                    self.__dicts_conf.append(defines.DictConf(
                          all_conf_params[defines.DictConf.DICT_TYPE],
                          dict_conf,
                          all_conf_params[defines.DictConf.RELOAD_CMD],
                          all_conf_params[defines.DictConf.FULL_PATH],
                          all_conf_params))
                elif all_conf_params["dict_type"] == "redis":
                    self.__dicts_conf.append(sem_redis_dict_conf.SemRedisDictConf(
                          all_conf_params[sem_redis_dict_conf.SemRedisDictConf.DICT_TYPE],
                          dict_conf,
                          all_conf_params[sem_redis_dict_conf.SemRedisDictConf.REDIS_URL],
                          all_conf_params[sem_redis_dict_conf.SemRedisDictConf.REDIS_PORT],
                          all_conf_params[sem_redis_dict_conf.SemRedisDictConf.REDIS_DB],
                          all_conf_params

                          ))
       
            except Exception as e:
                self.managerlogger.logger.error("DictConf[%s] error: %s" %(dict_conf, str(e)))
                self.errorlogger.logger.error("DictConf[%s] error: %s" %(dict_conf, str(e)))

        self.managerlogger.logger.info("Done init conf[%s]" %(dict_conf_file))
        return defines.ReturnCode.SUCC

    def __iter__(self):
        for d in self.__dicts.values():
            yield d.unit_dict

