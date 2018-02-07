
#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
manager log

File: sysmanagerlog.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""


import syslog


class SysManagerLog(syslog.SysLog):

      def __init__(self,filename):
            syslog.SysLog.__init__(self,filename,name='system')

      
