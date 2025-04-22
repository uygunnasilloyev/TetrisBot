
from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = '7965983575:AAEJOYjnCSrrm7O9iN-jE1DFO2hL39cC-jc'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Салом! Бу Қаршилик ҳисоблаш учун файлни юборувчи бот. Олиш учун /file деб ёзинг.")

@dp.message_handler(commands=['file'])
async def send_file(message: types.Message):
    with open("Қаршилик.xlsx", "rb") as doc:
        await bot.send_document(chat_id=message.chat.id, document=doc, caption="Мана файлингиз: Қаршилик.xlsx")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
