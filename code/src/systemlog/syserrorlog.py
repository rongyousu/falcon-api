#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
error log

File: syserrorlog.py
Author
Date: 2017/05/08 16:28
"""


import syslog


class SysErrorLog(syslog.SysLog):

      def __init__(self,filename):
            syslog.SysLog.__init__(self,filename,name='error')

      
