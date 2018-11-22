#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
access log

File: accesslog.py
Author: 
Date: 2017/05/08 16:28
"""


import syslog


class AccessLog(syslog.SysLog):

      def __init__(self,filename):
            syslog.SysLog.__init__(self,filename,name='access')

      
