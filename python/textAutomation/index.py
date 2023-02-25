import random
from twilio.rest import Client
import schedule
import time
import requests

# Function to fetch the daily horoscope for Leo sign
def get_leo_horoscope():
    # Replace with your API key and endpoint URL
    url = "https://api.horoscope.com/.../leo"
    headers = {
        "Authorization": "Bearer your_api_key"
    }
    response = requests.get(url, headers=headers)
    if response.ok:
        horoscope = response.json()["horoscope"]
        return horoscope
    else:
        return "Unable to fetch horoscope."

# Function to send the good morning text
def send_text():
    # Twilio account information
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    client = Client(account_sid, auth_token)

    # List of good morning messages
    messages = [
        "Good morning, sunshine!",
        "Rise and shine!",
        "Good morning, gorgeous!",
        "Morning, beautiful!",
        "Wake up and smell the coffee!",
        "Good morning, love!"
    ]

    # Choose a random message
    message = random.choice(messages)

    # Fetch the daily horoscope for Leo sign
    horoscope = get_leo_horoscope()

    # Include the horoscope in the message
    message = f"{message} {horoscope}"

    # Your Twilio phone numberß
    from_number = "+1234567890"
    # Your girlfriend's phone number
    to_number = "+0987654321"

    # Send the text message
    client.messages.create(to=to_number, from_=from_number, body=message)

# Schedule the script to run every day at 6 AM
schedule.every().day.at("6:00").do(send_text)

while True:
    schedule.run_pending()
    time.sleep(1)
