class FlightData:
    """
        This class is responsible for structuring flight data.

        Attributes:
            price (float): The price of the flight.
            departure_airport_name (str): The name of the departure airport.
            departure_airport_code (str): The code of the departure airport.
            arrival_airport (str): The name of the arrival airport.
            arrival_airport_code (str): The code of the arrival airport.
            pnr_count (int): The number of Passenger Name Records (PNR) for the flight, which indicates layovers.
            airlines (list): A list of airlines operating the flight.
        Methods:
            get_flight_details() -> dict:
                Get flight details as a dictionary, including price, departure and arrival airports, layovers, and airlines.
    """

    def __init__(self, price: float,
                 departure_airport_name: str, departure_airport_code: str,
                 arrival_airport: str, arrival_airport_code: str,
                 pnr_count: int, airlines: list):
        """
            Initialize a FlightData object with flight data.

            Args:
                price (float): The price of the flight.
                departure_airport_name (str): The name of the departure airport.
                departure_airport_code (str): The code of the departure airport.
                arrival_airport (str): The name of the arrival airport.
                arrival_airport_code (str): The code of the arrival airport.
                pnr_count (int): The number of Passenger Name Records (PNR) for the flight, indicating layovers.
                airlines (list): A list of airlines operating the flight.

            Returns:
                None
        """

        self.price = price
        self.departure_airport = departure_airport_name
        self.departure_airport_code = departure_airport_code
        self.arrival_airport = arrival_airport
        self.arrival_airport_code = arrival_airport_code
        self.pnr_count = pnr_count
        self.airlines = airlines

    def get_flight_details(self) -> dict:
        """
            Get flight details as a dictionary.

            Returns:
                dict: A dictionary containing flight details, including price, departure and arrival airports,
                layovers, and airlines.

            Example:
                details = flight_data.get_flight_details()
        """

        flight_details = {
            'price': self.price,
            'departure_airport': self.departure_airport,
            'departure_airport_code': self.departure_airport_code,
            'arrival_airport': self.arrival_airport,
            'arrival_airport_code': self.arrival_airport_code,
            'layovers': self.pnr_count - 1,
            'airlines': self.airlines,

        }

        return flight_details
