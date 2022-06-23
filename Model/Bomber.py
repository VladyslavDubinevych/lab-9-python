import time
import random
from Model.Aircraft import Aircraft

class Bomber(Aircraft):

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
    fuel_on_board, fuel_type, is_active, owner, bombs_capacity, bombs_on_board) -> None:
        super().__init__(model, registration, cockpit_crew, length, height, MTOW,
        OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
        engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
        fuel_on_board, fuel_type, is_active, owner)
        self.bombs_capacity = bombs_capacity
        self.bombs_on_board = bombs_on_board
        

    def __str__(self) -> str:
        return super().__str__() + f"""
Bombs capacity: {self.bombs_capacity}
Bombs on board: {self.bombs_on_board} 
"""


    def fly(self, origin, distance, fuel_burn_expected):
        if self.is_active:
            if fuel_burn_expected <= self.fuel_on_board:
                print(f"""Bomber {self.model} with registration {self.registration} is taking off from {origin} 
Bombs on board: {self.bombs_on_board} \n
""")
                fuel_burn_actual = self.fuel_burn_per_hour * (distance / self.cruise_speed) * (1.1 - random.random() * 0.2)

                if fuel_burn_actual > self.fuel_on_board:
                    print(f"Bomber {self.model} with registration {self.registration} has crashed \n Reason: Run out of fuel")
                    self.is_active = False
                elif random.random() > 0.8:
                    if random.random() > 0.99995:
                        print(f"Bomber {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                        self.is_active = False
                    else:
                        print(f"Bomber {self.model} with registration {self.registration} has crashed \n Reason: Shot Down")
                        self.is_active = False
                else:
                    self.fuel_on_board -= fuel_burn_actual

                    for i in range(5):
                        time.sleep(1)
                        self.drop_bombs((random.random() * 4).__floor__() + 1)
                    print("\n")

                    if fuel_burn_actual - fuel_burn_expected > 0:
                        print(f"""Bomber {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_actual - fuel_burn_expected} more litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    elif fuel_burn_actual - fuel_burn_expected < 0:
                        print(f"""Bomber {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_expected - fuel_burn_actual} less litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    else:
                        print(f"""Bomber {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_actual} litres of fuel
Fuel left: {self.fuel_on_board} \n
""")
            else:
                raise Exception("Not enough fuel!")
        else: 
            raise Exception("The airframe is not active")       
                     

    def drop_bombs(self, bombs_to_drop):
        if self.bombs_on_board - bombs_to_drop >= 0:
            print(f"Launched {bombs_to_drop} bombs!")
            self.bombs_on_board -= bombs_to_drop
        else:
            print("Not enough bombs!")

    def reload(self):
        self.bombs_on_board = self.bombs_capacity
        