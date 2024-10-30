# client information stored in csv file
import csv
from twilio.rest import Client
from datetime import datetime

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# File paths
last_sent_file = 'last_sent_date.txt'
recipients_file = 'recipients.csv'


def read_recipients():
    recipients = []
    with open(recipients_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            recipients.append((row['Name'], row['PhoneNumber']))
    return recipients


def send_messages(recipients):
    for name, number in recipients:
        message = client.messages.create(
            to=number,
            from_='+12060000000',
            body=f'Excessive Heat Warning! Please stay in cool places and keep hydrated!'
        )

def has_sent_today():
    try:
        with open(last_sent_file, 'r') as file:
            last_sent_date = file.read().strip()
            return last_sent_date == datetime.now().date().isoformat()
    except FileNotFoundError:
        return False


def update_last_sent_date():
    with open(last_sent_file, 'w') as file:
        file.write(datetime.now().date().isoformat())


if __name__ == "__main__":
    if not has_sent_today():
        recipients = read_recipients()
        send_messages(recipients)
        update_last_sent_date()
