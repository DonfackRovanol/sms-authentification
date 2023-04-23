import os
from twilio.rest import Client 
 
account_sid = 'AC93eb079fd6f989960366bb6834e6b84f' 
auth_token = '2350eca340520ee896aab5ba7ddd243b' 
client = Client(account_sid, auth_token) 
def send_sms(user_code, phone_number):
    message = client.messages.create(    
                              body=f'Hi! your user and verification code is {user_code}',    
                              from_='+13344328644',
                              to=f'{phone_number}'
                               
                          ) 
 
    print(message.sid)