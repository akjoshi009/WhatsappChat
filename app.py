# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:18:08 2021

@author: user
"""

from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

staged='0'
Get_Stage = "http://kms.1point1.in/voicebot/api/v1/getstage?id="

addstageinfo="http://kms.1point1.in/voicebot/api/v1/createconversation?"

def getstageinfo(number):
    r = requests.get(url = Get_Stage+number)
    if(len(r)>0):
        return r['stage']
    else:
        return '0'
    
def insertmsgs(stage,number,msg):
    fnurl=addstageinfo+'stage='+stage+'&number='+number+'&msg='+msg
    r = requests.get(url = fnurl)
    print(r)
    
    

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
    try:
       staged=getstageinfo(mobnumber)
       print("Staged"+str(staged))
    except:
        staged='0'
        pass
    if(staged=='0'):
        text =  'Hi I am IRA Bot 🤖 ,\n Please tell your name.\n Example(Name:John doe)'
        msg.body(text)
        #insertmsgs('1',mobnumber,incoming_msg)
        responded = True

    elif(staged=='1'):
        text = 'Please confirm your phone number.\n Example Number:986754321 🙂🙂'
        msg.body(text)
        insertmsgs('2',mobnumber,incoming_msg)
        responded = True
        
    elif(staged=='2'):
        text = 'We confirmed you user now please say info to get all the services 🙂🙂'
        msg.body(text)
        #insertmsgs('3',mobnumber,incoming_msg)
        responded = True    
    
    elif 'info' in incoming_msg.lower() and staged=='3':
        # return total cases
        text='IRA  Bot 🤖 supports Following \n Menu:\n 1:Check Balance \n 2:Cheque Book Request \n 3:E-statement \n 4:Talk to Customer support executive'
        msg.body(text)
        #insertmsgs('3',mobnumber,incoming_msg)
        responded = True
        
    elif ('check balance' in incoming_msg.lower() or '1' in incoming_msg.lower()) and staged=='3':
        text='Your balance is Rs.21245 for going to main menu replay with info 🙂🙂'
        msg.body(text)
        #insertmsgs('3',mobnumber,incoming_msg)
        responded = True
        
    elif('cheque book request' in incoming_msg.lower() or '2' in incoming_msg.lower()) and staged=='3':
        text='You are requested for cheque book it will delivered in next 7 days 🙂🙂.\n for going to main menu replay with info'
        msg.body(text)
        insertmsgs('3',mobnumber,incoming_msg)
        responded = True
        
    elif('e-statement' in incoming_msg.lower() or 'statement' in incoming_msg.lower() or '3' in incoming_msg.lower()) and staged=='3':
        text='E-staetment is mailed to your email id a*****dt@***.com 🙂🙂 \n for going to main menu replay with info'
        msg.body(text)
        #insertmsgs('3',mobnumber,incoming_msg)
        responded = True    
        
    elif ('bye' in incoming_msg.lower() or 'exit' in incoming_msg.lower() or '4' in incoming_msg.lower())and staged=='3':
        text='Bye nice talking to you'
        msg.body(text)
        #insertmsgs('3',mobnumber,incoming_msg)
        responded = True

    if responded == False:
        msg.body('I dont understand please send info to get more information., \n sorry 🙇🏽‍♂️🙇🏽‍♂️!'+mobnumber)

    return str(resp)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
