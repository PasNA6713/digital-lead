import os
import requests

import telebot
from dotenv import load_dotenv

from loguru import logger


load_dotenv(".env")

bot = telebot.TeleBot(os.getenv("MY_KEY"))
BACKEND = os.getenv("BACKEND_URL")
DIRPATH = os.getcwd()

@bot.message_handler(func=lambda message: True)
def send_welcome(message):
    r = requests.post(
        f'{BACKEND}message/create/',
        {
            "author_id": message.from_user.id,
            "text": message.text
        }
    )
    bot.reply_to(message, 'Спасибо за обращение, оно поможет сделать город лучше!')

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