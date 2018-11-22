#!/usr/bin/env python
# -*- coding=utf-8 -*-


class SemParamsFeature(object):
    """
    Define base feature
    """
    def __init__(self):
        self.request_id = ''
        self.key = ''
        self.value = ''
        self.old_value=''
        self.type = ''  #get /set
        self.timestamp=0
        self.status= 0

    def update(self, other):
        if isinstance(other, SemParamsFeature):
            self.value = other.value
            self.type = 'set'
            self.timestamp = other.timestamp
 

    def reset(self):
        self.request_id = ''
        self.key = ''
        self.value = ''
        self.old_value=''
        self.type = ''
        self.timestamp = 0

    def __str__(self):
        return "%s|%s|%s|%s|%s" %(self.key, self.old_value,self.value,self.type, self.timestamp)

