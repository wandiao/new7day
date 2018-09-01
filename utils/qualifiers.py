#!/usr/bin/env python
# *- coding: utf-8 -*-


from munch import Munch

OBDInfoQualifiers_A = Munch({
    'vin': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
    # whole_vehicle_info
    'car_status': 'b01',  # 车辆状态 defines.CAR_STATUSES
    'charge_status': 'b02',  # 充电状态
    'running_mode': 'b03',
    'speed': 'b04',
    'mileage': 'b05',
    'voltage': 'b06',
    'current': 'b07',
    'soc': 'b08',
    'dc_dc_status': 'b09',
    'gear': 'b10',
    'can_brake': 'b11',
    'can_drive': 'b12',
    'insulation_resistance': 'b13',
    'accelerator': 'b14',
    'brake': 'b15',
    # motor_info
    'motor_count': 'c01',
    'motor_info_list': 'c02',
    # fuel_cell_info
    'fuel_cell_voltage': 'd01',
    'fuel_cell_current': 'd02',
    'cell_fuel_consumption_rate': 'd03',
    'fuel_cell_temperature_probes_count': 'd04',
    'probe_temperature_list': 'd05',
    'hydrogen_system_highest_temperature': 'd06',
    'hydrogen_system_highest_temperature_probe_code': 'd07',
    'hydrogen_highest_concentration': 'd08',
    'hydrogen_highest_concentration_sensor_code': 'd09',
    'hydrogen_maximum_pressure': 'd10',
    'hydrogen_maximum_pressure_sensor_code': 'd11',
    'high_voltage_dc_dc_status': 'd12',
    # engine_info
    'engine_status': 'e01',
    'crankshaft_speed': 'e02',
    'engine_fuel_consumption_rate': 'e03',
    # vehicle_location_info
    'lng': 'f01',
    'lat': 'f02',
    'address': 'f03',
    'is_location_valid': 'f04',
    'south_or_north': 'f05',
    'east_or_west': 'f06',
    # extreme_value_info
    'maximum_voltage_battery_subsystem_code': 'g01',
    'maximum_voltage_battery_cell_code': 'g02',
    'battery_cell_voltage_highest_value': 'g03',
    'minimum_voltage_battery_subsystem_code': 'g04',
    'minimum_voltage_battery_cell_code': 'g05',
    'battery_cell_voltage_lowest_value': 'g06',
    'maximum_temperature_subsystem_code': 'g07',
    'maximum_temperature_probe_code': 'g08',
    'maximum_temperature_value': 'g09',
    'minimum_temperature_subsystem_code': 'g10',
    'minimum_temperature_probe_code': 'g11',
    'minimum_temperature_value': 'g12',
    # alert_info
    'highest_alert_level': 'h01',
    'battery_faults_count': 'h02',
    'battery_fault_codes': 'h03',
    'motor_faults_count': 'h04',
    'motor_fault_codes': 'h05',
    'engine_faults_count': 'h06',
    'engine_fault_codes': 'h07',
    'other_faults_count': 'h08',
    'other_fault_codes': 'h09',
    'temperature_difference_alert': 'h10',
    'battery_high_temperature_alert': 'h11',
    'energy_storage_device_high_voltage_alert': 'h12',
    'energy_storage_device_low_voltage_alert': 'h13',
    'soc_low_alert': 'h14',
    'single_battery_high_voltage_alert': 'h15',
    'single_battery_low_voltage_alert': 'h16',
    'soc_too_high_alert': 'h17',
    'soc_jumping_alert': 'h18',
    'rechargeable_energy_storage_system_mismatch_alert': 'h19',
    'battery_cell_consistency_low_alert': 'h20',
    'insulation_alert': 'h21',
    'dc_dc_temperature_alert': 'h22',
    'braking_system_alert': 'h23',
    'dc_dc_status_alert': 'h24',
    'motor_controller_temperature_alert': 'h25',
    'hvil_alert': 'h26',
    'motor_temperature_alert': 'h27',
    'energy_storage_device_over_charge_alert': 'h28',
    # rechargeable_energy_storage_device_info
    'resd_subsystem_count': 'i01',
    'resd_subsystem_voltage_list': 'i02',
    'resd_subsystem_temperature_list': 'i03',
    # 燃油车发动机及车辆数据补充采集
    'ACC_status': 'j01',  # ACC状态 0 or 1
    'engine_total_running_time': 'j02',  # 发动机总运行时间
    'engine_rotate_speed': 'j03',  # 发动机转速
    'engine_torque': 'j04',  # 扭矩
    'battery_voltage': 'j05',  # 电瓶电压（精确到 0.1 V）
    'coolant_temperature': 'j06',  # 冷却液温度
    'urea_liquid_level': 'j07',  # 尿素液位
    'car_running_speed': 'j08',  # 车辆行驶速度
    'fuel_consumption_rate': 'j09',  # 瞬时油耗
    'total_mileage': 'j10',  # 总里程数据
    'total_idling_time': 'j11',  # 怠速时间数据（总怠速时间）
    'total_ignition_time': 'j12',  # 点火次数数据（总点火时间）
    # 锁车协议扩展报警
    'extend_faults_count': 'k01',  # 其他故障总数
    'extend_fault_codes': 'k02',  # 其他故障列表
    'low_electricity': 'k03',  # 低电报警
    'main_power_down': 'k04',  # 主电源断电报警
    'CAN_communication_fault': 'k05',  # CAN 通信故障
    'positioning_antenna_cut': 'k06',  # 定位天线断开
    'positioning_antenna_short_circuit': 'k07',  # 定位天线短路
    'gps_antenna_cut_down': 'k08',  # GPS天线剪短报警
    # 锁车协议锁车状态
    'TBOX_activate_status': 'l01',  # TBOX 激活状态
    'ECU_activate_status': 'l02',  # ECU 激活状态
    'TBOX_ECU_bind_status': 'l03',  # TBOX 与 ECU 绑定状态
    'TBOX_ECU_handshake_status': 'l04',  # TBOX 与 ECU 握手状态
    'passive_lock_status': 'l05',  # 被动锁车状态
})
OBDInfoQualifiers_B = Munch({
    'hex_data': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
})

