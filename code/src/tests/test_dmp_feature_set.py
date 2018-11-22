
###########################################################
#
# Copyright (c) 2017, Inc. All Rights Reserved
#
###########################################################
"""
test class DmpFeatureSet

File: test_dmp_feature_set

Date: 2017/05/10 16:26
"""

import sys
sys.path.append('../..')


import unittest

from src.schemas import defines
from src.schemas import dmp_feature
from src.schemas import dmp_feature_set


class TestDmpFeatureSet(unittest.TestCase):
    """
    test class DmpFeatureSet
    """
    feature = None
    feature_set = None

    def setUp(self):
        self.feature = dmp_feature.DmpFeature()
        self.feature_set = dmp_feature_set.DmpFeatureSet()

    def tearDown(self):
        self.feature.reset()
        if self.feature_set is not None:
            self.feature_set.clear()
        feature_set = None

    def test_feature__1(self):
        """
        feature not exist
        return None
        """
        self.assertTrue(self.feature_set.feature(0) is None)
        self.assertTrue(self.feature_set.feature(1) is None)

    def test_feature__2(self):
        """
        feature not exist
        return None
        """
        # add first feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        # add second feature
        self.feature = dmp_feature.DmpFeature()
        self.feature.id = 1
        self.feature.weight = 0.8
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)

        self.assertFalse(self.feature_set.feature(0) is None)
        self.assertFalse(self.feature_set.feature(1) is None)

    def test_feature_at__1(self):
        """
        invalid index
        return None
        """
        self.assertEqual(self.feature_set.feature_at(0), None)

    def test_feature_at__2(self):
        """
        get feature at index
        return feature
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

        self.assertFalse(self.feature_set.feature_at(0) is None)
        self.assertEqual(self.feature_set.feature_at(0).id, 0)

    def test_push_feature__1(self):
        """
        push None feature
        Error
        """
        self.assertEqual(self.feature_set.push_feature(None), 
                defines.ReturnCode.ERROR)
        self.assertEqual(len(self.feature_set), 0)

    def test_push_feature__2(self):
        """
        push new feature
        SUCCESS
        """
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

    def test_push_feature__3(self):
        """
        push duplicated feature
        FAIL
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

        # add duplicated feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.FAIL)
        self.assertEqual(len(self.feature_set), 1)

    def test_push_feature__4(self):
        """
        push duplicated feature, overwrite
        SUCCESS
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)
       
        # add duplicated feature
        # if exist, overwrite
        self.feature.weight = 0.5
        self.assertEqual(self.feature_set.push_feature(self.feature, True),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)
        self.assertEqual(self.feature_set.feature_at(0).weight, 0.5)

    def test_push_feature__5(self):
        """
        push new features
        SUCCESS
        """
        # add first feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)
       
        # add second feature
        self.feature = dmp_feature.DmpFeature()
        self.feature.id = 1
        self.feature.weight = 0.8
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 2)

        self.assertEqual(self.feature_set.feature_at(0).id, 0)
        self.assertEqual(self.feature_set.feature_at(1).id, 1)

    def test_pop_feature__1(self):
        """
        empty featureset
        FAIL
        """
        self.assertEqual(self.feature_set.pop_feature(), defines.ReturnCode.FAIL)

    def test_pop_feature__2(self):
        """
        SUCCESS
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

        self.assertEqual(self.feature_set.pop_feature(), defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 0)

    def test_del_feature__1(self):
        """
        None feature
        FAIL
        """
        self.assertEqual(self.feature_set.del_feature(None), defines.ReturnCode.FAIL)

    def test_del_feature__2(self):
        """
        feature not exist
        FAIL
        """
        self.assertEqual(self.feature_set.del_feature(self.feature), defines.ReturnCode.FAIL)

    def test_del_feature__3(self):
        """
        SUCCESS
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

        self.assertEqual(self.feature_set.del_feature(self.feature), defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 0)

    def test_clear__1(self):
        """
        SUCCESS
        """
        # add a new feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 1)

        self.assertEqual(self.feature_set.clear(), defines.ReturnCode.SUCC)
        self.assertEqual(len(self.feature_set), 0)

    def test_sort__1(self):
        """
        SUCCESS
        """
        # add first feature
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        # add second feature
        self.feature = dmp_feature.DmpFeature()
        self.feature.id = 1
        self.feature.weight = 0.8
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)
        # add third feature
        self.feature = dmp_feature.DmpFeature()
        self.feature.id = 2
        self.feature.weight = 0.8
        self.feature.timestamp = 2
        self.assertEqual(self.feature_set.push_feature(self.feature),
                defines.ReturnCode.SUCC)

        # check feature set
        self.assertEqual(self.feature_set.feature_at(0).id, 0)
        self.assertEqual(self.feature_set.feature_at(1).id, 1)
        self.assertEqual(self.feature_set.feature_at(2).id, 2)
        # check feature id dict
        self.assertEqual(self.feature_set.feature(0).id, 0)
        self.assertEqual(self.feature_set.feature(1).id, 1)
        self.assertEqual(self.feature_set.feature(2).id, 2)

        # sort
        self.assertEqual(self.feature_set.sort(), defines.ReturnCode.SUCC)

        # check sorted feature set
        self.assertEqual(self.feature_set.feature_at(0).id, 2)
        self.assertEqual(self.feature_set.feature_at(1).id, 1)
        self.assertEqual(self.feature_set.feature_at(2).id, 0)

        # check updated feature id dict
        self.assertEqual(self.feature_set.feature(0).id, 0)
        self.assertEqual(self.feature_set.feature(1).id, 1)
        self.assertEqual(self.feature_set.feature(2).id, 2)

if __name__ == '__main__':
    unittest.main()

