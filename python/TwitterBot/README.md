# NomadScripts - Python Automation 


# Good Morning Text with Daily Horoscope

This is a Python script that sends a variation of good morning texts every day with the daily horoscope for the Leo sign. The script uses the Twilio API to send text messages and a horoscope API to fetch the daily horoscope.

# Setup
To use this script, follow these steps:

    1. Clone this repository to your local machine.
    2. Install the required Python libraries by running pip install -r requirements.txt.
    3. Obtain an API key for the Twilio API and the horoscope API.
    4. Update the config.ini file with your Twilio account information, phone numbers, and API keys for the horoscope API.

# Usage
This script will do the following:

    * Run the script by running python main.py in your terminal.
    * The script will run in the background and send a good morning text message with the daily horoscope for the Leo sign every day at 6 AM.

# Features
    Sends a variation of good morning texts every day with the daily horoscope for the Leo sign.
    Uses the Twilio API to send text messages.
    Uses a horoscope API to fetch the daily horoscope for the Leo sign.
    Randomly selects a good morning text message from a list of options.
    Schedule the script to run at a specific time every day.
    Easy to configure by updating the config.ini file with your API keys and phone numbers.

# Configuration

# The config.ini file contains the following configuration options:

    twilio_account_sid: Your Twilio account SID.
    twilio_auth_token: Your Twilio auth token.
    from_number: Your Twilio phone number.
    to_number: The phone number that will receive the good morning texts.
    horoscope_api_key: Your API key for the horoscope API.
    horoscope_api_endpoint: The endpoint URL for the horoscope API.
    You can update these options to configure the script for your specific use case.

# Limitations

    The script only sends good morning texts with the daily horoscope for the Leo sign.
    The horoscope API may have rate limits or usage limits that you need to be aware of.
    Sending text messages through a programmatic interface like Twilio may incur additional costs.