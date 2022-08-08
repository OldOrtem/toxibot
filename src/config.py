import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
admin_id =  os.getenv("admin_id")

voice_speach = False # переменная которая отвечает за речь бота. false - текст, true - аудио
