


from src.schemas import defines
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog


class UnitDict(object):
    """
    dict operating implement
    """

    # dict instance
    _dict = None
    # dict conf
    _dict_conf = None

    def __init__(self):
        # init log
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)

        self._dict = None
        self._dict_conf = None

    def __del__(self):
        self.destroy()

    @property
    def instance(self):
        return self._dict

    @property
    def dict_type(self):
        if self._dict_conf is None:
            return ''
        else:
            return self._dict_conf.dict_type

    @property
    def dict_name(self):
        if self._dict_conf is None:
            return ''
        else:
            return self._dict_conf.dict_name

    @property
    def reload_cmd(self):
        if self._dict_conf is None:
            return ''
        else:
            return self._dict_conf.reload_cmd

    def load(self, dict_conf):
        self._dict_conf = dict_conf
        self.managerlogger.logger.info("Done dict[%s] load" %(self.dict_name))
        return defines.ReturnCode.SUCC

    def destroy(self):
        if self._dict is not None:
            self.managerlogger.logger.info("Done dict[%s] destroy" %(self.dict_name))
        return defines.ReturnCode.SUCC

    def __str__(self):
        if self._dict_conf is None:
            return ''
        else:
            return "%s|%s|%s|%s" % ( \
                    self._dict_conf.dict_type, \
                    self._dict_conf.dict_name, \
                    self._dict_conf.dict_md5, \
                    self._dict_conf.reload_cmd)

