import os
import argparse
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
personal_mobile_number = os.environ['TWILIO_PERSONAL_MOBILE_NUMBER']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']

client = Client(account_sid, auth_token)

parser = argparse.ArgumentParser(description='Fetch a conversation.')
parser.add_argument('conversation_sid',help='conversation sid')
args = parser.parse_args()

participant = client.conversations \
    .conversations(args.conversation_sid) \
    .participants \
    .create(
         messaging_binding_address=personal_mobile_number,
         messaging_binding_proxy_address=twilio_phone_number
     )

print(participant.sid)
