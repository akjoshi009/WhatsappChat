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
        text =  'Hi from 1point1 solutions please type Info to know about us'
        msg.body(text)
        responded = True

    if 'Info' in incoming_msg.lower():
        # return total cases
        text='1Point1 enables its clients to adopt the right technology tools and refurbish their IT landscape for a leading edge in a fast-paced marketplace.'
        msg.body(text)
        responded = True

    if 'Bye' in incoming_msg or 'bye' in incoming_msg:
        text='Bye nice talking to you'
        msg.body(text)
        responded = True

    if responded == False:
        msg.body('I only know about 1Point1 Solutions, sorry!')

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
