



if __name__ == "__main__":
    from aiogram import executor
    from handlers import dp
    from handlers import send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)
