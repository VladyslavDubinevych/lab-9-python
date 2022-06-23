import time
import random


class Aircraft():

    def __init__(self, model, registration, cockpit_crew, length, height, MTOW,
    OEW, wingspan, fuel_capacity, range, cruise_speed, cruise_altitude,
    engines, last_maintnance_date, flying_hours, fuel_burn_per_hour,
    fuel_on_board, fuel_type, is_active, owner) -> None:
        self.model = model
        self.registration = registration
        self.cockpit_crew = cockpit_crew
        self.length = length
        self.height = height
        self.MTOW = MTOW
        self.OEW = OEW
        self.wingspan = wingspan
        self.fuel_capacity = fuel_capacity
        self.range = range
        self.cruise_speed = cruise_speed
        self.cruise_altitude = cruise_altitude
        self.engines = engines
        self.last_maintnance_date = last_maintnance_date
        self.flying_hours = flying_hours
        self.fuel_burn_per_hour = fuel_burn_per_hour
        self.fuel_on_board = fuel_on_board
        self.fuel_type = fuel_type
        self.is_active = is_active
        self.owner = owner


    def __str__(self) -> str:
        return f"""Aircraft {self.model} with registration {self.registration} specifications:
Cockpit crew: {self.cockpit_crew}
Length: {self.length}m
Height: {self.height}m
MTOW(Maximum TakeOff Weight): {self.MTOW}kg
OEW(Operating Empty Weight): {self.OEW}kg
Wingspan: {self.wingspan}m
Fuel capacity: {self.fuel_capacity}l
Range: {self.range}km
Cruise speed: {self.cruise_speed}km/h
Cruise altitude: {self.cruise_altitude}ft
Engines: {self.engines}
Last maintnance date: {self.last_maintnance_date}
Total hours flown: {self.flying_hours}h
Fuel burn per hour: {self.fuel_burn_per_hour}kgs
Owner: {self.owner} """


    def fly(self, origin, destination, distance, passengers_on_board, fuel_burn_expected, destination_weather):
        if self.is_active:
            if fuel_burn_expected <= self.fuel_on_board:
                print(f"""Aircraft {self.model} with registration {self.registration} is taking off from {origin} 
Passengers on board: {passengers_on_board} 
Weather in {destination} is {destination_weather} 
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
                    
                    if fuel_burn_actual - fuel_burn_expected > 0:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} \n
Burned {fuel_burn_actual - fuel_burn_expected} more kgs of fuel than expected
Fuel left: {self.fuel_on_board}
""")
                    elif fuel_burn_actual - fuel_burn_expected < 0:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} \n
Burned {fuel_burn_expected - fuel_burn_actual} less kgs of fuel than expected
Fuel left: {self.fuel_on_board}
""")
                    else:
                        print(f"""Aircraft {self.model} with registration {self.registration} arrived to {destination} \n
Burned {fuel_burn_actual} kgs of fuel
Fuel left: {self.fuel_on_board}
""")
            else:
                raise Exception("Not enough fuel!")
        else:
            raise Exception("The airframe is not active")        


    def refuel(self, fuel_type, fuel_amount):
        if self.is_active:
            if self.fuel_type == fuel_type:
                if self.fuel_on_board + fuel_amount >= self.fuel_capacity:
                    self.fuel_on_board = self.fuel_capacity
                else:
                    self.fuel_on_board += fuel_amount
                print(f"""Aircraft {self.registration} has been successfully refueled \n
Fuel on board: {self.fuel_on_board}
""")
            else:
                raise Exception("Wrong fuel type!")
        else:
            raise Exception("The airframe is not active") 


    def do_maintnance(self, current_date):
        if self.is_active:
            print(f"Aircraft {self.registration} has been successfully maintnanced \n")
            self.last_maintnance_date = current_date
        else:
            raise Exception("The airframe is not active")

    
    def change_ownership(self, new_owner):
        self.owner = new_owner
        print(f"Aircraft {self.registration} is now owned by {self.owner} \n")

