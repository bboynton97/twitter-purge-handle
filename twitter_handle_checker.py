import twitter
import smtplib
import time
import os
from oauthlib.oauth1 import Client
from requests_oauthlib import OAuth1Session
import secrets
import string

# Twitter API credentials
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# Target Twitter handle to check
target_handle = "shweta"

# Email configuration
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
email_password = os.environ.get("EMAIL_PASSWORD")

oauth_session = OAuth1Session(
    client_key=consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret
)

# Authenticate with Twitter API
api = twitter.Api(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token_key=access_token,
    access_token_secret=access_token_secret
)

oauth_client = Client(consumer_key, client_secret=consumer_secret)

def generate_random_nonce(length=32):
    alphabet = string.ascii_letters + string.digits
    nonce = ''.join(secrets.choice(alphabet) for _ in range(length))
    return nonce

# Function to check if handle is available
def check_handle_availability(handle):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params = {"screen_name": target_handle, "count": 1}  # Example API parameters

    # Generate the OAuth signature
    oauth_client = Client(consumer_key, client_secret=consumer_secret)
    uri, headers, _ = oauth_client.sign(
        uri=url,
        http_method="GET",
        realm=None,
    )

    # Make the request to the Twitter API
    response = oauth_session.get(url, params=params, headers=headers)
    print(response.json())

    return response.status_code == 200:

# Function to send email notification
def send_email_notification():
    subject = f"Twitter Handle {target_handle} is now available!"
    body = f"The Twitter handle {target_handle} has become available."

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, email_password)
        server.sendmail(sender_email, receiver_email, message)


while True:
    if check_handle_availability(target_handle):
        send_email_notification()
        break

    print("Handle not available. Checking again in 1 hour...")
    time.sleep(60 * 60)  # Sleep for 1 hour before checking again
