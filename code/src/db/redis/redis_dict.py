

from src.schemas import defines
from src.systemlog  import syserrorlog
from src.systemlog  import sysmanagerlog
from src.db.dict_manager import unit_dict
import redis

class RedisDict(unit_dict.UnitDict):
    """
    implement annoy UnitDict
    
    """
    # required options
    REDIS_URL = 'redis_url'
    REDIS_PORT = 'redis_port'
    REDIS_DB = 'redis_db'

    def __init__(self,dict_conf):
        self._dict_conf = dict_conf
        self.load(dict_conf)
    


    def load(self, dict_conf):
        try:
         
            # check required configure
            if not self.valid(dict_conf):
                return defines.ReturnCode.FAIL
            # init
            if self._dict!= None:
                    self._dict.unload()
                    self._dict=None
            pool = redis.ConnectionPool(host=dict_conf.option_items[self.REDIS_URL], port=dict_conf.option_items[self.REDIS_PORT], db=dict_conf.option_items[self.REDIS_DB])
            self._dict = redis.Redis(connection_pool=pool)
            
            # do load
            self._dict_conf = dict_conf
        except Exception as e:
            return defines.ReturnCode.FAIL

        return defines.ReturnCode.SUCC

    def destroy(self):
         if self._dict is not None:
             self._dict.unload()
             self._dict = None
         if self._dict_conf is not None:
             self._dict_conf.reset()
     
         return defines.ReturnCode.SUCC

    def find_by_key(self, key):
        if self._dict is None or not self.valid(self._dict_conf):
            return None

        return self._dict.get(key)

    def set_by_key(self, key, value):
        if self._dict is None or not self.valid(self._dict_conf):
            return None

        return self._dict.set(key,value)

    def valid(self, dict_conf):
        return (dict_conf.valid() \
            and (self.REDIS_URL in dict_conf.option_items) \
            and (self.REDIS_PORT in dict_conf.option_items) \
            and (self.REDIS_PORT in dict_conf.option_items))

  

