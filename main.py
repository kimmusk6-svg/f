import os
import telebot
import requests

TOKEN = os.getenv('BOT_TOKEN')
DS_KEY = os.getenv('DEEPSEEK_API_KEY')
bot = telebot.TeleBot(TOKEN)

def get_ai_reply(text):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {DS_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": text}],
        "stream": False
    }
    res = requests.post(url, json=data, headers=headers, timeout=15)
    if res.status_code != 200:
        return f"🦞 出错啦，状态码：{res.status_code}"
    return res.json()['choices'][0]['message']['content']

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        reply = get_ai_reply(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"🦞 故障：{str(e)}")

print("Lobster AI Online")
bot.infinity_polling()
