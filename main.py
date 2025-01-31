import telebot

TOKEN = "8122418852:AAGtJX3KlIRHMoZgKdH2YO1q4czfeuRlIlU"
bot = telebot.TeleBot(TOKEN)

@bot.channel_post_handler(func=lambda message: True)
def send_message(message):
    bot.send_message(message.chat.id, "ارسل كلمة اللغز بسرعه !!!!")

print("البوت يعمل...")
bot.polling()
