#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 , Inc. All Rights Reserved
#
###########################################################
"""
main schedule

File: dmp_server.py
Autho
Date: 2017/05/05 16:28
"""

from service import xes_test_service as xt_serv


if __name__ == '__name__':
    """
    start all service
    """

    # falcon.API instances are callable WSGI apps
    application = falcon.API()

    # start xes test service
    application.add_route('/tests', xt_serv.XesTestService())

