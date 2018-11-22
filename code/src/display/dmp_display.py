#!/usr/bin/env python
# -*- coding=utf-8 -*-


from src.schemas import dmp_feature_set
from src.schemas import dmp_response
from src.display import dmp_display_conf
from src.systemlog import sysmanagerlog
from src.systemlog import syserrorlog
from src.schemas import accessdictmodel
from src.systemlog import accesslog

import time


class DmpDisplay(object):
    """
     display base class
     deal features and return response
    """

    #save conf_file
    __dmp_display_manager = None

    #save access_modle
    access_model = None

    def __init__(self, config, access_model):
        """
         init log
         init and load display_manager
        """
        self.managerlogger = sysmanagerlog.SysManagerLog(__file__)
        self.errorlogger = syserrorlog.SysErrorLog(__file__)
        self.access_model = access_model

        self.managerlogger.logger.info('Start init DmpDisplay for config')
        
        try:
            self.__dmp_display_manager = dmp_display_conf.DmpDisplayManager(access_model)
            length = self.__dmp_display_manager.load_conf(config)

            self.managerlogger.logger.info('End init DmpDisplay for config')

        except Exception as e:
            self.managerlogger.logger.warning('Failed init DmpDisplay for config')
            self.errorlogger.logger.warning('Failed init DmpDisplay for config')

    def display(self, features, request, conf_name = 'default'):
        """
         display api:get repronse  
        """

        self.managerlogger.logger.info('Start do Display for [%s]'\
                %(conf_name))
        
        try:
            display_conf = self.__dmp_display_manager.find_conf(conf_name)

            filter_features = self.__do_filter(features, display_conf)
            
            sort_features = self.__do_sort(filter_features, display_conf)
 
            self.managerlogger.logger.info('End to Display for [%s]'\
                    %(conf_name))

        except Exception as e:
            sort_features = None

            self.managerlogger.logger.warning('Failed to Display for [%s]'\
                    %(conf_name))
            self.errorlogger.logger.warning('Failed to Display for [%s]'\
                    %(conf_name))

        return self.__do_features2response(sort_features, request)

    def __do_filter(self, sort_features, display_conf):
        """
         filter by display_conf
        """
        self.managerlogger.logger.info('Start to filter for [%s]'\
                %(display_conf.conf_name))

        feature_set = dmp_feature_set.DmpFeatureSet()
        try:
            start_time = int(round(time.time()*1000))
            for feature in sort_features:

                if feature.id >= display_conf.min_id and feature.id <= display_conf.max_id \
                        and feature.weight >= display_conf.min_weight \
                        and feature.weight <= display_conf.max_weight \
                        and feature.timestamp >= display_conf.min_timestamp \
                        and feature.timestamp <= display_conf.max_timestamp:
                    feature_set.push_feature(feature)

            end_time = int(round(time.time()*1000))

            self.managerlogger.logger.info('End to filter for conf[%s]' 
                    %(display_conf.conf_name))
            self.access_model.set_log_dic_key('display:filter_time:', str(end_time - start_time))

 
            return feature_set

        except Exception as e:

            self.managerlogger.logger.warning('Failed to filter for conf[%s]'\
                    %(display_conf.conf_name))
            self.errorlogger.logger.warning('Failed to filter for conf[%s]'\
                    %(display_conf.conf_name))

            return None

    def __do_sort(self, features, display_conf):
        """
         sort features by default
        """
        self.managerlogger.logger.info('Start sort by conf[%s]'\
                %(display_conf.conf_name))

        start_time = int(round(time.time()*1000))
        try:
            
            features.sort()

            end_time = int(round(time.time()*1000))
            
            self.managerlogger.logger.info('End sort by conf[%s]' \
                %(display_conf.conf_name))

            self.access_model.set_log_dic_key('display:sort_time:', str(end_time - start_time))
            
            return features

        except Exception as e:
            self.managerlogger.logger.warning('Failed sort by conf[%s]' \
                    %(display_conf.conf_name))
            self.errorlogger.logger.warning('Failed sort by conf[%s]' \
                    %(display_conf.conf_name))
            
            return None
    
    def __do_features2response(self, features, request):
        """
         deal features 2 response
        """
        self.managerlogger.logger.info('Start features2response for \
                 [%s]' %(request.request_id))
        
        feature_list = []

        response = dmp_response.DmpResponse()
        response.request_id = request.request_id

        if request.request_num <= 0 or features is None:
            response.msg = 'execute failed'
            response.status = False
            response.test_features = feature_list
            return response
        
        try:
            start_time = int(round(time.time()*1000))

            size = 0
            for feature in features:

                if size < request.request_num:
                    feature_list.append(feature)
                else:
                    break

                size = size + 1

            response.msg = 'execute success'
            response.status = True
            response.test_features = feature_list

            end_time = int(round(time.time()*1000))
            
            self.managerlogger.logger.info('End to features2response for requstid[%s]'\
                    %(request.request_id))
            self.access_model.set_log_dic_key('display:response', response)
            self.access_model.set_log_dic_key('display:response_time:', str(end_time - start_time))

            return response

        except Exception as e:
            response.msg = 'execute failed'
            response.status = False
            response.test_features = feature_list

            self.managerlogger.logger.warning('Failed to features2response for requestid[%s]'\
                    %(request.request_id))
            self.errorlogger.logger.warning('Failed to features2response for requestid[%s]'\
                    %(request.request_id))

            return response

