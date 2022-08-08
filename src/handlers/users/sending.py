
import datetime
from random import random, randint

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from keyboards.inline.callback_datas import send_callback
from keyboards.text.keyboardmenu import test_q1, test_q2
from loader import bot, dp
from states.send import Send


@dp.message_handler(Command("/starte"))
async def send(message: types.Message, state: FSMContext):
    user_id = 0
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"send_anon {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")
    my_user_id = message.from_user.id
    await message.answer("Щас подлючим тебя к какому-нибудь огрызку")
    await message.answer("Щас подлючим тебя к какому-нибудь огрызку")
    file = open('handlers/users/users_data/users.txt', 'r')
    line_count = sum(1 for line in file)
    file.seek(0)
    rand = randint(1, line_count)
    i = 1
    for string in file:
        if i == rand:
            print(string)
            words = string.split()
            user_id = words[1]
            break
        i = i + 1
    file.close()

    await Send.first()

    await state.update_data(user_id=user_id)
    await message.answer(
        "Вроде всё готово. Я наладил связь, можешь отправлять свои валентинки этому ботинку. Будешь должен.\n"
        "Не забудь три правила:\n"
        "1.Только текст(пока что что имеем то и юзаем, мб когда-нибудь мои хозяева расширят функционал)\n"
        "3.Как захочешь закончить ваш анонимный онанизм напиши /end_chat\n")

    # ssss = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Начать диалог", callback_data=f"send:{my_user_id}"), ], ])
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Начать диалог", callback_data=f"sendmess:{my_user_id}"))

    await bot.send_message(chat_id=user_id, text="Тебе пишет какой-то анонимус, хочешь ответь ему, хочешь нет, "
                                                 "но спамить он может и не прекратит", reply_markup=keyboard)
    await Send.next()

@dp.message_handler(Command("send"))
async def send(message: types.Message):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"send {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Со мной значит тебе скучно, нужны какие-то реальные ботинки?\n"
                         "Плевать, скинь мне его юзернейм без всяких лишних символов и тогда договоримся")

    await Send.first()


@dp.message_handler(state=Send.Q1)
async def get_username(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"get_username {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")
    my_user_id = message.from_user.id
    print(my_user_id)
    username = message.text
    user_id = 0
    file = open('handlers/users/users_data/users.txt', 'r')
    for string in file:
        if username in string:
            words = string.split()
            user_id = words[1]
            break
    file.close()
    if user_id == 0:
        await message.answer("Я те чё, сова?! А если и сова, то всё равно такого типа не знаю.\n"
                             "Проверь не долбишься ли ты в глаза и попробуй снова.")

    else:
        await state.update_data(user_id=user_id)
        await message.answer("С ним? бож...")
        await message.answer("Ладно...")
        await message.answer(
            "Вроде всё готово. Я наладил связь, можешь отправлять свои валентинки этому ботинку. Будешь должен.\n"
            "Не забудь три правила:\n"
            "1.Только текст(пока что что имеем то и юзаем, мб когда-нибудь мои хозяева расширят функционал)\n"
            "3.Как захочешь закончить ваш анонимный онанизм напиши /end_chat\n")

        # ssss = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Начать диалог", callback_data=f"send:{my_user_id}"), ], ])
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Начать диалог", callback_data=f"sendmess:{my_user_id}"))

        await bot.send_message(chat_id=user_id, text="Тебе пишет какой-то анонимус, хочешь ответь ему, хочешь нет, "
                                                     "но спамить он может и не прекратит", reply_markup=keyboard)
        await Send.next()


@dp.message_handler(Command("end_chat"), state=Send.Q2)
async def end_chat(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"end_chat {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Наскучил собеседничек? Или сказать нечего? Хотя и то и то, я думаю. \n"
                         "Впрочем если захочешь повторить, ты уже всё знаешь, но лучше не надо")
    await state.finish()


@dp.message_handler(state=Send.Q2)
async def send_mess(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"send_mess{message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    data = await state.get_data()
    user_id = data.get("user_id")

    await bot.send_message(chat_id=user_id, text=message.text)


@dp.message_handler(Command("end_chat"))
async def end_chat(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"end_chat {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Слышь мышь! \n"
                         "А шерсть не жмёт на всякие кнопки без контекста жать?")


@dp.callback_query_handler(send_callback.filter())
async def send_back(call: CallbackQuery, callback_data: dict, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"send_back {call.message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {call.message.text}")

    await call.answer(cache_time=60)
    user_id = callback_data.get("username")
    print(user_id)

    await call.message.answer("3...")
    await call.message.answer("2...")
    await call.message.answer("1...")
    await call.message.answer("FIGHT")

    await bot.send_message(chat_id=user_id, text="Ботинок, хочет вам ответить. Подключаю.")
    await Send.first()
    await Send.next()
    await state.update_data(user_id=user_id)

