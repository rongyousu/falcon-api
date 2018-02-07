#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
img2vector

File: img2vector.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import cv2
import numpy as np
from src.systemlog  import sysmanagerlog
from src.systemlog  import syserrorlog
import urllib

class Img2Vector():

    
    def __init__(self, dimension,file):
        self.dimension = dimension
        self.file= file
        self.managerlogger=sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger=syserrorlog.SysErrorLog(__file__)
        
    def __get_url_img_vector(self,url):
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      
        new_img=cv2.resize(gray,dsize=(int(self.dimension),int(self.dimension)))
        img_mean=cv2.mean(new_img)

        return new_img > img_mean[0]
     
    def __get_to_list(self,img_vector):
        dim_len=int(self.dimension) * int(self.dimension)
        sample=img_vector.reshape((1,int(dim_len) ))
        b=np.array(sample)
        b=b.astype(np.float)
        arrays=b.tolist()[0]
    
        return arrays

    def get_vector(self):
        v = None
        try:
             temp_v = self.__get_url_img_vector(self.file)
             v = self.__get_to_list(temp_v)
        except Exception as e:
                self.managerlogger.logger.error("getpic :: %s  error: %s" %(self.file, str(e)))
                self.errorlogger.logger.error("getpic :: %s  error: %s" %(self.file, str(e)) )
        return v 
