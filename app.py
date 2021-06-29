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
    #print(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'hi' in incoming_msg.lower() or 'hey' in incoming_msg.lower() or 'hello' in incoming_msg.lower():
        text =  'Hi I am IRA Bot 🤖 ,Please say info to get all menu.'
        msg.body(text)
        responded = True

    if 'info' in incoming_msg.lower():
        # return total cases
        text='IRA  Bot 🤖 supports Following Menu:\n 1:Check Balance \n 2:Cheque Book Request \n 3:E-statement \n 4:Exit'
        msg.body(text)
        responded = True
        
    if 'check balance' in incoming_msg.lower() or '1' in incoming_msg.lower():
        text='Your balance is Rs.21245 for going to main menu replay with info 🙂🙂'
        msg.body(text)
        responded = True
        
    if 'cheque book request' in incoming_msg.lower() or '2' in incoming_msg.lower():
        text='You are requested for cheque book it will delivered in next 7 days 🙂🙂.\n for going to main menu replay with info'
        msg.body(text)
        responded = True
        
    if 'e-statement' in incoming_msg.lower() or 'statement' in incoming_msg.lower() or '3' in incoming_msg.lower():
        text='E-staetment is mailed to your email id a*****dt@***.com 🙂🙂 \n for going to main menu replay with info'
        msg.body(text)
        responded = True    
        
    if 'bye' in incoming_msg.lower() or 'exit' in incoming_msg.lower() or '4' in incoming_msg.lower():
        text='Bye nice talking to you'
        msg.body(text)
        responded = True

    if responded == False:
        msg.body('I dont understand please send info to get more information., \n sorry 🙇🏽‍♂️🙇🏽‍♂️!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
