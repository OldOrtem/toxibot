
import datetime


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.text.keyboardmenu import test_q1, test_q2
from loader import bot, dp
from states.test import Test

@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"enter_test {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer("Первый вопрос:\n Вы гей или лесбуха?", reply_markup=test_q1)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker=r"CAACAgIAAxkBAAEFcA1i6CyBc7D7vUTMN62gmynsaM0Y1AACowcAAkb7rARoqaAAAUqkfyApBA")
    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"answer_q1 {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    answer = message.text
    await state.update_data(answer1=answer)
    if message.text == "лесбуха":
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker=r"CAACAgIAAxkBAAEFcA9i6C0SCU5KRztqZznHGZB6Bqn_VgACWAYAAvoLtggLUiPPY3zCyikE")
        await message.answer("Вы сами то себе верите? \n Допустим...", reply_markup=ReplyKeyboardRemove())
    elif message.text == "гей":
        await message.answer("Уважаемо!", reply_markup=ReplyKeyboardRemove())
    await message.answer("Второй вопрос:\nВы педофил или пидорас?", reply_markup=test_q2)
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"answer_q2 {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    answer2 = message.text
    data = await state.get_data()
    answer1 = data.get("answer1")
    if answer1 == "лесбуха" and ("Николай" in answer2 or "николай" in answer2):
        await message.answer(f"Поздравляю, вы прошли тест!!!\n"
                             f"Опрос показал что вы на удивление классный парень.\n"
                             f"Приятно иметь с вами дело;)", reply_markup=ReplyKeyboardRemove())
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker=r"CAACAgIAAxkBAAEFcBFi6C0n1W05dZ0lHcrIiIJDBtIl8QACwxUAAgImKUsUBkXpd6hrdCkE")
    else:
        await message.answer(f"Поздравляю, вы прошли тест!!!\n"
                             f"Опрос показал что вы {answer1}-{answer2}.\n"
                             f"Даже не знаю как вам с этим дальше жить...", reply_markup=ReplyKeyboardRemove())
        await bot.send_sticker(chat_id=message.chat.id,
                               sticker=r"CAACAgIAAxkBAAEFcAti6CwE0NIP9uf86kGaR5bwBSE76gACNwMAAsSraAu8M1Of1BlNMykE")
    await state.finish()

    # await state.reset_state(with_data=False) # без стирания данных в data
