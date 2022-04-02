from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markup
from sdamgia import SdamGIA
import random
import requests
import json
import emoji

TOKEN = '5018669230:AAG7aLb8pxho0Cfnp8zd-sjNf9Gxtz_bcP4'

sdamgia = SdamGIA()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    username = message.from_user["username"]
    supported_user = username.replace('.', '-')
    request = requests.get(url + '?auth=' + auth)
    data = request.json()
    logins = set()
    for key, value in data.items():
        logins.add(key)
    if supported_user not in logins:
        signup_info = str({
            f'"{username}":{{"Количество решённых задач":"0"}}'})
        signup_info = signup_info.replace(".", "-")
        signup_info = signup_info.replace("\'", "")
        to_database = json.loads(signup_info)
        requests.patch(url=url, json=to_database)
    await message.answer(f'Приветствую {message.from_user["username"]}, давайте начнем подготовку к ЕГЭ.',
                         reply_markup=markup.mainMenu)


@dp.message_handler()
async def main_dialog(message: types.Message):
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    if message.text in markup.d.keys():
        await message.answer('Все задачи', reply_markup=markup.d[message.text][1])
    elif message.text in markup.testList:
        await message.answer('Неизвестная команда')
    elif message.text == 'Выбор предмета':
        await message.answer('Каталог предметов', reply_markup=markup.subjectsMenu)
    elif message.text == 'Главное меню':
        await message.answer('Главное меню', reply_markup=markup.mainMenu)
    elif message.text == 'Профиль':
        username = message.from_user["username"]
        supported_user = username.replace('.', '-')
        request = requests.get(url + '?auth=' + auth)
        data = request.json()
        print(data)
        quantify = data[supported_user]['Количество решённых задач']
        await message.answer(emoji.emojize('👤') + 'Профиль:' + '\n\n' +
                             'Имя пользователя: ' + username + '\n' +
                             'Количество решённых задач: ' + quantify, reply_markup=markup.profile)
    elif message.text == 'Помощь':
        await message.answer('Бот для ЕГЭ')


executor.start_polling(dp, skip_updates=True)
