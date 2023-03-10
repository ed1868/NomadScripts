import tweepy
import time

# Add your Twitter API credentials here
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



# Define the event date and time
event_date = datetime.datetime(2023, 3, 17, 12, 0, 0) # year, month, day, hour, minute, second

# Define the message to be tweeted
message = "Reminder: Our event is happening in 2 hours! Join us at the venue."

# Define the charity donation link
donation_link = "https://example.com/donate"

# Set the time interval for checking the event time
interval = 60 # in seconds

while True:
    # Get the current date and time
    now = datetime.datetime.now()

    # Calculate the time remaining until the event
    time_remaining = event_date - now

    # Check if the event is happening in less than 2 hours
    if time_remaining <= datetime.timedelta(hours=2):
        # Tweet the reminder message and donation link
        api.update_status(f"{message} Donate to our charity here: {donation_link}")
        print("Tweeted:", message)
        print("Donation link:", donation_link)
        break

    # Wait for the specified interval before checking the time again
    time.sleep(interval)



    
# Define a function to handle incoming mentions
def handle_mentions():
    # Get the 20 most recent mentions
    mentions = api.mentions_timeline(count=20)

    for mention in mentions:
        # Get the text of the mention
        mention_text = mention.text.lower()

        # Check if the mention is a request for directions
        if 'directions to' in mention_text:
            # Extract the destination from the mention text
            destination = mention_text.split('directions to ')[1]

            # Send a response with directions
            response = f"Here are the directions to {destination}: [insert directions here]"
            api.update_status(f"@{mention.user.screen_name} {response}", in_reply_to_status_id=mention.id)

        # Check if the mention is a request for recommendations
        elif 'recommendations for' in mention_text:
            # Extract the category from the mention text
            category = mention_text.split('recommendations for ')[1]

            # Send a response with recommendations
            response = f"Here are some recommendations for {category}: [insert recommendations here]"
            api.update_status(f"@{mention.user.screen_name} {response}", in_reply_to_status_id=mention.id)

# Set the time interval for checking mentions
interval = 60 # in seconds

while True:
    try:
        # Handle incoming mentions
        handle_mentions()

        # Wait for the specified interval before checking mentions again
        time.sleep(interval)

    except tweepy.TweepError as error:
        print(error.reason)

    except StopIteration:
        break
