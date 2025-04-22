
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
    import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message

API_TOKEN = "7965983575:AAEJOYjnCSrrm7O9iN-jE1DFO2hL39cC-jc"

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer("Ассалому алайкум! Мен ишлаяпман!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    git add .
git commit -m "Fix import error with aiogram executor"
git push origin main
