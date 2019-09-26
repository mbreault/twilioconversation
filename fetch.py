import os
import argparse
from twilio.rest import Client

parser = argparse.ArgumentParser(description='Fetch a conversation.')
parser.add_argument('conversation_sid',help='conversation sid')
args = parser.parse_args()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations(args.conversation_sid) \
                     .fetch()

print(conversation.chat_service_sid)
