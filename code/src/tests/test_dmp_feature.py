###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
test class DmpFeature

File: test_dmp_feature
Author:
Date: 2017/05/10 16:26
"""

import sys
sys.path.append('../..')


import unittest

from src.schemas import dmp_feature


class TestDmpFeature(unittest.TestCase):
    """
    test class DmpFeature
    """
    feature = None

    def setUp(self):
        self.feature = dmp_feature.DmpFeature()

    def tearDown(self):
        self.feature.reset()

    def test_reset__1(self):
        """
        test reset
        """
        self.feature.id = 1
        self.feature.weight = 0.8
        self.feature.timestamp = 12345
        self.assertEqual(self.feature.id, 1)
        self.assertEqual(self.feature.weight, 0.8)
        self.assertEqual(self.feature.timestamp, 12345)

        self.feature.reset()
        self.assertEqual(self.feature.id, 0)
        self.assertEqual(self.feature.weight, 0)
        self.assertEqual(self.feature.timestamp, 0)

if __name__ == '__main__':
    unittest.main()

