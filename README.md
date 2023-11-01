# Flight Deals Alert System

The Flight Deals Alert System is a Python application that helps you find and get alerts for the cheapest flight deals from a specified departure city to various destination cities. It uses the Sheety API to manage destination and threshold price data in a Google Sheet and the Tequila Kiwi API to search for flight information, and it sends notifications through the Twilio API.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)

## Features

- Retrieves destination cities and threshold prices from a Google Sheet.
- Searches for the cheapest flights from a specified departure city to multiple destinations.
- Sends low price flight alerts via SMS using the Twilio API.
- Provides flexibility in specifying departure city, destination cities, and threshold prices.

## Prerequisites

Before using the Flight Deals Alert System, make sure you have the following prerequisites in place:

- Python 3.x installed on your system.
- Required Python packages (can be installed using `pip`):
  - `requests` for making HTTP requests
  - (Other packages as mentioned in your code)

## Installation

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

## Configuration

To configure and use the Flight Deals Alert System, follow these steps:

1. Obtain the necessary API keys and credentials:

   - Sheety API credentials for accessing Google Sheets.
   - Tequila Kiwi API credentials for flight information.
   - Twilio API credentials for sending SMS alerts.

2. Set up the Google Sheet:

   - Create a Google Sheet with the necessary structure for destination cities and threshold prices.

3. Update the configuration in your code:

   - Replace the placeholder values in your code with the actual API keys and credentials.
   - Customize the departure city and other parameters as needed.

## Usage

1. Run the main program to start the Flight Deals Alert System:

2. The system will retrieve destination cities and threshold prices from the Google Sheet.

3. It will search for the cheapest flights to these destination cities in the next six months.

4. If a flight's price is below the specified threshold, it will send an SMS alert via Twilio.

5. Monitor the terminal for status updates and alerts.
