from aiogram import Bot,types
from aiogram.dispatcher.filters import Text
from aiogram.types import InputFile,InputMediaPhoto
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markup
from sdamgia import SdamGIA
import random
import requests
import json
import emoji
import convertapi
from dicts import d_math

TOKEN = '5120464715:AAHnuFfZcZW4wnFVhReAE6SRpMiE6S7mouY'

sdamgia = SdamGIA()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

SUBJECT ='Математика'
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
    global SUBJECT
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    if message.text in markup.d.keys():
        await message.answer('Все задачи', reply_markup=markup.d[message.text][1])
    elif message.text in markup.testList:
        await test_by_category(message)
    elif message.text == 'Сгенерировать тест':
        await generate_test(message,subj=SUBJECT)
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
async def test_by_category(message:types.Message):
    for i in markup.d.keys():
        if message.text.split()[1] == i[:3]:
            markuprepl = ''
            subject = markup.d[i][0]
            id = int(message.text.split()[0])
            try:
                s = random.choice(sdamgia.get_catalog(subject)[int(id) - 1]['categories'])
                categoryTests = sdamgia.get_category_by_id(subject, s['category_id'])
                test = sdamgia.get_problem_by_id(subject, random.choice(categoryTests))
                img = requests.get(test['condition']['images'][0])
                img_file = open('C:/PycharmProjects/telegrambot/img.svg', 'wb')
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

@dp.message_handler()
async def generate_test(message:types.Message,subj):
    problems = {}
    for i in range(1,markup.d[subj][2]+1):
        problems[i] = 1
    await message.answer(sdamgia.generate_pdf('math', sdamgia.generate_test(markup.d[subj][0],problems=problems), nums=True, pdf='h'))
executor.start_polling(dp, skip_updates=True)
