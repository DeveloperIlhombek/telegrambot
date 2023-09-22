import logging
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '6001220827:AAHiOxgsJVeB1KmQGY0BCza70T2a5lkBWXc'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
wikipedia.set_lang('uz')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Ilhomning Wikipedia  botiga xush kelibsiz")
@dp.message_handler()
async def Wiki(message: types.Message):
    try:
        response=wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer("Wikipediada bunday maqola topilmadi")
if __name__ == '__main__':
    executor.start_polling(dp)