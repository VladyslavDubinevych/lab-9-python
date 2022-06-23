import time
import random
from Model.Aircraft import Aircraft

class PassengerPlane(Aircraft):

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
    fuel_on_board, fuel_type, is_active, owner, passengers_capacity) -> None:
        super().__init__(model, registration, cockpit_crew, length, height, MTOW,
        OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
        engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
        fuel_on_board, fuel_type, is_active, owner)
        self.passengers_capacity = passengers_capacity
        

    def __str__(self) -> str:
        return super().__str__() + f"""
Passengers capacity: {self.passengers_capacity} 
"""


    def fly(self, origin, destination, distance, passengers_on_board, fuel_burn_expected, destination_weather):
        if self.is_active and passengers_on_board <= self.passengers_capacity:
            if fuel_burn_expected <= self.fuel_on_board:
                print(f"""Aircraft {self.model} with registration {self.registration} is taking off from {origin} 
Passengers on board: {passengers_on_board} 
Weather in {destination} is {destination_weather} \n
""")

                fuel_burn_actual = self.fuel_burn_per_hour * (distance / self.cruise_speed) * (1.1 - random.random() * 0.2)

                if fuel_burn_actual > self.fuel_on_board:
                    print(f"Aircraft {self.model} with registration {self.registration} has crashed \n Reason: Run out of fuel")
                    self.is_active = False
                elif random.random() > 0.99995:
                    print(f"Aircraft {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                    self.is_active = False
                else:
                    self.fuel_on_board -= fuel_burn_actual

                    for i in range(5):
                        time.sleep(1)
                        print(". . . ")
                    print("\n")

                    if fuel_burn_actual - fuel_burn_expected > 0:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} 
Burned {fuel_burn_actual - fuel_burn_expected} more litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    elif fuel_burn_actual - fuel_burn_expected < 0:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} 
Burned {fuel_burn_expected - fuel_burn_actual} less litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    else:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} 
Burned {fuel_burn_actual} litres of fuel
Fuel left: {self.fuel_on_board} \n
""")
            else:
                raise Exception("Not enough fuel!")
        else:
            if self.is_active:
                raise Exception("Too much passengers")
            else:
                raise Exception("The airframe is not active")       
                     