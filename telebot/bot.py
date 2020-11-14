import os
import json
import requests

import telebot
from dotenv import load_dotenv


load_dotenv(".env")

bot = telebot.TeleBot(os.getenv("MY_KEY"))
BACKEND = os.getenv("BACKEND_URL")

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    r = requests.post(
        f'{BACKEND}message/create/',
        {
            "author_id": message.from_user.id,
            "text": message.text
        }
    )
    response = json.loads(r.content)
    cl = response.get("event_class")
    if cl == "D": cl = "Дтп"
    elif cl == "F": cl = "Пожар"
    elif cl == "WW": cl = "Нарушение водоснабжения"
    bot.reply_to(message, f'Ваше сообщение класса: {cl}\nПо адресу: {response.get("address")}\nПринято!\n\nСпасибо за обращение, оно поможет сделать город лучше!')

@bot.message_handler(content_types=['photo'])
def processPhotoMessage(message):
    fileID = message.photo[-1].file_id
    file = bot.get_file(fileID)
    to_send = bot.download_file(file.file_path)
    headers = {
        'cache-control': "no-cache",
        'Content-Disposition': 'attachment; filename=example.txt'
    }
    file = {
        'file': to_send
    }
    requests.post(f'{BACKEND}message/photo/', headers=headers, files=file)
    bot.reply_to(message, 'Спасибо за обращение, оно поможет сделать город лучше!')

bot.polling()