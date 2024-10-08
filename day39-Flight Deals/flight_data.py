class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, from_airport, to_airport, from_date, return_date):
        self.price = price
        self.from_airport = from_airport
        self.to_airport = to_airport
        self.from_date = from_date
        self.return_date = return_date

        
def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flights data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
        
    first_flight = data['data'][0]
    lowest_price = float(first_flight['price']['grandTotal'])
    from_airport = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    to_airport = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    from_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
    
    cheapest_flight = FlightData(lowest_price, from_airport, to_airport, from_date, return_date)
    
    # Comparison of flight prices
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
