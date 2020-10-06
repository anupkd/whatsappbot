from flask import Flask, request ,send_file ,jsonify
import json
import requests
from twilio.twiml.messaging_response import MessagingResponse
import smtplib
import os
import sys
import random 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from  data.db import getuserid , insertuser ,updateuserasvalid

app = Flask(__name__)
lurl = os.environ['API_URL']
#opendb()

def mailme(mailid):
    SERVER_NAME='smtp.gmail.com'
    SERVER_PORT=587
    USER_NAME='anupkkd81'
    PASSWORD='A*$'
    print('connecting')
    server = smtplib.SMTP(SERVER_NAME, SERVER_PORT)
    print('connected..')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(USER_NAME, PASSWORD)
    text = 'TEST  ' +  str(random.randrange(2000, 5000, 3)) 
    server.sendmail('digital@gmail.com', mailid, 'Subject: Digital bank {}\n\n{}'.format(text, text))
    server.quit()


@app.route('/', methods=['GET'])
def home():
    amt = str(random.randrange(2000, 5000, 3)) 
    print(amt)    
    return  send_file('dynamicsay.json')

@app.route('/dynamicsay', methods=['POST'])
def dynamic_say():
    return send_file('dynamicsay.json')

@app.route('/complaint', methods=['POST'])
def dynamic_complaint():
    return send_file('complaint.json')


@app.route('/validateuserotp', methods=['POST'])
def validateuserotp():
    memory = json.loads(request.form.get('Memory'))
    answers = memory['twilio']['collected_data']['user_valid']['answers']
    option = answers['user_validate_otp']['answer']
    if(option == '1234'):
      updateuserasvalid(memory['twilio']['messaging.whatsapp']['From'].replace('whatsapp:+',''))
      return send_file('validated.json')
    return send_file('complaint.json') 


@app.route('/validate_useryesno', methods=['POST'])
def validate_useryesno():
    memory = json.loads(request.form.get('Memory'))
    answers = memory['twilio']['collected_data']['user_valid']['answers']
    option = answers['user_validate_now']['answer']
    if(option == 'Yes'):
      return send_file('validateuser.json')
    return send_file('complaint.json') 

@app.route('/userreg', methods=['POST'])
def usereg():
    memory = json.loads(request.form.get('Memory'))
    answers = memory['twilio']['collected_data']['user_reg']['answers']
    option = answers['user_reg_confirm']['answer']
    if('user_reg_fname'   in answers  ):
       val = (answers['user_reg_fname']['answer'],answers['user_reg_lname']['answer'], memory['twilio']['messaging.whatsapp']['From'].replace('whatsapp:+',''))
       insertuser(val)
       return send_file('complaint.json') 
    if(option == 'Yes'):
       return send_file('userreg.json')
    else:
       return send_file('complaint.json')

@app.route('/mail', methods=['POST'])
def dynamic_mail():
    memory = json.loads(request.form.get('Memory'))
    answers = memory['twilio']['collected_data']['mail_option']['answers']
    #print(answers['mail_option_selected'])
    if('mail_id' not in answers  ):
       option = answers['mail_option_selected']['answer']
    else: 
       option = answers['mail_id']['answer']
    print(option)
    if(option == 'No'):
       return jsonify(actions=[{'say': {'speech': 'Thanks for using the service.'}}])
    if(option == 'Yes'):
       return jsonify(actions=[{'collect':{'name':'mail_option','questions':[ {'question':'Enter email id','name':'mail_id','type':'Twilio.EMAIL'}],'on_complete':{'redirect':{'method':'POST','uri':lurl+'/mail'}}}}]) 
    else:  
       mailme(option)
    return jsonify(actions=[{'say': {'speech': 'Mail send to :' + option}}])

@app.route('/collect',  methods=['POST'])
def collect():
    memory = json.loads(request.form.get('Memory'))
    if('messaging.whatsapp'   in memory['twilio']  ):
       print(memory['twilio']['messaging.whatsapp']['From'].replace('whatsapp:+',''))
       u = getuserid(memory['twilio']['messaging.whatsapp']['From'].replace('whatsapp:+',''))
       if(u.id == -1): 
         return send_file('startuserreg.json')
       if(u.id > 0 and u.isvalidated ==0 ): 
         return send_file('nonvalid.json')
    answers = memory['twilio']['collected_data']['lead_option']['answers']
    amt = str(random.randrange(20000, 65000, 3)) 
    option = answers['lead_option_selected']['answer']
    if ( option == '1') : 
        message = f""" Balance 
you have AED {amt} balance in your current account ending with 5670, would like to send a detail report in your registered email? Enter Yes/No"""
        return jsonify(actions=[{'collect':{'name':'mail_option','questions':[{'question':message,'name':'mail_option_selected','type':'Twilio.YES_NO'} ],'on_complete':{'redirect':{'method':'POST','uri':lurl+'/mail'}}}}]) 

    if ( option == '2') : 
        amt2 = str(random.randrange(10000, 20000, 3))
        amt3 = str(random.randrange(1500, 9000, 3))
        amt4 = str(random.randrange(22000, 35000, 3))   
        message = f""" Statement
Please see your statement of account ending with **1345

Balance: {amt2}
Amount :{amt}
Date: 08-April-2020 10.30 PM
Description: ATM withdrawal
            
Balance: {amt3}
Amount :{amt4}
Date: 08-April-2020 10.30 PM
Description: Online trasfer

Would like to send a detail statement in your registered email? Enter Yes/No """
        return jsonify(actions=[{'collect':{'name':'mail_option','questions':[{'question':message,'name':'mail_option_selected','type':'Twilio.YES_NO'} ],'on_complete':{'redirect':{'method':'POST','uri':lurl+'/mail'}}}}]) 

    if ( option == '3') : 
        message = f"""Please specify your complaint """       
    return jsonify(actions=[{'collect':{'name':'compliant_option','questions':[{'question':message,'name':'complaint_text','type':'Twilio.ALPHANUMERIC'},{'question':'Enter contact number','name':'complaint_contact','type':'Twilio.ALPHANUMERIC'}],'on_complete':{'redirect':{'method':'POST','uri':lurl+'/complaint'}}}}]) 

    return jsonify(actions=[{'say': {'speech': 'Please specify a valid option'}}])
#jsonify(actions=[{'say': {'speech': message}}])
 
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

