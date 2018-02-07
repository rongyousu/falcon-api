#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
pic_sim_dbreload.py 

File: ***.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/18 10:30
"""

import json
import urllib

result=0
try:
     url='http://0.0.0.0:8000/api/manager/dbreload/reload_img_tests_annoy_dict?appid=1495158789&appkey=0bea2cb49c1614e5dd8868bd56f9b6cf'
     resp = urllib.urlopen(url)
     content = resp.readline()

     mjson=json.loads(content)
     
     db_nums= int(mjson['db_nums'])

     if db_nums>1 :
          result=0
     else:
          result=1
     
except Exception as e:
     result=1
     #print str(e)

print result
