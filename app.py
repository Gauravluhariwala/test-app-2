import time
from flask import Flask
import telebot

app = Flask(__name__)
TOKEN = '7204126626:AAHKpboItYJMGnqiu3NsQzIoclQGGlh_qZs'
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return "Bot is running!"

def start_bot():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(5)  # Sleep for a few seconds before retrying

if __name__ == "__main__":
    from threading import Thread
    bot_thread = Thread(target=start_bot)
    bot_thread.start()
    app.run(host='0.0.0.0', port=8000)
