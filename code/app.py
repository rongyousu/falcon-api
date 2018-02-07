#!/usr/bin/env python
# -*- coding=utf-8 -*-
###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
falcon api 主要逻辑区

File: app.py
Author: surongyou(surongyou@100tal.com)
Date: 2017/05/08 16:28
"""

import falcon
import sys

from src.schemas import defines
from src.db.treenode import annoy_dict
from src.db.dict_manager import dict_manager


from src.middleware.context import ContextMiddleware
from src.middleware.auth import AuthMiddleware

from src.resources  import mainresource
from src.resources.manager import managerresource

class MyService(falcon.API):
    def __init__(self, cfg):
        super(MyService, self).__init__(
            middleware=[ContextMiddleware(),AuthMiddleware()]
        )
        self.req_options.auto_parse_form_urlencoded=True
        self.cfg = cfg

        #逻辑代码区

        # Build an object to manager our db connections.        
        
        all_dicts = dict_manager.DictManager()

        if defines.ReturnCode.SUCC != all_dicts.load_dicts('./config/dict_manager.conf'):
              print "Fail to load all dicts"
              sys.exit()
 

        # Create user resources
        mainServerResource = mainresource.Main_Resource(all_dicts,cfg['trigger'],cfg['manager'],cfg['display'])

        
        #create manager resources
        managerResource = managerresource.Manager_Resource(all_dicts,cfg['trigger'])
        # Build routes
        self.add_route('/api/getdata/{app_name}',mainServerResource)
        self.add_route('/api/manager/{app_name}/{app_cmd}',managerResource)
          

    def start(self):
        """ A hook to when a Gunicorn worker calls run()."""
        pass

    def stop(self, signal):
        """ A hook to when a Gunicorn worker starts shutting down. """
        pass
