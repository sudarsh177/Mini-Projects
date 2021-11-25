import requests
import os

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/6f39c0c5161ffe06a39e819462d7be71/flightDeals/prices"
        self.tequila_api = "http://tequila-api.kiwi.com/"
        self.api_key = os.getenv("APIKEY")
        self.details_endpoint = "https://api.sheety.co/6f39c0c5161ffe06a39e819462d7be71/flightDeals/details"

        self.header = {
            "apikey": self.api_key,
        }
        self.response = requests.get(self.sheety_endpoint)
        self.response.raise_for_status()
        self.data = self.response.json()

    def get_spreadsheet_data(self):
        return self.data['prices']

    def get_details(self):
        self.reponse1 = requests.get(self.details_endpoint)
        self.reponse1.raise_for_status()
        self.details_data = self.reponse1.json()
        return self.details_data['details']









