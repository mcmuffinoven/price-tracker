from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64
from email.mime.text import MIMEText


SCOPES = ['https://mail.google.com/']

class Mailer():
    def __init__(self):
        self.mail_from = "mustachio1125@gmail.com"
        self.mail_subject_header = "Sale Alert For "
        self.creds_file = "token.json"
        self.secrets_file = "credentials.json"
        self.mail_body = """Your product is on sale!!"""
        
    def gmail_send_message(self, creds):

        try:
            service = build('gmail', 'v1', credentials=creds)
            message = MIMEText(self.mail_body)
            message['To'] = 'mustachio1125@gmail.com'
            message['From'] = self.mail_from
            message['Subject'] = self.mail_subject_header
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


    def authenticate(self):
        """Shows basic usage of the Gmail API.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.creds_file):
            creds = Credentials.from_authorized_user_file(self.creds_file, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.secrets_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.creds_file, 'w') as token:
                token.write(creds.to_json())

        return creds

def main():
    # Initiate Mailer 
    mailer = Mailer()
    product = "abc"
    creds = mailer.authenticate()
    mailer.gmail_send_message(creds, product)

if __name__ == '__main__':
    main()
