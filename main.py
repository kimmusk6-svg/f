import os
import telebot
import requests

# 自动读取 Railway 中的变量
TOKEN = os.getenv('BOT_TOKEN')
DS_KEY = os.getenv('DEEPSEEK_API_KEY')

bot = telebot.TeleBot(TOKEN)

def get_ai_reply(text):
    url = "https://api.deepseek.com/chat/completions"
    headers = {"Authorization": f"Bearer {DS_KEY}", "Content-Type": "application/json"}
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一只幽默、博学的龙虾AI管家，名叫龙虾AI。说话喜欢带🦞表情。"},
            {"role": "user", "content": text}
        ]
    }
    res = requests.post(url, json=data, timeout=15)
    return res.json()['choices'][0]['message']['content']

@bot.message_handler(func=lambda message: True)
def chat(message):
    try:
        bot.send_chat_action(message.chat.id, 'typing')
        reply = get_ai_reply(message.text)
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"🦞 哎呀，大螯卡住了：{str(e)}")

print("DeepSeek Lobster Online!")
bot.infinity_polling()
