import pandas as pd
from car import Car, CarType


class Region:
    def __init__(self, region_id, region_type):
        self.id = region_id
        self.region_type = region_type
        self.cars = []

    def add_cars_from_config(self, car_dict, tech_data: pd.DataFrame):
        for car_type_name, car_count in car_dict.items():
            # create new car type
            # TODO: add charging curve and implement in code
            bat_cap = tech_data.at[car_type_name, 'battery_capacity']
            consumption = tech_data.at[car_type_name, 'energy_consumption']
            charging_capacity_slow = tech_data.at[car_type_name, 'max_charging_capacity_slow']
            charging_capacity_fast = tech_data.at[car_type_name, 'max_charging_capacity_fast']
            charging_capacity = {'slow': charging_capacity_slow, 'fast': charging_capacity_fast}
            # TODO: add charging curve
            car_type = CarType(car_type_name, bat_cap, charging_capacity, {}, consumption)
            for car_number in range(car_count):
                # create new car objects
                # TODO: randomize starting SoC and location, charging station availability
                new_car = Car(1, car_type, False, False, car_number)
                self.cars.append(new_car)
