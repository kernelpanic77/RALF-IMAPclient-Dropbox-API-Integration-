import email
import os
from ralf_dropbox import *

from imapclient import IMAPClient

HOST = 'imap-mail.outlook.com'#imap server depends on the website you choose, i will recommend OUTLOOK
USERNAME = 'SYSTEM EMAIL ID'
PASSWORD = 'SYSTEM EMAIL PASSWORD'#account that checks for emails from you

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    server.select_folder('INBOX', readonly=True)

    messages = server.search('UNSEEN')
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        if email_message.get('From') == 'IMT2019037 Ishan Shanware <ishan.shanware@iiitb.org>':#your email id from whic
          #  h you send the mails
            BACKUPPATH = '/' + os.path.basename(email_message.get('Subject'))
            print(BACKUPPATH)
            LOCALFILE = email_message.get('Subject')
            print(LOCALFILE)
            if len(TOKEN) == 0:
                sys.exit(
                    "ERROR: Looks like you didn't add your access token. Open up backup-and-restore-example.py in a text editor and paste in your token in line 14.")

            # Create an instance of a Dropbox class, which can make requests to the API.
            print("Creating a Dropbox object...")
            dbx = dropbox.Dropbox(TOKEN)

            # Check that the access token is valid
            try:
                dbx.users_get_current_account()
            except AuthError as err:
                sys.exit(
                    "ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

            try:
                checkFileDetails(dbx)
            except Error as err:
                sys.exit("Error while checking file details")

            print("Creating backup...")
            # Create a backup of the current settings file
            backup(dbx, LOCALFILE, BACKUPPATH)

            print("Done!")

    server.logout()

    # print(uid, email_message.get('From'), (email_message.get('Subject')), email_message.get('Body'))
