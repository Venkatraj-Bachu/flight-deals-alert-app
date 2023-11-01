import requests
import datetime
from flight_data import FlightData

TODAY = datetime.datetime.today()
SIX_MONTHS_FROM_TODAY = TODAY + datetime.timedelta(days=180)
print(TODAY.strftime("%d/%m/%Y"), SIX_MONTHS_FROM_TODAY.strftime("%d/%m/%Y"))


class FlightSearch:
    """
        A class for interacting with the Tequila Kiwi Flight Search API.

        This class allows you to search for location data and find the cheapest flight options
        based on various parameters such as departure and arrival cities, travel dates, and
        stay duration.

        Attributes:
            api_key (str): Your API key for authentication with the Tequila Kiwi Flight API.

        Methods:
            get_location_data(query):
                Retrieve location data based on a search query.

            get_cheapest_flights(from_city, to_city, min_stay_length, max_stay_length, currency):
                Find the cheapest flight options from one city to another within a specified date range
                and stay duration, returning flight details.
    """

    def __init__(self, api_key):
        """
            Initialize the FlightSearch object with an API key.

            Args:
                api_key (str): Your Tequila Kiwi API key for authentication.
            Returns:
                None
            Example:
                flight_search = FlightSearch(api_key='your_api_key_here')
        """
        self.flight_search_endpoint = f"https://api.tequila.kiwi.com"
        self.api_key = api_key
        self.header = {
            'apikey': api_key
        }

    def get_location_data(self, query) -> dict:
        """
            Retrieve location data based on a search query.

            Args:
                query (str): The search query for location data.
            Returns:
                dict: Location data for the first matching location found.
            Example:
                location_data = flight_search.get_location_data('New York')
        """
        get_location_data_endpoint = f"{self.flight_search_endpoint}/locations/query"
        location_parameters = {
            'term': query
        }
        response = requests.get(url=get_location_data_endpoint, params=location_parameters, headers=self.header)
        location_data = response.json()['locations'][0]
        return location_data

    def get_cheapest_flights(self, from_city, to_city,
                             min_stay_length, max_stay_length, currency) -> dict:
        """
            Find the cheapest flight options from one city to another within a specified date range
            and stay duration, returning flight details.

            Args:
                from_city (str): The departure city or airport code.
                to_city (str): The arrival city or airport code.
                min_stay_length (int): The minimum stay duration in nights.
                max_stay_length (int): The maximum stay duration in nights.
                currency (str): The currency code for pricing (e.g., 'USD').
            Returns:
                dict: Flight details for the cheapest available flight option.
            Example:
                cheapest_flight = flight_search.get_cheapest_flights(
                    from_city='New York',
                    to_city='London',
                    min_stay_length=5,
                    max_stay_length=10,
                    currency='USD'
                )
        """
        get_cheapest_flights_endpoint = f"{self.flight_search_endpoint}/search"
        flight_parameters = {
            'fly_from': from_city,
            'fly_to': to_city,
            'date_from': TODAY.strftime("%d/%m/%Y"),
            'date_to': SIX_MONTHS_FROM_TODAY.strftime("%d/%m/%Y"),
            'nights_in_dst_from': min_stay_length,
            'nights_in_dst_to': max_stay_length,
            'one_for_city': 1,
            'curr': currency,
        }

        response = requests.get(url=get_cheapest_flights_endpoint, params=flight_parameters, headers=self.header)
        response.raise_for_status()
        if len(response.json()['data']) == 0:
            return {}
        flight_data = response.json()['data'][0]

        flight_details = FlightData(price=flight_data['price'],
                                    departure_airport_name=flight_data['cityFrom'],
                                    departure_airport_code=flight_data['flyFrom'],
                                    arrival_airport=flight_data['cityTo'],
                                    arrival_airport_code=flight_data['flyTo'],
                                    airlines=flight_data['airlines'],
                                    pnr_count=flight_data['pnr_count'])

        flight_info = flight_details.get_flight_details()
        return flight_info
