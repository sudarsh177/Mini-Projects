import requests
import os
from twilio.rest import Client

account_sid = os.getenv("SID")
auth_token = os.getenv("TOKEN")
from_no = os.getenv("FROM")
to_no = os.getenv("TO") # Add your phone number here
lat = os.getenv("LAT")  # Add your Latitude here
lon = os.getenv("LON") # Add your Longitude here


parameters = {
    "lat" : lat,
    "lon" : lon,
    "appid" : "7b2d40ab4ab2f639125eb322a0862adb",
    "exclude": "current,minutely,daily",
}

response = requests.get(url = "https://api.openweathermap.org/data/2.5/onecall", params= parameters)
response.raise_for_status()
data = response.json()
hourly_data = []

for a in range(12):
    temp = data["hourly"][a]["weather"][0]
    hourly_data.append(temp)


for a in hourly_data:
    if a["id"] < 700:
        print("yes")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Its going to rain today. Remember to make arrangements. \nSudarh177",
            from_=from_no,
            to=to_no
        )
        print(message.status)





