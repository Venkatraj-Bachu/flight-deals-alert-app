# Import necessary modules
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

####---------------------------------------------- DECLARE CONSTANTS ----------------------------------------------####

# Constants for SHEETY, TEQUILA KIWI, and TWILIO APIs

# SHEETY API Details
USERNAME = '<ENTER YOUR SHEETY USERNAME>'
PROJECTNAME = '<FILE_NAME>'
SHEET_NAME = '<SHEET_NAME>'

# TEQUILA KIWI API Details
FLIGHT_SEARCH_API = "<YOUR_TEQUILA_API>"

# TWILIO API Details
TWILIO_ACCOUNT_SID = "<YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "<YOUR_TWILIO_AUTH_TOKEN>"
TWILIO_PHONE = "<YOUR_TWILIO_PHONE>"
MY_PHONE = '<YOUR_PHONE>'

# Departure Airport
DEPARTURE_FROM = 'Charlotte'

####------------------------- GET DESTINATIONS AND THRESHOLD PRICES FROM THE GOOGLE SHEET -------------------------####

# Create a DataManager object to interact with the Google Sheet
# Comment lines 30-33 and uncomment lines 35-36 to hard code the cities and the threshold prices.
data_manager = DataManager(username=USERNAME, projectname=PROJECTNAME, sheet_name=SHEET_NAME)
price_data = data_manager.get_data()['prices']
cities = [(entry['id'], entry['city'], entry['lowestPrice']) for entry in price_data]

# cities = [(1, 'Paris', 2000), (2, 'Berlin', 2000), (3, 'Tokyo', 2000), (4, 'Sydney', 2000), (5, 'Istanbul', 2000),
#           (7, 'New York', 2000), (8, 'San Francisco', 2000), (9, 'Cape Town', 2000), (10, 'Hyderabad', 2000)]


####------------------- GET IATA CODES FOR THE DESTINATIONS CITIES AND UPDATE THE GOOGLE SHEET -------------------####

flight_search = FlightSearch(api_key=FLIGHT_SEARCH_API)

departure_city_code = flight_search.get_location_data(DEPARTURE_FROM)['code']  # To get the departure city IATA code

for city_id, city_name, threshold_price in cities:
    city_data = flight_search.get_location_data(city_name)
    destination_city = city_data['code']
    data_manager.update_row(row_id=city_id, iataCode=destination_city)
    print("pricing coming up.....\n")

####--------------- SEARCH FOR THE CHEAPEST FLIGHTS TO THE DESTINATION CITIES IN THE NEXT SIX MONTHS ---------------####

    cheapest_flight = flight_search.get_cheapest_flights(from_city='CLT', to_city=destination_city,
                                                         min_stay_length=11, max_stay_length=12,
                                                         currency='USD')

    if cheapest_flight == {}:
        print(f"No flights from {DEPARTURE_FROM} to {city_name}")
    else:
        price = cheapest_flight['price']
        total_flights = cheapest_flight['layovers']
        airlines = cheapest_flight['airlines']

####--------------------------------------- SEND LOW PRICE ALERTS AS AN SMS ---------------------------------------####

        twilio = NotificationManager(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        if price <= threshold_price:
            message_status = twilio.send_message(message=f'Cheap flight Alert from {DEPARTURE_FROM} to {city_name} '
                                                         f'for just {price}$\n'
                                                         f'No. of layovers: {total_flights}\n'
                                                         f'Airlines: {airlines}\n',
                                                 from_phone=TWILIO_PHONE, to_phone=MY_PHONE)
        else:
            message_status = twilio.send_message(message=f'found no cheap flight from {DEPARTURE_FROM} to {city_name}',
                                                 from_phone=TWILIO_PHONE, to_phone=MY_PHONE)
