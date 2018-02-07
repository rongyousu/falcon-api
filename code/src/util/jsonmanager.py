#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
json manager

File: jsonmanager.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import json

def get_message(message):
        json_str=json.dumps(message,default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_str=json_str.replace('\n','').replace('\t','')
        return json_str
