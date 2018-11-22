

import os

from src.schemas import defines
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog

from src.db import dict_creator



class RedisDict(object):
    """
    redis dict container
    return the redis dict operator
    """

    #es dict conf
    __dict_conf = None

    #es dict
    __dict = None

    def __init__(self):
        # init log
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)

    def __del__(self):
        self.__dict_conf = None
        self.__dict = None

    @property
    def unit_dict(self):
        """
         return the redis dict
         arguments: None
         return: es dict
        """
        return self.__dict

    @property
    def dict_type(self):
        """
         return dict type
         arguments: None
         return: es dict type
        """

        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_type

    @property
    def dict_name(self):
        """
         return dict name
         arguments: None
         return: redis dict name
        """

        if self.__dict_conf is None:
            return ''
        else:
            return self.__dict_conf.dict_name

    def load(self, dict_conf):
        """
         load redis dict
         arguments: redis dict config
         return: success or not
        """

        self.__dict_conf = dict_conf

        # do init
        if defines.ReturnCode.SUCC != self.__init(dict_conf):
            self.managerlogger.logger.error("Fail to init dict[%s:%s]" \
                                            % (dict_conf.dict_type, dict_conf.dict_name))
            return defines.ReturnCode.ERROR

        return defines.ReturnCode.SUCC

    def __init(self,dict_conf):
        """
         create an redis dict
         arguments: redis dict config
         return: success or not
        """

        # init dict array
        unit_dict = dict_creator.DictCreator.create_dict(dict_conf)

        # unit_dict = foo.Foo(dict_conf)
        if unit_dict is None:
            self.managerlogger.logger.error("Error DictConf.dict_type[%s]" % (dict_conf.dict_type))
            return defines.ReturnCode.ERROR

        self.__dict = unit_dict

        self.managerlogger.logger.info("Done init dict manager")
        return defines.ReturnCode.SUCC


