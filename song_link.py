from flask import Flask
from flask import request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client


account_sid = 'account'
auth_token = 'auth-token'

client = Client(account_sid, auth_token)
msg = client.messages.create(from_="whatsapp:+14155238886", body="Spotify-bot is online ^^", to="whatsapp:+910000000000")

app = Flask(__name__)
  
@app.route("/", methods=["POST"])

def chatbot():
    user_msg = request.values.get('Body', '').lower()

    response = MessagingResponse()
    query = user_msg+' spotify'
    result = []

    for i in search(query, num_results=1):
        result.append(i)
    
    msg = client.messages.create(from_="whatsapp:+14155238886", body=result[0], to="whatsapp:+910000000000")
    print(msg.sid)
    return str(response)

if __name__== "__main__":
    app.run()
