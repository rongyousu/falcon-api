###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
test class DictConf

File: test_dict_conf
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/10 16:26
"""

import sys
sys.path.append('../..')


import unittest

from src.schemas import defines


class TestDictConf(unittest.TestCase):
    """
    test class DictConf
    """
    dict_conf = None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_valid__1(self):
        """
        empty dict_type
        return False
        """
        dict_conf = defines.DictConf('', 'test_dict', 'addafd', '1')
        self.assertFalse(dict_conf.valid())

    def test_valid__2(self):
        """
        return True
        """
        dict_conf = defines.DictConf('annoy_dict', 'test_dict', 'addafd', '1')
        self.assertTrue(dict_conf.valid())

if __name__ == '__main__':
    unittest.main()