AlertRecordQualifiers_A = Munch({
    'vin': 'a01',
    'unique_code': 'a02',
    'first_alert_time': 'a03',
    'obd_time': 'a04',
    'receive_time': 'a05',
    'publication_number': 'a06',
    # b
    'alert_level': 'b01',
    'alarm_type': 'b02',  # alert or fault
    'alert_type': 'b03',
    'source_type': 'b04',  # battery, motor, engine, other
    'fault_code': 'b05',
    'alert_status': 'b06',  # alerting or cleared
    'alert_times': 'b07',
    'clear_alert_time': 'b08',
    # c
    'alert_lat': 'c01',
    'alert_lng': 'c02',
    'alert_address': 'c03',
    'first_alert_lat': 'c04',
    'first_alert_lng': 'c05',
    'first_alert_address': 'c06',
    'has_regeoed': 'c07',
    # d
    'handle_plan_status': 'd01',  # unhandled, handling, handled
    'handle_result_status': 'd02',  # unreported, reported
    'handle_plan_data': 'd03',
    'handle_result_data': 'd04',
    # e
    'platform_company_id': 'e01',
    'main_factory_id': 'e02',
    'division_id': 'e03',
    'local_platform_id': 'e04',
})
AlertRecordQualifiers_B = Munch({
    'alert_hex_data': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
})

AlertHistoryQualifiers_A = Munch({
    'vin': 'a01',
    'unique_code': 'a02',
    'obd_time': 'a03',
    'receive_time': 'a04',
    # b
    'alert_level': 'b01',
    'alarm_type': 'b02',  # alert or fault
    'alert_type': 'b03',
    'source_type': 'b04',  # battery, motor, engine, other
    'fault_code': 'b05',
    # c
    'alert_lat': 'c01',
    'alert_lng': 'c02',
    'alert_address': 'c03',
    # d, 暂时没有
    # e
    'platform_company_id': 'e01',
    'main_factory_id': 'e02',
    'division_id': 'e03',
    'local_platform_id': 'e04',
})
AlertHistoryQualifiers_B = Munch({
    'alert_hex_data': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
})

CarInfoQualifiers_A = Munch({
    'vin': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
    # b
    'iccid': 'b01',
    'info_type': 'b02',
    'login_serial_number': 'b03',
    'logout_serial_number': 'b04',
    # c
    'rechargeable_energy_storage_system_encoding_length': 'c01',
    'rechargeable_energy_storage_subsystems_count': 'c02',
    'rechargeable_energy_storage_system_encoding': 'c03',
})
CarInfoQualifiers_B = Munch({
    'hex_data': 'a01',
    'obd_time': 'a02',
    'receive_time': 'a03',
})

CarStatisticalDataQualifiers_A = Munch({
    # a
    'vin': 'a01',
    'date': 'a02',
    # b
    'total_mileage': 'b01',
    'total_time': 'b02',
    'alert_count': 'b03',
    'fault_count': 'b04',
})
CarStatisticalDataQualifiers_B = Munch({
    # a
    'alert_info_row_keys': 'a01',
    'date': 'a02',
})

ReversedOBDInfoQualifiers_A = {
    v: k for k, v in OBDInfoQualifiers_A.iteritems()
}
ReversedAlertRecordQualifiers_A = {
    v: k for k, v in AlertRecordQualifiers_A.iteritems()
}
ReversedAlertHistoryQualifiers_A = Munch({
    v: k for k, v in AlertHistoryQualifiers_A.iteritems()
})
ReversedCarInfoQualifiers_A = Munch({
    v: k for k, v in CarInfoQualifiers_A.iteritems()
})
ReversedCarStatisticalDataQualifiers_A = Munch({
    v: k for k, v in CarStatisticalDataQualifiers_A.iteritems()
})


def get_column_name(cf, qualifier):
    return '%s:%s' % (cf, qualifier)
