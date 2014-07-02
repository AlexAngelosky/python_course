from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""#place the sid here
auth_token  = ""#place the token here
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="my name is makaron and i'm gonna ograba you and eat your kotka",
    to="",    # Replace with your phone number
    from_="") # Replace with your Twilio number
print message.sid

# I see a nice way to prank people with this :D
