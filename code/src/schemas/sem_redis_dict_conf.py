#!/usr/bin/env python
# -*- coding=utf-8 -*-

from src.util import configmanager

class SemRedisDictConf(object):
    """
    configure for es dicts
    """

    # conf name
    DICT_TYPE = 'dict_type'
    DICT_NAME = 'dict_name'
    REDIS_URL = 'redis_url'
    REDIS_PORT = 'redis_port'
    REDIS_DB = 'redis_db'

    # required option
    dict_type = ''
    dict_name = ''
    redis_url = ''
    redis_port = ''
    redis_db = ''
    # optional option, <name, value>
    option_items = None

    def __init__(self, type, name,url,port,db,oi):
        self.dict_type = type
        self.dict_name = name
        self.redis_url = url
        self.redis_port = port
        self.redis_db = db
        
        self.option_items = oi

    def valid(self):
        return (self.dict_type != '' \
                and self.dict_name != '' \
                and self.redis_url != '' \
                and self.redis_port != '' \
                and self.redis_db !='' \
                and self.option_items is not None)

    def reset(self):
        self.dict_type = ''
        self.dict_name = ''
        self.redis_url = ''
        self.redis_port = ''
        self.redis_db = ''
        if self.option_items is not None:
            self.option_items.clear()

    def __str__(self):
        return "%s|%s|%s|%s|%s" \
                % (self.dict_type, self.dict_name, self.redis_url ,self.redis_port,self.redis_db)
