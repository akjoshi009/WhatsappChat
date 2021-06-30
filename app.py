from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    mobnumber=request.values.get('From','')
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'hi' == incoming_msg.lower() or 'hey' == incoming_msg.lower() or 'hello' == incoming_msg.lower():
        text =  'Hi I am IRA Bot 🤖 ,\n Please tell your name.\n Example(Name:John doe)'
        msg.body(text)
        responded = True

    elif 'name' in incoming_msg.lower():
        text = 'Please confirm your phone number.\n Example Number:986754321 🙂🙂'
        msg.body(text)
        responded = True
        
    elif 'number' in incoming_msg.lower():
        text = 'We confirmed you John doe now please say info to get all the services 🙂🙂'
        msg.body(text)
        responded = True
    
    
    elif 'info' in incoming_msg.lower():
        # return total cases
        text='IRA  Bot 🤖 supports Following \n Menu:\n 1:Check Balance \n 2:Cheque Book Request \n 3:E-statement \n 4:Exit'
        msg.body(text)
        responded = True
        
    elif 'check balance' in incoming_msg.lower() or '1' in incoming_msg.lower():
        text='Your balance is Rs.21245 for going to main menu replay with info 🙂🙂'
        msg.body(text)
        responded = True
        
    elif 'cheque book request' in incoming_msg.lower() or '2' in incoming_msg.lower():
        text='You are requested for cheque book it will delivered in next 7 days 🙂🙂.\n for going to main menu replay with info'
        msg.body(text)
        responded = True
        
    elif 'e-statement' in incoming_msg.lower() or 'statement' in incoming_msg.lower() or '3' in incoming_msg.lower():
        text='E-staetment is mailed to your email id a*****dt@***.com 🙂🙂 \n for going to main menu replay with info'
        msg.body(text)
        responded = True    
        
    elif 'bye' in incoming_msg.lower() or 'exit' in incoming_msg.lower() or '4' in incoming_msg.lower():
        text='Bye nice talking to you'
        msg.body(text)
        responded = True

    if responded == False:
        msg.body('I dont understand please send info to get more information., \n sorry 🙇🏽‍♂️🙇🏽‍♂️!'+mobnumber)

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
