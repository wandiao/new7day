#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from utils.deconstruct_package import do_parse_data


class TestDeconstructPackage(unittest.TestCase):

    def setUp(self):
        self.bind_report = '##\t\xfeUGWZYW386SO038620\x01\x00I\x12\x07\x1f\x11\x17\x0fU00000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x9d'
        self.unbind_report = '##\t\xfeUGWZYW386SO038620\x01\x00I\x12\x07\x1f\x11\x172\xaa00000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0000\x00\x01\x02]'
        self.lock_report = '##\t\xfeUGWZYW386SO038620\x01\x00G\x12\x07\x1f\x11\x18-\x8000000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00k'
        self.unlock_report = '##\t\xfeUGWZYW386SO038620\x01\x00G\x12\x07\x1f\x11\x19\x00\x9000000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02U'
        self.speed_report = '##\t\xfeUGWZYW386SO038620\x01\x00G\x12\x07\x1f\x11\x19\n\x8100000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00O'
        self.torque_report = '##\t\xfeUGWZYW386SO038620\x01\x00G\x12\x07\x1f\x11\x19\x14\x8200000000000000000000\xab\xc1#EUGWZYW386SO038620burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00S'

    def test_do_parse_data_bind(self):
        data = do_parse_data(self.bind_report)
        self.assertEqual(data.start, '##')
        self.assertEqual(data.command_flag, 0x09)
        self.assertEqual(data.answer_flag, 0xFE)
        self.assertEqual(data.unique_code, 'UGWZYW386SO038620')
        self.assertEqual(data.encrypto_method, '\x01')
        self.assertEqual(data.length, 73)
        self.assertEqual(data.checksum, 157)

        payload = data.payload
        self.assertEqual(payload.command_id, 0x55)
        self.assertEqual(payload.iccid, '00000000000000000000')
        self.assertEqual(payload.obd_id, 'abc12345')
        self.assertEqual(payload.vin, 'UGWZYW386SO038620')
        self.assertEqual(payload.platform_id, 'burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(payload.ecu_type, '\x00\x01')
        self.assertEqual(payload.current_state, 0)
        self.assertEqual(payload.execute_state, 0)
        self.assertEqual(payload.failure_reason, 0)

    def test_do_parse_data_unbind(self):
        data = do_parse_data(self.unbind_report)
        self.assertEqual(data.start, '##')
        self.assertEqual(data.command_flag, 0x09)
        self.assertEqual(data.answer_flag, 0xFE)
        self.assertEqual(data.unique_code, 'UGWZYW386SO038620')
        self.assertEqual(data.encrypto_method, '\x01')
        self.assertEqual(data.length, 73)
        self.assertEqual(data.checksum, 93)

        payload = data.payload
        self.assertEqual(payload.command_id, 0xAA)
        self.assertEqual(payload.iccid, '00000000000000000000')
        self.assertEqual(payload.obd_id, 'abc12345')
        self.assertEqual(payload.vin, 'UGWZYW386SO038620')
        self.assertEqual(payload.platform_id, 'burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(payload.ecu_type, '00')
        self.assertEqual(payload.current_state, 0)
        self.assertEqual(payload.execute_state, 1)
        self.assertEqual(payload.failure_reason, 2)

    def test_deconstruct_report_payload_lock(self):
        payload = deconstruct_report_payload(self.lock_report_payload)
        self.assertEqual(payload.command_id, 0x80)
        self.assertEqual(payload.iccid, '00000000000000000000')
        self.assertEqual(payload.obd_id, 'abc12345')
        self.assertEqual(payload.vin, 'UGWZYW386SO038620')
        self.assertEqual(payload.platform_id, 'burnish\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
        self.assertEqual(payload.current_state, 1)
        self.assertEqual(payload.execute_state, 0)
        self.assertEqual(payload.failure_reason, 0)


if __name__ == "__main__":
    unittest.main()
