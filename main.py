from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile, InputMediaPhoto
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markup
from sdamgia import SdamGIA
import random
import requests
import json
import emoji
import convertapi
import pyrebase

TOKEN = '5018669230:AAG7aLb8pxho0Cfnp8zd-sjNf9Gxtz_bcP4'

sdamgia = SdamGIA()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("profile", "Профиль"),
        types.BotCommand("math", "Математика"),
        types.BotCommand("rus", "Русский язык"),
        types.BotCommand("inf", "Информатика"),
        types.BotCommand("phys", "Физика"),
        types.BotCommand("chem", "Химия"),
        types.BotCommand("bio", "Биология"),
        types.BotCommand("soc", "Обществознание"),
        types.BotCommand("his", "История"),
        types.BotCommand("lit", "Литература"),
        types.BotCommand("geo", "География")

    ])


@dp.message_handler(commands='start')
async def command_start(message: types.Message):
    firebaseConfig = {
        'apiKey': "AIzaSyD2FYwRp4O_12HTtkKMnmUJLBHvJ4cgaEE",
        'authDomain': "egebot-79552.firebaseapp.com",
        'databaseURL': "https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId': "egebot-79552",
        'storageBucket': "egebot-79552.appspot.com",
        'messagingSenderId': "878336561547",
        'appId': "1:878336561547:web:547ef57a8c1bf2c0a19f8e",
        'measurementId': "G-PJ20VQMKJN"
    }
    firebase = pyrebase.initialize_app(firebaseConfig)
    username = message.from_user['username']
    db = firebase.database()
    a = db.get('hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV')
    logins = []
    for i in a.val():
        logins.append(i)
    if username not in logins:
        data = {"Количество решённых задач": "0"}
        db.child(f"{username}").set(data)
    await set_default_commands(dp)
    await message.answer(f'Приветствую {message.from_user["username"]}, давайте начнем подготовку к ЕГЭ.',
                         reply_markup=markup.mainMenu)


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('Бот для подготовки к ЕГЭ')


@dp.message_handler(commands='profile')
async def profile(message: types.Message):
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    username = message.from_user["username"]
    supported_user = username.replace('.', '-')
    request = requests.get(url + '?auth=' + auth)
    data = request.json()
    print(data)
    quantify = data[supported_user]['Количество решённых задач']
    await message.answer(emoji.emojize('👤') + 'Профиль:' + '\n\n' +
                         'Имя пользователя: ' + username + '\n' +
                         'Количество решённых задач: ' + quantify, reply_markup=markup.profile)


@dp.message_handler(commands='math')
async def math(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Математика'][1])


@dp.message_handler(commands='rus')
async def rus(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Русский язык'][1])


@dp.message_handler(commands='inf')
async def inf(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Информатика'][1])


@dp.message_handler(commands='phys')
async def phys(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Физика'][1])


@dp.message_handler(commands='chem')
async def chem(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Химия'][1])


@dp.message_handler(commands='bio')
async def math(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Биология'][1])


@dp.message_handler(commands='geo')
async def geo(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['География'][1])


@dp.message_handler(commands='soc')
async def soc(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Обществознание'][1])


@dp.message_handler(commands='lit')
async def lit(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['Литература'][1])


@dp.message_handler(commands='his')
async def lit(message: types.Message):
    await message.answer('Все задачи', reply_markup=markup.d['История'][1])


@dp.message_handler()
async def main_dialog(message: types.Message):
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    if message.text in markup.d.keys():
        await message.answer('Все задачи', reply_markup=markup.d[message.text][1])
    elif message.text in markup.testList:
        await test_by_category(message)
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


@dp.message_handler()
async def test_by_category(message: types.Message):
    for i in markup.d.keys():
        if message.text.split()[1] == i[:3]:
            markuprepl = ''
            subject = markup.d[i][0]
            id = message.text.split()[0]
            print(sdamgia.get_catalog(subject)[int(id) - 1])
            s = random.choice(sdamgia.get_catalog(subject)[int(id) - 1]['categories'])
            categoryTests = sdamgia.get_category_by_id(subject, s['category_id'])
            test = sdamgia.get_problem_by_id(subject, random.choice(categoryTests))
            print(test)
            # await message.answer(test['condition']['text'])
            try:
                img = requests.get(test['condition']['images'][0])
                img_file = open('C:/Users/arosl/PycharmProjects/egebot/img.svg', 'wb')
                img_file.write(img.content)
                img_file.close()
                convertapi.api_secret = 'PY8ZVrPVo6V5oog1'
                convertapi.convert('png', {
                    'File': 'img.svg'
                }, from_format='svg').save_files('my.png')
                photo = InputFile('my.png')
                # k = sdamgia.get_problem_by_id(subject, random.choice(categoryTests), path_to_img='my.jpg',img='pyppeteer')
                # photo = InputFile('my.jpg')
                await bot.send_photo(chat_id=message.chat.id, photo=photo, caption=test['condition']['text'])
            except Exception:
                await message.answer(test['condition']['text'])


executor.start_polling(dp, skip_updates=True)
