from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import nudes_callback

choice_nudes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Киску", callback_data=nudes_callback.new(nudes="kitty")),
            InlineKeyboardButton(text="Дыньки", callback_data="send:melons"),
        ],
        [
            InlineKeyboardButton(text="Орех", callback_data=nudes_callback.new(nudes="nut")),
            InlineKeyboardButton(text="Я гей", callback_data="cancel"),
        ],
    ]
)

choice_send = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Начать диалог", callback_data=nudes_callback.new(nudes="kitty")),
        ],
    ]
)