import os
import telebot

TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "你好！我已经成功在 Railway 上活过来了！")

print("Bot started...")
bot.infinity_polling()
