flights = [
    {
        "flight_number": "SK1401",
        "destination": "Stockholm",
        "departure_time": "06:15",
        "gate": "A12",
        "passengers": 148,
        "maximum_capacity": 180,
        "delay_minutes": 0,
        "cancelled": False,
    },
    {
        "flight_number": "DY310",
        "destination": "Oslo",
        "departure_time": "07:40",
        "gate": "",
        "passengers": 186,
        "maximum_capacity": 186,
        "delay_minutes": 25,
        "cancelled": False,
    },
    {
        "flight_number": "AY1542",
        "destination": "Helsinki",
        "departure_time": "08:05",
        "gate": "C7",
        "passengers": 92,
        "maximum_capacity": 150,
        "delay_minutes": 10,
        "cancelled": False,
    },
    {
        "flight_number": "LH2458",
        "destination": "Frankfurt",
        "departure_time": "09:20",
        "gate": "D2",
        "passengers": 0,
        "maximum_capacity": 220,
        "delay_minutes": 0,
        "cancelled": True,
    },
    {
        "flight_number": "BA768",
        "destination": "London",
        "departure_time": "10:50",
        "gate": "A3",
        "passengers": 201,
        "maximum_capacity": 210,
        "delay_minutes": 45,
        "cancelled": True,
    },
    {
        "flight_number": "AF1756",
        "destination": "Paris",
        "departure_time": "12:10",
        "gate": "B9",
        "passengers": 134,
        "maximum_capacity": 174,
        "delay_minutes": 5,
        "cancelled": False,
    },
    {
        "flight_number": "KL1134",
        "destination": "Amsterdam",
        "departure_time": "13:35",
        "gate": "C1",
        "passengers": 167,
        "maximum_capacity": 180,
        "delay_minutes": 80,
        "cancelled": False,
    },
    {
        "flight_number": "IB3681",
        "destination": "Madrid",
        "departure_time": "15:00",
        "gate": "D8",
        "passengers": 73,
        "maximum_capacity": 160,
        "delay_minutes": 0,
        "cancelled": False,
    },
    {
        "flight_number": "AZ612",
        "destination": "Rome",
        "departure_time": "16:25",
        "gate": "A7",
        "passengers": 0,
        "maximum_capacity": 200,
        "delay_minutes": 0,
        "cancelled": True,
    },
    {
        "flight_number": "LX1258",
        "destination": "Zurich",
        "departure_time": "17:45",
        "gate": "B2",
        "passengers": 119,
        "maximum_capacity": 140,
        "delay_minutes": 15,
        "cancelled": False,
    },
    {
        "flight_number": "TK1784",
        "destination": "Istanbul",
        "departure_time": "19:10",
        "gate": "C14",
        "passengers": 212,
        "maximum_capacity": 230,
        "delay_minutes": 120,
        "cancelled": False,
    },
    {
        "flight_number": "SK2024",
        "destination": "Copenhagen",
        "departure_time": "21:30",
        "gate": "D5",
        "passengers": 98,
        "maximum_capacity": 150,
        "delay_minutes": 0,
        "cancelled": False,
    },
    {
        "flight_number": "SK2026",
        "destination": "London",
        "departure_time": "14:30",
        "gate": "B4",
        "passengers": 132,
        "maximum_capacity": 180,
        "delay_minutes": 25,
        "cancelled": False,
    },
]

# Print all flights

# print(f"Total flights: {len(flights)}")
# for flight in flights:
#     print(flight)

# print("--------------------------------")
# Print all flights in a table format

# for index, flight in enumerate(flights):
#     print((f"{index}. {flight['flight_number']} - {flight['destination']} - {flight['departure_time']} - {flight['gate']}"))

# print("--------------------------------")
# Print all flights that are cancelled, severely delayed, delayed, slightly delayed, or on time


# for flight in flights:
#     if flight['cancelled']:
#         print(f"{flight['flight_number']} - {flight['destination']} - CANCELLED")
#         continue
#     elif flight['delay_minutes'] >= 60:
#         print(f"{flight['flight_number']} - {flight['destination']} - SEVERELY DELAYED")
#         continue
#     elif flight['delay_minutes'] >= 20:
#         print(f"{flight['flight_number']} - {flight['destination']} - DELAYED")
#         continue
#     elif flight['delay_minutes'] > 0:
#         print(f"{flight['flight_number']} - {flight['destination']} - SLIGHTLY DELAYED")
#         continue
#     else:
#         print(f"{flight['flight_number']} - {flight['destination']} - ON TIME")

# print("--------------------------------")

# print(f"Total number of scheduled flights: {len(flights)}") # 13

# print("--------------------------------")

# count_cancelled = 0
# for flight in flights:
#     if flight["cancelled"]:
#         count_cancelled = count_cancelled +1
# print(f"Total number of cancelled flights: {count_cancelled}") # 2

# print("--------------------------------")

# count_delayed = 0
# for flight in flights:
#     if flight["delay_minutes"] > 0:
#         count_delayed = count_delayed +1
# print(f"Total number of delayed flights: {count_delayed}") # 8

# print("--------------------------------")

# count_on_time = 0
# for flight in flights:
#     if flight["delay_minutes"] == 0:
#         count_on_time = count_on_time + 1
# print(f"Total number of on time flights: {count_on_time}") # 5

