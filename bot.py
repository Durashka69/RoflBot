import logging

from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from random import choice

from urls import URLS

API_TOKEN = TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Bot is online')

# '''#######################################################################'''

curse_words = ('хуй', 'блять', "гандон", "сука", "пизда", "ебланище",
               "влагалище", "пердун", "дрочила", "пидарас", "пиздец")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm ChortBot!.")


oxxxy_words = ('Говно залупа пенис хер давалка хуй блядина \nГоловка шлюха жопа член еблан петух мудила \nРукоблуд ссанина очко блядун вагина \nСука ебланище влагалище пердун дрочила \nПидор пизда туз малафья \nГомик мудила пилотка манда \nАнус вагина путана пидрила \nШалава хуила мошонка елда \nРаунд!')

# URL = 'https://ih1.redbubble.net/image.3067696797.1541/st,small,507x507-pad,600x600,f8f8f8.jpg'


@dp.message_handler(commands=['oxxxy'])
async def oxxxy(message: types.Message):
    await message.answer(oxxxy_words)


@dp.message_handler(commands=['greet_dragon'])
async def dragon(message: types.Message):
    await message.answer('Привет, Дракон! \nМы скучали, чорт!<3')


@dp.message_handler(commands=['image', 'img'])
async def send_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url(choice(URLS)))


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.lower() in curse_words:
        await message.answer('Не материмся')
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
