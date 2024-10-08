import time
from data_manager import DataManager
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from datetime import datetime, timedelta

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

"""
Program Requirements
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send an SMS (or WhatsApp Message) to your own number using the Twilio API.

The SMS should include the departure airport IATA code, destination airport IATA code, flight price and flight dates.
"""


data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_rows()

ORIGIN_CITY = "LON"

# Fill iataCode in sheet
for flight in sheet_data:
    if flight["iataCode"]=="":
        flight["iataCode"] = flight_data.get_city_codes(flight["city"])
        time.sleep(2)
        data_manager.update_row(flight["id"], {"price":flight})

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=6*30)

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        from_airport=ORIGIN_CITY,
        to_airport=destination["iataCode"],
        from_date=tomorrow.strftime("%Y-%m-%d"),
        return_date=six_month_from_today.strftime("%Y-%m-%d")
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: $ {cheapest_flight.price}")
    time.sleep(2)