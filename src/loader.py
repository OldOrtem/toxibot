import pyttsx3
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config

bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#text_to_speach = pyttsx3.init()  # работаем над голосом
# for voice in text_to_speach.getProperty('voices'):
#     print('--------------------')
#     print('Имя: %s' % voice.name)
#     print('ID: %s' % voice.id)
#text_to_speach.setProperty('voice',
 #                          "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0")
