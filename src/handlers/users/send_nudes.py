import datetime

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.callback_datas import nudes_callback
from keyboards.inline.choice_buttons import choice_nudes
from loader import bot, dp


@dp.message_handler(Command("send_nudes"))
async def sendNudes(message: Message):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"sendNudes {message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {message.text}")

    await message.answer(text="Ах ты шалунишка, ну выбирай, что хочешь:", reply_markup=choice_nudes)


@dp.callback_query_handler(nudes_callback.filter())
async def send_kitty(call: CallbackQuery, callback_data: dict):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"send_kitty {call.message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {call.message.text}")

    await call.answer(cache_time=60)
    if callback_data.get("nudes") == "kitty":
        await bot.send_photo(call.message.chat.id, open("handlers/users/nudes/kitty.jpg", 'rb'), "Держи киску")
    elif callback_data.get("nudes") == "melons":
        await bot.send_photo(call.message.chat.id, open("handlers/users/nudes/melons.jpg", 'rb'), "Держи дыньки")
    elif callback_data.get("nudes") == "nut":
        await bot.send_photo(call.message.chat.id, open("handlers/users/nudes/nut.jpg", 'rb'), "Держи орешек")


@dp.callback_query_handler(text="cancel")
async def cancelNudes(call: CallbackQuery):
    date_format = "%H:%M:%S %d.%m.%Y"
    print(f"cancelNudes {call.message.from_user.username} ({datetime.datetime.today().strftime(date_format)}): {call.message.text}")

    await call.answer("Круто, че", show_alert=True)
    await call.message.edit_reply_markup()
