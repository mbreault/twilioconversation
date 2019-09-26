import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

conversation = client.conversations \
                     .conversations \
                     .create(friendly_name='My First Conversation')

print(conversation.sid)