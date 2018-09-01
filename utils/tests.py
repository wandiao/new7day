#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import (
    TestCase,
)

from utils import common_utils


class UtilsTestCase(TestCase):

    def setUp(self):
        pass

    def test_is_id_num_checked(self):
        right_id_number = '430624197302243733'
        self.assertTrue(common_utils.is_id_num_checked(right_id_number))
        wrong_id_number = '430624197302243734'
        self.assertFalse(common_utils.is_id_num_checked(wrong_id_number))
