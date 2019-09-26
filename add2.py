import os
import argparse
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

parser = argparse.ArgumentParser(description='Fetch a conversation.')
parser.add_argument('conversation_sid',help='conversation sid')
args = parser.parse_args()

participant = client.conversations \
    .conversations(args.conversation_sid) \
    .participants \
     .create(identity='embersilk')

print(participant.sid)