# print("--------------------------------")

# count_passengers = 0
# for flight in flights:
#     count_passengers = count_passengers + flight["passengers"]
# print(f"Total number of passengers: {count_passengers}") # 1562

# print("--------------------------------")

# larger_number_passengers = 0
# for flight in flights:
#     if flight["passengers"] > larger_number_passengers:
#         larger_number_passengers = flight["passengers"]
# print(f"The flight with the largest number of passengers is: {larger_number_passengers}") # 212

# print("--------------------------------")

# on_maximum_capacity = 0
# for flight in flights:
#     if flight["passengers"] > flight["maximum_capacity"] * 0.8:
#         on_maximum_capacity = on_maximum_capacity + 1
# print(f"The number of flights on maximum capacity is: {on_maximum_capacity}") # 6

# print("--------------------------------")

# Part 5 - Search a flight by flight number

# flight_number = input("Enter the flight number: ") # SK2026
# for flight in flights:
#     if flight_number == flight["flight_number"]:
#         print(f"Destination: {flight['destination']}")
#         print(f"Departure: {flight['departure_time']}")
#         print(f"Gate: {flight['gate']}")
#         print(f"Passengers: {flight['passengers']}")
#         print(f"Status: {'CANCELLED' if flight['cancelled'] else 'DELAYED' if flight['delay_minutes'] > 0 else 'ON TIME'}")
#         break
# else:
#     print("Flight not found")

#print("--------------------------------")

# Part 7 - Gate overview

# terminals = ["A", "B", "C"]
# gate_number = [1, 2, 3, 4]

# # Generate all possible combinations of terminals and gate numbers
# for terminal in terminals:
#     for gate in gate_number:
#         print(f"Gate {terminal}{gate}")

# print("--------------------------------")

# Part 8 - Interactive Airport menu

# menu = input("Enter a menu option (1 - 6): 1. View all flights, 2. View delayed flights, 3. View cancelled flights, 4. Search a flight, 5. View flight statistics, 6. Quit: ")

# while menu != "6":
#     if menu == "1":
#         print(flights)
#     elif menu == "2":
#         found_delayed = False
#         for flight in flights:
#             if flight["delay_minutes"] > 0 and flight["cancelled"] == False:
#                 print(flight)
#                 found_delayed = True
#         if not found_delayed:
#             print("No delayed flights")
#     elif menu == "3":
#         found_cancelled = False
#         for flight in flights:
#             if flight["cancelled"]:
#                 print(flight)
#                 found_cancelled = True
#         if not found_cancelled:
#             print("No cancelled flights")
#     elif menu == "4":
#         flight_number = input("Enter the flight number: ") # SK2026
#         for flight in flights:
#             if flight_number == flight["flight_number"]:
#                 print(flight)
#                 break
#         else:
#             print("Flight not found")
#     elif menu == "5":
#         print(f"Total number of scheduled flights: {len(flights)}") # 13

#         count_cancelled = 0
#         for flight in flights:
#             if flight["cancelled"]:
#                 count_cancelled = count_cancelled +1
#         print(f"Total number of cancelled flights: {count_cancelled}") # 2

#         count_delayed = 0
#         for flight in flights:
#             if flight["delay_minutes"] > 0:
#                 count_delayed = count_delayed +1
#         print(f"Total number of delayed flights: {count_delayed}") # 8

#         count_on_time = 0
#         for flight in flights:
#             if flight["delay_minutes"] == 0:
#                 count_on_time = count_on_time + 1
#         print(f"Total number of on time flights: {count_on_time}") # 5
#     else:
#         print("Invalid menu option!")
#     menu = input("Enter a menu option (1 - 6): 1. View all flights, 2. View delayed flights, 3. View cancelled flights, 4. Search a flight, 5. View flight statistics, 6. Quit: ")

# print("Program closed!")


# FINAL CHALLENGE - Display a summary of the flights

print("--------------------------------")
print("AIRPORT OPERATIONS REPORT")
print("--------------------------------")
print(" ")
print(f"Scheduled flights: {len(flights)}") # 13

count_cancelled = 0
for flight in flights:
    if flight["cancelled"]:
        count_cancelled = count_cancelled +1
print(f"Cancelled flights: {count_cancelled}") # 2

count_delayed = 0
for flight in flights:
    if flight["delay_minutes"] > 0:
        count_delayed = count_delayed +1
print(f"Delayed flights: {count_delayed}") # 8

count_on_time = 0
for flight in flights:
    if flight["delay_minutes"] == 0:
        count_on_time = count_on_time + 1
print(f"On time flights: {count_on_time}") # 5

count_passengers = 0
for flight in flights:
    count_passengers = count_passengers + flight["passengers"]
print(f"Passengers today: {count_passengers}") # 1562
print(" ")
print("--------------------------------")
print(" ")
larger_number_passengers = 0
busiest_flight = None
for flight in flights:
    if flight["passengers"] > larger_number_passengers:
        larger_number_passengers = flight["passengers"]
        busiest_flight = flight
print("Busiest flight: ")
print(busiest_flight)
print(" ")
print("--------------------------------")
print(" ")
print("Flights above 80% capacity:")
print(" ")
for flight in flights:
    if flight["passengers"] > flight["maximum_capacity"] * 0.8:
        print(f"{flight['flight_number']} - {flight['destination']}")
