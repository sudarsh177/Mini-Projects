from twilio.rest import Client
import smtplib
import os

FROM_MAIL = os.getenv("FROM")
PSWD = os.getenv("PSWD")
MOB = os.getenv("MOB")
FROM_MOB = os.getenv("FMOB")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.getenv("SID")
        self.auth_token = os.getenv("AUTHTOKEN")
        self.msg_body = ""

    def send_message(self,data):
        self.flight = data
        self.msg_body = f"Only Rs.{self.flight['price'] * 86} to fly from {self.flight['from_city']} " \
                        f"to {self.flight['to_city']}, from {self.flight['dept_date']} to {self.flight['arr_date']}"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body= self.msg_body,
            from_=FROM_MOB,
            to=MOB)
        print(message.status)

    def send_email(self,flight,detail):
        details = detail
        self.flight = flight
        for a in details[1:]:
            connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            connection.login(FROM_MAIL, PSWD)
            connection.sendmail(FROM_MAIL,f"{a['email']}", f"Subject:Flight Deals for you!!\n\n"
                                                                              f"Only Rs.{self.flight['price'] * 86} to fly from "
                                                                              f"{self.flight['from_city']} to {self.flight['to_city']},"
                                                                              f" from {self.flight['dept_date']} to "
                                                                              f"{self.flight['arr_date']}")
            connection.quit()







