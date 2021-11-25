#This class is responsible for talking to the Flight Search API.
FLY_FROM = "BLR"
import requests
from flight_data import FlightData
from datetime import datetime, timedelta
from dateutil.relativedelta import *

class FlightSearch:

    def __init__(self,flight:FlightData):
        self.data = flight



    def search_flights(self,dest):
        self.destination = dest
        tom = datetime.today() + timedelta(days = 1)
        today = tom.strftime("%d/%m/%Y")
        search_end = tom + relativedelta(months =+ 6)
        search_end = search_end.strftime("%d/%m/%Y")


        parameters = {
            "fly_from": FLY_FROM,
            "fly_to": self.destination,
            "date_from": today,
            "date_to": search_end,
            "return_from": today,
            "return_to": search_end,
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 15
        }

        url = f"{self.data.tequila_api}v2/search"

        response = requests.get(url, params=parameters, headers=self.data.header)
        response.raise_for_status()
        flights = response.json()
        from_city = flights['data'][0]['routes'][1][0]

        complete_data = dict()
        complete_data['price'] = flights['data'][0]['price']
        complete_data['from_city'] = f"{flights['data'][0]['cityFrom']}-{flights['data'][0]['cityCodeFrom']}"
        complete_data['to_city'] = f"{flights['data'][0]['cityTo']}-{flights['data'][0]['cityCodeTo']}"
        complete_data['dept_date'] = ((flights['data'][0]['route'][0]['local_departure']).split("T"))[0]

        for a in flights['data'][0]['route']:
            if a['flyFrom'] == from_city:
                complete_data['arr_date'] = ((a['local_departure']).split("T"))[0]

        return complete_data





