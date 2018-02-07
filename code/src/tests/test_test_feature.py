###########################################################
#
# Copyright (c) 2017 xueersi.com, Inc. All Rights Reserved
#
###########################################################
"""
test class TestFeature

File: test_test_feature
Author: wangliang(wangliang1@100tal.com)
Date: 2017/05/11 12:03
"""

import sys
sys.path.append('../..')


import unittest

from src.schemas import dmp_feature
from src.schemas import test_feature


class TestTestFeature(unittest.TestCase):
    """
    test class TestFeature
    """
    feature = None

    def setUp(self):
        self.feature = test_feature.TestFeature()

    def tearDown(self):
        self.feature.reset()

    def test_reset__1(self):
        """
        test reset
        """
        self.feature.id = 1
        self.feature.weight = 0.8
        self.feature.timestamp = 12345
        self.feature.img_url = 'http'
        self.assertEqual(self.feature.id, 1)
        self.assertEqual(self.feature.weight, 0.8)
        self.assertEqual(self.feature.timestamp, 12345)
        self.assertEqual(self.feature.img_url, 'http')

        self.feature.reset()
        self.assertEqual(self.feature.id, 0)
        self.assertEqual(self.feature.weight, 0)
        self.assertEqual(self.feature.timestamp, 0)
        self.assertEqual(self.feature.img_url, '')

if __name__ == '__main__':
    unittest.main()

