from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
import os

from email.mime.text import MIMEText

SCOPES = ['https://mail.google.com/']

def gmail_send_message(creds):

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = MIMEText('Your product is on sale!!!')
        message['To'] = 'mustachio1125@gmail.com'
        message['From'] = 'sender@gmail.com'
        message['Subject'] = 'Sale Alert'
        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf8')

        print(encoded_message)
        create_message = {'raw': encoded_message}
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message


def main():
    """Shows basic usage of the Gmail API.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    gmail_send_message(creds)


if __name__ == '__main__':
    main()
# [END gmail_quickstart]