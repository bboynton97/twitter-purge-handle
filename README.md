# Twitter Handle Availability Checker

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Python script that checks if a Twitter handle becomes available and sends an email notification when it does. This open-source project utilizes the Tweepy library for Twitter API interaction and the smtplib library for sending email notifications.

## Features

- Monitors a specified Twitter handle to check if it becomes available.
- Sends an email notification when the handle becomes available.
- Customizable email configuration.

## Usage

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/twitter-handle-availability-checker.git
   ```

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Set up your Twitter API credentials and email configuration:
    - Obtain Twitter API credentials from the Twitter Developer Portal.
    - Configure the email settings in the script.

4. Customize the script:
   - Specify the Twitter handle you want to monitor in the target_handle variable.
   - Modify the email subject and body in the send_email_notification function to suit your needs.

5. Run the script:
`python twitter_handle_checker.py`

The script will continuously check if the handle becomes available and send an email notification when it does.

## Configuration
The script requires the following environment variables to be set:

```
CONSUMER_KEY: Your Twitter API consumer key.
CONSUMER_SECRET: Your Twitter API consumer secret.
ACCESS_TOKEN: Your Twitter API access token.
ACCESS_TOKEN_SECRET: Your Twitter API access token secret.
SENDER_EMAIL: The sender's email address for email notifications.
RECEIVER_EMAIL: The receiver's email address for email notifications.
EMAIL_PASSWORD: The password for the sender's email account.
```

## Contributing
Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.