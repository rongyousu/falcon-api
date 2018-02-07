###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
test class DualDict

File: test_dual_dict
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/16 17:34
"""

import sys
sys.path.append('../..')

import unittest

from src.schemas import defines
from src.db.dict_manager import dual_dict


class TestDualDict(unittest.TestCase):
    """
    test class DualDict
    """
    du_dict = None
    dict_conf = None

    def setUp(self):
        self.du_dict = dual_dict.DualDict()
        self.dict_conf = defines.DictConf(
                'annoy_dict', 'img_tests_annoy_dict', 'reload_annoy_dict',
                './tests_data/img_tests_annoy_dict',
                {
                    "dimension":10,
                    "metric":"euclidean",
                    "search_k":-1
                })

    def tearDown(self):
        del self.du_dict
        del self.dict_conf

    def test_unit_dict__1(self):
        """
        empty dual dict
        return None
        """
        self.assertTrue(self.du_dict.unit_dict is None)

    def test_dict_type__1(self):
        """
        empty dual dict
        return ''
        """
        self.assertEqual(self.du_dict.dict_type, '')

    def test_dict_name__1(self):
        """
        empty dual dict
        return ''
        """
        self.assertEqual(self.du_dict.dict_name, '')

    def test_reload_cmd__1(self):
        """
        empty dual dict
        return ''
        """
        self.assertEqual(self.du_dict.reload_cmd, '')

    def test_load__1(self):
        """
        load fail
        error conf
        """
        self.dict_conf.dict_type = 'unknown'
        self.assertEqual(self.du_dict.load(self.dict_conf), defines.ReturnCode.ERROR)
        self.assertTrue(self.du_dict.unit_dict is None)

    def test_load__2(self):
        """
        load succ
        """
        self.assertEqual(self.du_dict.load(self.dict_conf), defines.ReturnCode.SUCC)
        self.assertFalse(self.du_dict.unit_dict is None)
        self.assertEqual(self.du_dict.dict_type, 'annoy_dict')
        self.assertEqual(self.du_dict.dict_name, 'img_tests_annoy_dict')
        self.assertEqual(self.du_dict.reload_cmd, 'reload_annoy_dict')

    def test_reload__1(self):
        """
        reload fail
        do not need reload
        """
        self.assertEqual(self.du_dict.load(self.dict_conf), defines.ReturnCode.SUCC)
        self.assertFalse(self.du_dict.unit_dict is None)
        self.assertEqual(self.du_dict.dict_name, 'img_tests_annoy_dict')

        self.assertEqual(self.du_dict.reload(), defines.ReturnCode.FAIL)

if __name__ == '__main__':
    unittest.main()

