#!/usr/bin/env python
# coding=utf-8

from owl.models import Truck as TruckModel
from defines import (
    TRUCK_COLOR,
    TRUCK_TYPE,
)


def get_truck_info(truck_id):
    truck = TruckModel.objects.filter(id=truck_id)
    if truck:
        truck = truck.values().first()
        truck['truck_color'] = TRUCK_COLOR.get(truck['truck_color'])
        truck['truck_type'] = TRUCK_TYPE.get(truck['truck_type'])
        return truck
    else:
        return None


def get_user_trucks(user_id):
    truck_ids = [
        truck.id for truck in TruckModel.objects.filter(user_id=user_id)
    ]
    trucks = [get_truck_info(truck_id) for truck_id in truck_ids]
    return trucks
