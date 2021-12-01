#keeping the bot alive 24/7 on replit
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "**MIrai_IS_ONLINE_&_READY**"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()