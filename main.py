import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "说你想说的任何话")

print("Bot started...")
bot.infinity_polling()
