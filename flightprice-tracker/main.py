#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import  NotificationManager

flight_data = FlightData()
manage_data = DataManager(flight_data)

manage_data.add_details()

# manage_data.initialise_iatacodes()

flight_search = FlightSearch(flight_data)
data = flight_data.get_spreadsheet_data()
details = flight_data.get_details()
msg = NotificationManager()

for entry in data:
    code = entry['iataCode']
    flight_results = flight_search.search_flights(code)
    if flight_results['price'] <= entry['lowestPrice']:
        print(flight_results)
        # for sending SMS
        # msg.send_message(flight_results)

        #for sending emails
        msg.send_email(flight_results, details)




