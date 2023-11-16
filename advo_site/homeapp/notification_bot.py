from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from advo_site.secret import TG_KEY as TOKEN, CHAT_ID, ADMIN_ID


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def send_telegram_message(message):
    try:
        await bot.send_message(chat_id=CHAT_ID, text=message)
    except Exception as e:
        await bot.send_message(chat_id=ADMIN_ID, text=e)
    pass
