#!/usr/bin/env python
# -*- coding=utf-8 -*-



from src.util import configmanager
from src.systemlog import sysmanagerlog
from src.systemlog import syserrorlog
from src.schemas  import accessdictmodel
from src.systemlog import accesslog

import time

class DisplayOneConf(object):
    """
     filter and sort's condition
    """
    MIN_ID = 'min_id'
    MAX_ID = 'max_id'

    MIN_WEIGHT = 'min_weight'
    MAX_WEIGHT = 'max_weight'
    
    MIN_TIMESTAMP = 'min_timestamp'
    MAX_TIMESTAMP = 'max_timestamp'

    SORT = 'sort'
    REVERSE = 'reverse'

    #save confing name
    conf_name = ''
    
    min_id = 0
    max_id = 0

    min_weight = 0
    max_weight = 0
    
    min_timestamp = 0
    max_timestamp = 0

    sort = 'weight'
    reverse = 1


class DmpDisplayManager(object):
    """
     read display.conf
    """

    __conf_dict = None

    def __init__(self, access_model):
        """
         init log
         init and read conf
        """
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)
        self.access_model = access_model

        self.__conf_dict = {}

    def __del__(self):
        if self.__conf_dict is not None:
            self.__conf_dict.clear()
            self.__conf_dict = None

    def load_conf(self, config):
        self.managerlogger.logger.info('Start load conf')
        
        try:
            start_time = int(round(time.time()*1000))
            confs = config

            for section in confs:
                conf_one = DisplayOneConf()
                conf_one.conf_name = section

                if confs.has_option(section, DisplayOneConf.MIN_ID):
                    conf_one.min_id = confs.get_float(section, DisplayOneConf.MIN_ID)
                else:
                    conf_one.min_id = confs.get_float('default', DisplayOneConf.MIN_ID)

                if confs.has_option(section, DisplayOneConf.MAX_ID):
                    conf_one.max_id = confs.get_float(section, DisplayOneConf.MAX_ID)
                else:
                    conf_one.max_id = confs.get_float('default', DisplayOneConf.MAX_ID)
               
                if confs.has_option(section, DisplayOneConf.MIN_WEIGHT):
                    conf_one.min_weight = confs.get_float(section, DisplayOneConf.MIN_WEIGHT)
                else:
                    conf_one.min_weight = confs.get_float('default', DisplayOneConf.MIN_WEIGHT)
               
                if confs.has_option(section, DisplayOneConf.MAX_WEIGHT):
                    conf_one.max_weight = confs.get_float(section, DisplayOneConf.MAX_WEIGHT)
                else:
                    conf_one.max_weight = confs.get_float('default', DisplayOneConf.MAX_WEIGHT)
               
                if confs.has_option(section, DisplayOneConf.MIN_TIMESTAMP):
                    conf_one.min_timestamp = confs.get_float(section, DisplayOneConf.MIN_TIMESTAMP)
                else:
                    conf_one.min_timestamp = confs.get_float('default', DisplayOneConf.MIN_TIMESTAMP)
               
                if confs.has_option(section, DisplayOneConf.MAX_TIMESTAMP):
                    conf_one.max_timestamp = confs.get_float(section, DisplayOneConf.MAX_TIMESTAMP)
                else:
                    conf_one.max_timestamp = confs.get_float('default', DisplayOneConf.MAX_TIMESTAMP)

                if confs.has_option(section, DisplayOneConf.SORT):
                    conf_one.sort = confs.get_key(section, DisplayOneConf.SORT)
                else:
                    conf_one.sort = confs.get_key('default', DisplayOneConf.SORT)

                if confs.has_option(section, DisplayOneConf.REVERSE):
                    conf_one.reverse = confs.get_float(section, DisplayOneConf.REVERSE)
                else:
                    conf_one.reverse = confs.get_float('default', DisplayOneConf.REVERSE)

                self.__conf_dict[section] = conf_one

            if len(self.__conf_dict) <= 0:
                self.managerlogger.logger.warning('load conf result: 0 dict')
                self.errorlogger.logger.warning('load conf result: 0 dict')

                return None

            end_time = int(round(time.time()*1000))

            self.managerlogger.logger.info('End load conf')
            self.access_model.set_log_dic_key('display_conf:load_conf_time', str(end_time - start_time))

            return len(self.__conf_dict)
        except Exception as e:
            self.errorlogger.logger.warning(e)
            self.managerlogger.logger.warning(e)

            return None

    def find_conf(self, conf_name):
        """
         get conf from conf_list
        """
        start_time = int(round(time.time()*1000))

        self.managerlogger.logger.info('Start find conf[%s]' %(conf_name))

        conf = None

        try:

            if conf_name in self.__conf_dict.keys():
                conf = self.__conf_dict[conf_name]

            if conf == None:
                self.managerlogger.logger.warning('Fail to find display \
                    config for name[%s]' %(conf_name))
                return None

            end_time = int(round(time.time()*1000))

            self.access_model.set_log_dic_key('display:conf',conf)
            self.access_model.set_log_dic_key('display:find_conf_time', str(end_time - start_time))

        except Exception as e:
            self.errorlogger.logger.warning('Failed find conf[%s]' %(conf_name))
            self.managerlogger.logger.info('Failed find conf[%s]' %(conf_name))

        return conf

