import telebot
from flask import Flask, request
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

API_TOKEN = '7204126626:AAHKpboItYJMGnqiu3NsQzIoclQGGlh_qZs'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me a photo to get started.")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    user_id = message.from_user.id
    landing_page_url = f"https://youtube.com?user={user_id}"
    bot.reply_to(message, f"Please view an ad to continue: {landing_page_url}")

@app.route('/landing_page')
def landing_page():
    return """
    <h1>Watch the Ad</h1>
    <p>Ad would go here. After viewing, your request will be processed.</p>
    <script>
        setTimeout(function() {
            alert("Thank you for viewing the ad. Your request is being processed.");
        }, 5000);
    </script>
    """
@app.route('/')
def home():
    return "Welcome to the bot's web server!"

if __name__ == "__main__":
    import threading
    threading.Thread(target=app.run, kwargs={'host': '0.0.0.0', 'port': 8000}).start()

    print("Bot is starting...")
    print(f"Using token: {API_TOKEN}")
    try:
        bot.get_me()  # This will fail if the token is invalid
        print("Token is valid. Bot is running.")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"An error occurred: {e}")
        logging.exception("An error occurred:")