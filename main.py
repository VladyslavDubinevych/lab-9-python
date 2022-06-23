from Model.Bomber import Bomber
from Model.FighterJet import FighterJet
from Model.Glider import Glider
from Model.PassengerPlane import PassengerPlane
from Model.SportsPlane import SportsPlane

def main():

    bomber = Bomber("Boeing B-52", "60-0058", 5, 48.5, 12.4, 219600, 120000, 56.4, 181610, 14200,
    819, 45000, "Pratt & Whitney TF33-P-3/103", "18/11/2021", 55024, 11050, 130000, "Jet A1", True, "US Air Force", 50, 30)
    fighter_jet = FighterJet("Mikoyan Gurevich MiG-29UB 1-13", "57 WHITE", 1, 17.32, 4.73, 18000, 14900, 11.36, 3500, 1430,
    1200, 45000, "Klimov RD-33", "18/05/2022", 21433, 3000, 3000, "Jet A1", True, "Ukrainian Air Force", 6, 4, False)
    glider = Glider("Test Glider Gl-2", "N22369", 2, 17, 2.3, 7000, 4000, 19.2, 300,
    200, 10000, "NONE", "11/03/1998", 19083, False, "LOT Flight Academy", "By plane")
    passenger_plane = PassengerPlane("Boeing 737-8H6(WL)", "UR-SQA", 2, 39.5, 12.5, 79016, 41413, 35.8, 26022, 5436,
    842, 37000, "CFMI CFM56-7B26", "11/04/2022", 9855, 2583, 11000, "Jet A1", True, "SkyUp Airlines", 189)
    sports_plane = SportsPlane("Aeroprakt A-69", "UR-COOL", 2, 15, 3, 15000, 6000, 10, 8000, 950,
    700, 27000, "Motor Sich MS-12", "11/06/2021", 4110, 4000, 6000, "Jet B2", True, "Andrii Shpak", "Ukrainian Eagles")

    while True:
        print("""Aircraft types:
1. Bomber
2. Fighter Jet
3. Glider
4. Passenger Plane
5. Sports Plane
""")
        planetype = input("Enter aircraft type: ")
        if planetype == "1":
            print("""Commands:
1. Fly
2. Reload
3. Refuel
4. Do maintnance
5. Change ownership
6. Print
7. Quit
""")
            command = input("Enter command: ")
            if command == "1":
                bomber.fly("Lviv", 1000, 8000)
            elif command == "2":
                bomber.reload()
            elif command == "3":
                bomber.refuel("Jet A1", 10000)
            elif command == "4":
                bomber.do_maintnance("26/05/2022")
            elif command == "5":
                bomber.change_ownership("US Air Museum")
            elif command == "6":
                print(bomber)
            elif command == "7":
                break
            else:
                print("Wrong command, please write again!")
        elif planetype == "2":
            print("""Commands:
1. Fly
2. Reload
3. Refuel
4. Do maintnance
5. Change ownership
6. Print
7. Quit
""")
            command = input("Enter command: ")
            if command == "1":
                fighter_jet.fly("Kyiv", 500, 2300)
            elif command == "2":
                fighter_jet.reload()
            elif command == "3":
                fighter_jet.refuel("Jet A1", 300)
            elif command == "4":
                fighter_jet.do_maintnance("26/05/2022")
            elif command == "5":
                fighter_jet.change_ownership("Polish Air Force")
            elif command == "6":
                print(fighter_jet)
            elif command == "7":
                break
            else:
                print("Wrong command, please write again!")
        elif planetype == "3":
            print("""Commands:
1. Fly
2. Do maintnance
3. Change ownership
4. Print
5. Quit
""")
            command = input("Enter command: ")
            if command == "1":
                glider.fly("Karpaty", "Lviv", 200)
            elif command == "2":
                glider.do_maintnance()
            elif command == "3":
                glider.change_ownership("Chernihiv Aero School")
            elif command == "4":
                print(glider)
            elif command == "5":
                break
            else:
                print("Wrong command, please write again!")
        elif planetype == "4":
            print("""Commands:
1. Fly
2. Refuel
3. Do maintnance
4. Change ownership
5. Print
6. Quit
""")
            command = input("Enter command: ")
            if command == "1":
                passenger_plane.fly("Warsaw", "Paris", 1100, 163, 4120, "Cloudy, +22 C")
            elif command == "2":
                passenger_plane.refuel("Jet A1", 5000)
            elif command == "3":
                passenger_plane.do_maintnance("26/05/2022")
            elif command == "4":
                passenger_plane.change_ownership("Bees Airline")
            elif command == "5":
                print(passenger_plane)
            elif command == "6":
                break
            else:
                print("Wrong command, please write again!")
        elif planetype == "5":
            print("""Commands:
1. Fly
2. Refuel
3. Do maintnance
4. Change ownership
5. Print
6. Quit
""")
            command = input("Enter command: ")
            if command == "1":
                sports_plane.fly("Lviv", "Lviv", 200, 1500)
            elif command == "2":
                sports_plane.refuel("Jet A1", 2000)
            elif command == "3":
                sports_plane.do_maintnance("26/05/2022")
            elif command == "4":
                sports_plane.change_ownership("Oleh Yatskiv")
            elif command == "5":
                print(sports_plane)
            elif command == "6":
                break
            else:
                print("Wrong command, please write again!")
        else:
            print("Wrong type, please write again!")

        


if __name__ == '__main__':
    main()