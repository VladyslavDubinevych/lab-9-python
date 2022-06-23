import time
import random
from Model.Aircraft import Aircraft

class FighterJet(Aircraft):

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
    fuel_on_board, fuel_type, is_active, owner, rockets_capacity, rockets_on_board, is_for_training) -> None:
        super().__init__(model, registration, cockpit_crew, length, height, MTOW,
        OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
        engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
        fuel_on_board, fuel_type, is_active, owner)
        self.rockets_capacity = rockets_capacity
        self.rockets_on_board = rockets_on_board
        self.is_for_training = is_for_training
        

    def __str__(self) -> str:
        return super().__str__() + f"""
Rockets capacity: {self.rockets_capacity} 
Rockets on board: {self.rockets_on_board} 
Is for training: {self.is_for_training} 
"""


    def fly(self, origin, distance, fuel_burn_expected):
        if self.is_active:
            if self.is_for_training:
                print(f"""Training Fighter Jet {self.model} with registration {self.registration} is taking off from {origin} 
Rockets on board: {self.rockets_on_board} \n
""")

                fuel_burn_actual = self.fuel_burn_per_hour * (distance / self.cruise_speed) * (1.1 - random.random() * 0.2)

                if fuel_burn_actual > self.fuel_on_board:
                    print(f"Training Fighter Jet {self.model} with registration {self.registration} has crashed \n Reason: Run out of fuel")
                    self.is_active = False
                elif random.random() > 0.99995:
                    print(f"Training Fighter Jet {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                    self.is_active = False
                    
                else:
                    self.fuel_on_board -= fuel_burn_actual

                    for i in range(5):
                        time.sleep(1)
                        print(". . . ")
                    print("\n")

                    if fuel_burn_actual - fuel_burn_expected > 0:
                        print(f"""Training Fighter Jet {self.model} with registration {self.registration} successfully 
completed training 
Burned {fuel_burn_actual - fuel_burn_expected} more litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    elif fuel_burn_actual - fuel_burn_expected < 0:
                        print(f"""Training Fighter Jet {self.model} with registration {self.registration} successfully 
completed training
Burned {fuel_burn_expected - fuel_burn_actual} less litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    else:
                        print(f"""Training Fighter Jet {self.model} with registration {self.registration} successfully 
completed training
Burned {fuel_burn_actual} litres of fuel
Fuel left: {self.fuel_on_board} \n
""")
            else:
                if fuel_burn_expected <= self.fuel_on_board:
                    print(f"""Fighter Jet {self.model} with registration {self.registration} is taking off from {origin} 
Rockets on board: {self.rockets_on_board} \n
""")

                    fuel_burn_actual = self.fuel_burn_per_hour * (distance / self.cruise_speed) * (1.1 - random.random() * 0.2)

                    if fuel_burn_actual > self.fuel_on_board:
                        print(f"Fighter Jet {self.model} with registration {self.registration} has crashed \n Reason: Run out of fuel")
                        self.is_active = False
                    elif random.random() > 0.8:
                        if random.random() > 0.99995:
                            print(f"Fighter Jet {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                            self.is_active = False
                        else:
                            print(f"Fighter Jet {self.model} with registration {self.registration} has crashed \n Reason: Shot Down")
                            self.is_active = False
                    else:
                        self.fuel_on_board -= fuel_burn_actual

                        for i in range(5):
                            time.sleep(1)
                            self.shoot((random.random() * 2).__floor__() + 1)
                        print("\n")

                        if fuel_burn_actual - fuel_burn_expected > 0:
                            print(f"""Fighter Jet {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_actual - fuel_burn_expected} more litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                        elif fuel_burn_actual - fuel_burn_expected < 0:
                            print(f"""Fighter Jet {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_expected - fuel_burn_actual} less litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                        else:
                            print(f"""Fighter Jet {self.model} with registration {self.registration} successfully 
completed the mission 
Burned {fuel_burn_actual} litres of fuel
Fuel left: {self.fuel_on_board} \n
""")
                else:
                    raise Exception("Not enough fuel!")
        else: 
            raise Exception("The airframe is not active")       
                     

    def shoot(self, rockets_to_launch):
        if self.rockets_on_board - rockets_to_launch >= 0:
            print(f"Launched {rockets_to_launch} rockets!")
            self.rockets_on_board -= rockets_to_launch
        else:
            print("Not enough rockets!")

    def reload(self):
        self.rockets_on_board = self.rockets_capacity