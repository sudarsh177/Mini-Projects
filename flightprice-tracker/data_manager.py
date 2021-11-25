import requests
from flight_data import FlightData


class DataManager:
    def __init__(self, flight : FlightData):
        self.sheetdata = flight

    def initialise_iatacodes(self):
        count = 2
        for entry in self.sheetdata.data["prices"]:

            parameters = {
                "term": f"{entry['city']}"
            }

            code_query_url = f"{self.sheetdata.tequila_api}locations/query"
            respond = requests.get(code_query_url, params=parameters, headers=self.sheetdata.header)
            respond.raise_for_status()
            data1 = respond.json()
            city_code = data1["locations"][0]['code']

            code = {
                "price": {
                    "iataCode": city_code
                }
            }
            add = requests.put(f"https://api.sheety.co/6f39c0c5161ffe06a39e819462d7be71/flightDeals/prices/{count}", json=code)
            count += 1

    def add_details(self):
        f_name= input("Enter your first name: \n")
        l_name = input("Enter your last name: \n")
        email_id = input("Enter your email id: \n")
        url = "https://api.sheety.co/6f39c0c5161ffe06a39e819462d7be71/flightDeals/details"

        add_details = {
            'detail': {
                'firstName': f_name,
                'lastName': l_name,
                'email':email_id
            }
        }

        add = requests.post(url, json=add_details)
        add.raise_for_status()
