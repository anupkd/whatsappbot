from flask import Flask, request ,jsonify
from twilio.twiml.messaging_response import MessagingResponse
import json
import requests

app = Flask(__name__)


GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():

    response = MessagingResponse()
    memory = json.loads(request.form.get('Memory'))
    #print(request.values)
    print(memory['twilio']['messaging.whatsapp']['From'])
    #num_media = int(request.values.get("NumMedia"))
    #if not num_media:
    #    msg = response.message("Send us an image!")
    #else:
    #    msg = response.message("Thanks for the image. Here's one for you!")
    #    msg.media(GOOD_BOY_URL)
    return str(response)

@app.route("/whatsapp2", methods=["GET", "POST"])
def reply_whatsapp2():

    response = MessagingResponse()
    if request.values.get("To")=='whatsapp:+14155238886' :
       print(request.values)
    return str(response)


if __name__ == "__main__":
    app.run("0.0.0.0",5000)
