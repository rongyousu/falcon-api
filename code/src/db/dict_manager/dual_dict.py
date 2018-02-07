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

import os

from src.schemas import defines
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog

from src.db import dict_creator
from multiprocessing import Process, Value, Array ,Manager



class DualDict(object):
    """
    0/1 dict container
    return current usefull dict operator
    """

    # dict size = 2
    DICT_SIZE = 2

    # dict array, size = 2
    manager = Manager()
    __dict = manager.list()

    # current usefull dict index
    __dict_index = Value('i',-1)
    __dict_md5 = Value('l',0)
    # current used dict conf
    __dict_conf = None

    __curr_dict = None   
    __curr_md5 = 0

    def __init__(self):
        # init log
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)
      
     

    def __del__(self):
        if self.__dict is not None:
            del self.__dict[:]
        self.__dict_index = Value('i',-1)
        self.__dict_conf = None

    @property
    def unit_dict(self):
        """
        return current dict
        """
        self.managerlogger.logger.info("current_index is :[%s]" %(self.__dict_index.value))
        if self.__dict_index.value == -1:
            return None
        else:
            if self.__curr_md5 != self.__dict_md5.value:
                   self.__curr_dict= self.__dict[self.__dict_index.value]
                   self.__curr_md5 = self.__dict_md5.value
           
            return self.__curr_dict

    @property
    def dict_type(self):
        """
        return current dict type
        """
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_type

    @property
    def dict_name(self):
        """
        return current dict name
        """
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_name

    @property
    def reload_cmd(self):
        """
        return current reload cmd
        """
        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.reload_cmd

    def reload(self):
        """
        reload dict at next index
        """
        self.managerlogger.logger.info("Start to reload dict[%s]" %(self.dict_name))
        return self.load(self.__dict_conf)

    def load(self, dict_conf):
        """
        reload dict and set __dict_index
        """
        # update dict md5
        new_md5 = self.__get_dict_md5(dict_conf)
    
       

        if int(self.__dict_index.value)==-1:
            # do init
            if defines.ReturnCode.SUCC != self.__init(dict_conf):
                self.managerlogger.logger.error("Fail to init dict[%s:%s]" \
                        %(dict_conf.dict_type, dict_conf.dict_name))
                return defines.ReturnCode.ERROR
            
            #innit the current temp param
            self.__curr_dict=self.__dict[0]

        elif not self.__need_update(new_md5):
            # old dict file, do not need update
            self.managerlogger.logger.warning("Dict[%s] do not neet update" \
                    %(self.__dict_conf.dict_name))
            return defines.ReturnCode.FAIL

        self.managerlogger.logger.info("Start to load dict[%s]  index:[%s]  conf[%s]" %(dict_conf.dict_name, self.__dict_index.value, str(dict_conf)))
    
        # load dict at next dict index
        next_dict_index = (int(self.__dict_index.value) + 1) % self.DICT_SIZE
        # destroy old dict
        #if defines.ReturnCode.SUCC != self.__dict[next_dict_index].destroy():
        #    self.managerlogger.logger.warning("Dict[%s] destroy error" %(dict_conf.dict_name))
        #    return defines.ReturnCode.FAIL
        # load new dict
        
        if defines.ReturnCode.SUCC != self.__dict[next_dict_index].load(dict_conf):
            self.managerlogger.logger.warning("Dict[%s] load error" %(dict_conf.dict_name))
            return  defines.ReturnCode.FAIL

        # set current dict index
        self.__dict_index.value  = next_dict_index
        self.__dict_conf = dict_conf
        self.__dict_md5.value = new_md5.__hash__()
 

        self.__curr_dict = self.__dict[next_dict_index]
        self.__curr_md5 = self.__dict_md5.value 
      

        # destroy pre dict
        # self.__dict[self.__dict_index].destry()

        self.managerlogger.logger.info("Done dict[%s] load on cmd[%s]  the current index[%s]" \
                %(dict_conf.dict_name, dict_conf.reload_cmd, self.__dict_index.value))
        return defines.ReturnCode.SUCC

    def __init(self,dict_conf):
        # init dict array
        for i in range(self.DICT_SIZE):
            unit_dict = dict_creator.DictCreator.create_dict(dict_conf)

            #unit_dict = foo.Foo(dict_conf)            
            if unit_dict is None:
                self.managerlogger.logger.error("Error DictConf.dict_type[%s]" %(dict_type))
                return defines.ReturnCode.ERROR
            
            self.__dict.append(unit_dict)
               
        # empty dict array
        # self.__dict_index = 0
        self.managerlogger.logger.info("Done init dict manager")
        return defines.ReturnCode.SUCC

    def __need_update(self, dict_md5):
        """
        check file md5[./data/dict_name.md5]
        if updated, reload dict
        """
        if self.__dict_conf is None:
            return True
        self.managerlogger.logger.warning("new md5[%s]  old md5[%s]" %(dict_md5.__hash__(), self.__dict_md5.value))
        return (dict_md5.__hash__() != self.__dict_md5.value)
    
    def __get_dict_md5(self, dict_conf):
        cur_dict_md5 = ''
        md5_file = "%s.md5" %(dict_conf.full_path)
        if not os.path.exists(md5_file):
            self.managerlogger.logger.warning("md5 file[%s] not exist" %(md5_file))
            return cur_dict_md5
        
        try:
            cur_dict_md5 = (open(md5_file).readline().split())[0]
        except Exception as e:
            self.managerlogger.logger.warning("read md5 file[%s] error: " \
                    %(md5_file, str(e)))
            self.errorlogger.logger.warning("read md5 file[%s] error:" \
                    %(md5_file, str(e)))
        
        return cur_dict_md5

