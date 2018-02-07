###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
Annoy Dict Definition

File: annoy_dict.py
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/08 15:35
"""

from src.schemas import defines
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog
from src.db.dict_manager import unit_dict
#from src.algorithm.annoy import AnnoyIndex
from annoy import AnnoyIndex

class AnnoyDict(unit_dict.UnitDict):
    """
    implement annoy UnitDict
    search all vectors to find K Nearrest Neightbors
    """
    # required options
    DIMENSION = 'dimension'
    METRIC = 'metric'
    SEARCH_K = 'search_k'

    def __init__(self,dict_conf):
        self._dict_conf = dict_conf
        self.load(dict_conf)
    


    def load(self, dict_conf):
        try:
         
            # check required configure
            if not self.valid(dict_conf):
                return defines.ReturnCode.FAIL
            # init
            #if self._dict is not None:
            #        self._dict.unload()
            #        self._dict = None
            self._dict = AnnoyIndex(
                    int(dict_conf.option_items[self.DIMENSION]),
                    metric = dict_conf.option_items[self.METRIC])
            # do load
            if not self._dict.load(dict_conf.full_path):
                return defines.ReturnCode.FAIL
            print 'annoy ok load'
            self._dict_conf = dict_conf
        except Exception as e:
            return defines.ReturnCode.FAIL

        return defines.ReturnCode.SUCC

    def destroy(self):
        pass
         #if self._dict is not None:
         #    self._dict.unload()
         #    self._dict = None
         #if self._dict_conf is not None:
         #    self._dict_conf.reset()
     
        return defines.ReturnCode.SUCC

    def find_by_key(self, test_id, max_size):
        if self._dict is None or not self.valid(self._dict_conf):
            return None

        return self._dict.get_nns_by_item(int(test_id), max_size,
                    int(self._dict_conf.option_items[self.SEARCH_K]),
                    include_distances=True)

    def find_by_vector(self, vector, max_size):
        if self._dict is None or not self.valid(self._dict_conf):
            return None

        return self._dict.get_nns_by_vector(vector, max_size,
                    int(self._dict_conf.option_items[self.SEARCH_K]),
                    include_distances=True)

    def valid(self, dict_conf):
        return (dict_conf.valid() \
            and (self.DIMENSION in dict_conf.option_items) \
            and (self.METRIC in dict_conf.option_items) \
            and (self.SEARCH_K in dict_conf.option_items))

    def __getstate__(self):
        """Return state values to be pickled."""
        return (self._dict ,self._dict_conf)

    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        
        self._dict,self._dict_conf = state

        self.load(self._dict_conf)
  

