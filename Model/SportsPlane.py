import time
import random
from Model.Aircraft import Aircraft

class SportsPlane(Aircraft):

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
    fuel_on_board, fuel_type, is_active, owner, team) -> None:
        super().__init__(model, registration, cockpit_crew, length, height, MTOW,
        OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
        engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
        fuel_on_board, fuel_type, is_active, owner)
        self.team = team
        

    def __str__(self) -> str:
        return super().__str__() + f"""
Team: {self.team} 
"""


    def fly(self, origin, destination, distance, fuel_burn_expected):
        if self.is_active:
            if fuel_burn_expected <= self.fuel_on_board:
                print(f"Sports aircraft {self.model} with registration {self.registration} is taking off from {origin} \n")

                fuel_burn_actual = self.fuel_burn_per_hour * (distance / self.cruise_speed) * (1.1 - random.random() * 0.2)

                if fuel_burn_actual > self.fuel_on_board:
                    print(f"Sports aircraft {self.model} with registration {self.registration} has crashed \n Reason: Run out of fuel")
                    self.is_active = False
                elif random.random() > 0.99995:
                    print(f"Sports aircraft {self.model} with registration {self.registration} has crashed \n Reason: Unknown")
                    self.is_active = False
                else:
                    self.fuel_on_board -= fuel_burn_actual

                    for i in range(5):
                        time.sleep(1)
                        self.do_tricks()
                    print("\n")
                    
                    if fuel_burn_actual - fuel_burn_expected > 0:
                        print(f"""Sports aircraft {self.model} with registration {self.registration} landed in {destination}
Burned {fuel_burn_actual - fuel_burn_expected} more litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    elif fuel_burn_actual - fuel_burn_expected < 0:
                        print(f"""Sports aircraft {self.model} with registration {self.registration} landed in {destination}
Burned {fuel_burn_expected - fuel_burn_actual} less litres of fuel than expected
Fuel left: {self.fuel_on_board} \n
""")
                    else:
                        print(f"""Sports aircraft {self.model} with registration {self.registration} landed in {destination}
Burned {fuel_burn_actual} litres of fuel
Fuel left: {self.fuel_on_board} \n
""")
            else:
                raise Exception("Not enough fuel!")
        else:
            raise Exception("The airframe is not active")    


    def do_tricks():
        if random() > 0.5:
            print("Done a barrel roll")
        else:
            print("Done a lowpass")   
                     