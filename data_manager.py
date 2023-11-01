import requests

SHEETY_ENDPOINT = 'https://api.sheety.co'


class DataManager:
    """
        This class is responsible for talking to the Google Sheet using the Sheety API.

        Attributes:
            sheety_endpoint (str): The base URL of the Sheety API for a specific Google Sheet.

        Methods:
            get_data() -> dict:
                Retrieve data from the Google Sheet.

            update_row(row_id, iataCode):
                Update a specific row in the Google Sheet with a new 'iataCode' value.

            add_row(city, lowest_price, iata_code=' ') -> str:
                Add a new row to the Google Sheet with specified 'city', 'lowest_price', and an optional 'iata_code'.
    """

    def __init__(self, username, projectname, sheet_name) -> None:
        """
            Initialize a DataManager object with the Sheety API endpoint for a specific Google Sheet.

            Args:
                username (str): Your Sheety username.
                projectname (str): Your Sheety project name.
                sheet_name (str): The name of the Google Sheet.

            Returns:
                None
        """
        self.sheety_endpoint = f"{SHEETY_ENDPOINT}/{username}/{projectname}/{sheet_name}"

    def get_data(self):
        """
            Retrieve data from the Google Sheet.

            Returns:
                dict: The data retrieved from the Google Sheet.
            Example:
                sheet_data = data_manager.get_data()
        """
        response = requests.get(url=self.sheety_endpoint)
        data = response.json()
        return data

    def update_row(self, row_id, iataCode):
        """
            Update a specific row in the Google Sheet with a new 'iataCode' value.

            Args:
                row_id (int): The ID of the row to be updated.
                iataCode (str): The new 'iataCode' value to set in the row.
            Returns:
                None
            Example:
                data_manager.update_row(row_id=1, iataCode='XYZ')
        """

        update_data = {
            'price': {
                'iataCode': iataCode
            }
        }

        response = requests.put(url=f"{self.sheety_endpoint}/{row_id}", json=update_data)
        print(response.text)

    def add_row(self, city: str, lowest_price: float, iata_code: str = ''):
        """
            Add a new row to the Google Sheet with specified 'city', 'lowest_price', and an optional 'iata_code'.

            Args:
                city (str): The name of the city to add to the Google Sheet.
                lowest_price (float): The lowest price for flights to the city.
                iata_code (str, optional): The IATA code of the city (optional, defaults to an empty string).
            Returns:
                str: The response text from the request.
            Example:
                response_text = data_manager.add_row(city='New York', lowest_price=500.0, iata_code='JFK')
        """

        new_data = {
            'price': {
                'city': city,
                'iataCode': iata_code,
                'lowestPrice': lowest_price,
            }
        }

        response = requests.post(url=self.sheety_endpoint, json=new_data)
        return response.text
