import requests
from datetime import datetime
import smtplib
import os

FROMMAIL = os.getenv['FROM_MAIL']
PASSWORD = os.getenv['PSWD']
TOMAIL = os.getenv['TO_MAIL']

MY_LAT = os.getenv['MYLAT'] # Your latitude
MY_LONG = os.getenv['MYLONG'] # Your longitude



response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def in_range(lat,lng,par_lat,par_lng):
    if par_lat > lat -5 and par_lat < lat + 5:
        if par_lng > lng - 5 and par_lng < lng + 5:
            return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
time_now = datetime.now().hour

def night_time():
    if time_now > sunrise and time_now < sunset:
        return False

if in_range(iss_latitude, iss_longitude, MY_LAT, MY_LONG) is True:
    if night_time() is True:
        con = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        con.login(FROMMAIL, PASSWORD)
        con.sendmail(TOMAIL, "Subject:Catch a view of ISS\n\nHey,\nISS is floating around in your night sky\n"
                                           "Don't miss watching it")
        con.quit()





