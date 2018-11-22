

from annoy import AnnoyIndex

from util.defines import ReturnCode


class UnitDict(object):
    """
    dict operating implement
    """

    # dict instance
    _dict = None

    def __init__(self):
        self._dict = None

    @property
    def instance(self):
        return self._dict

    def load(self, dict_conf):
        print "In UnitDict: load dict[%s]" %(dict_conf.dict_name)
        return ReturnCode.SUCC

    def destroy(self):
        print "In UnitDict: destroy dict[%s]" %(dict_conf.dict_name)
        return ReturnCode.SUCC

