import codecs
import datetime
import difflib
import os
from keyboards.text.keyboardmenu import menu
from aiogram.dispatcher.filters import Command, Text
from loader import bot, dp, text_to_speach
from aiogram.types import Message, ReplyKeyboardRemove
import config

with codecs.open('base.txt', encoding='utf-8') as x:  # открываем базу с ответами
    base = x.readlines()


async def send_to_admin(dp):
    await bot.send_message(chat_id=config.admin_id, text="Bot has been started! Well done")


async def delete_file(src):
    if os.path.isfile(src):
        os.remove(src)
        print(f"successful delete file {src}")
    else:
        print(f"File {src} doesn't exists!")

@dp.message_handler(Command("start"))
async def answerForComandStart(message: Message):
    file = open('handlers/users/users_data/users.txt', 'r+')
    file.seek(0)
    if message.from_user.username not in file.read():
        file.write(f"{message.from_user.username}: {message.from_user.id}\n")
    file.close()
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"answerForComandStart {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Салам, да наполниться токсичностью наш с тобой диалог)))")

@dp.message_handler(Command("hi"))
async def answerForComandHi(message: Message):

    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"answerForComandHi {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Привет, человече, как тебе удобнее воспринимать мою речь?", reply_markup=menu)


@dp.message_handler(Text(equals="Голосом"))
async def set_voice_speach(message: Message):
    config.voice_speach = True

    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"set_voice_speach {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    src = 'handlers/users/voice_messages/' + str(message.chat.id) + str(message.message_id) + '_answer.oga'
    text_to_speach.save_to_file("Как тебе мой волшебный голос?", src)
    text_to_speach.runAndWait()
    voice = open(src, 'rb')

    await bot.send_audio(message.chat.id, voice, reply_markup=ReplyKeyboardRemove())
    await delete_file(src)


@dp.message_handler(Text(equals="Текстом"))
async def set_text_speach(message: Message):

    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"set_text_speach {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    config.voice_speach = False
    await message.answer("Окей, как скажешь, мне ни капли не обидно!!!", reply_markup=ReplyKeyboardRemove())


@dp.message_handler()
async def default_answer(message: Message):

    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"default_answer {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    text = "У меня в базе нет таких слов чтоб описать насколько поношеный ты ботинок"
    tmp = 0.1
    for i in range(10):
        matcher = difflib.SequenceMatcher(None, message.text.lower(), base[i].lower()).ratio()
        if matcher > tmp:
            text = base[i]
            tmp = matcher

    print("bot: " + text)
    if config.voice_speach:
        src = 'handlers/users/voice_messages/' + str(message.chat.id) + str(message.message_id) + '_answer.oga'
        text_to_speach.save_to_file(text, src)
        text_to_speach.runAndWait()
        voice = open(src, 'rb')
        await bot.send_audio(message.chat.id, voice)
        await delete_file(src)
    else:
        await message.answer(text)
