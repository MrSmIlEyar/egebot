from aiogram import Bot, types
from aiogram.types import InputFile, InputMediaPhoto
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
import markup
from sdamgia import SdamGIA
import random
import requests
import emoji
import convertapi
from dicts import d_math, d_inf
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import pyrebase

storage = MemoryStorage()

TOKEN = '5120464715:AAHnuFfZcZW4wnFVhReAE6SRpMiE6S7mouY'

sdamgia = SdamGIA()
storage = MemoryStorage()
subjectInTest = 'math'

subjectInTest = 'math'
bot = Bot(token=TOKEN)

dp = Dispatcher(bot, storage=storage)
SUBJECT = 'math'
TESTID = ''
ANSWER = ''
TestIdDict = {}
GenerateTestDict = {}


class Test(StatesGroup):
    test1 = State()


class Reqst(StatesGroup):
    req1 = State()


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


SUBJECT = 'Математика'


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
    TestIdDict[message.from_user.id] = []
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
    await message.answer_sticker(r'CAACAgIAAxkBAAEEicBiYwqNtEmdLWZpkoNbLyQ7jav-hgACxgEAAhZCawpKI9T0ydt5RyQE')
    await message.answer(f'Приветствую {message.from_user["username"]}, давайте начнем подготовку к ЕГЭ.',
                         reply_markup=markup.mainMenu)


@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.answer('''По всем вопросам обращаться к:
                     @isalahov
                @mr_smile_offical''')


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
    global SUBJECT
    auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
    url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
    if message.text in markup.d.keys():
        SUBJECT = message.text
        await message.answer('Все функции', reply_markup=markup.d[message.text][1])
    elif message.text in markup.testList:
        await est_by_category(message)
    elif message.text == 'Сгенерировать тест':
        await generate_test(message, subj=SUBJECT)
    elif message.text == 'Полезные ссылки':
        await message.answer(markup.d[SUBJECT][3])
    elif message.text == 'Получить тест по id':
        await requestProblem(message)
    elif message.text == 'Выбор предмета':
        await message.answer(emoji.emojize(':clipboard:') +
                             'Каталог предметов', reply_markup=markup.subjectsMenu)
    elif message.text == 'Главное меню':
        await message.answer('Главное меню', reply_markup=markup.mainMenu)
    elif message.text == 'Профиль':
        username = message.from_user["username"]
        supported_user = username.replace('.', '-')
        request = requests.get(url + '?auth=' + auth)
        data = request.json()
        quantify = data[supported_user]['Количество решённых задач']
        await message.answer(emoji.emojize('👤') + 'Профиль:' + '\n\n' +
                             'Имя пользователя: ' + username + '\n' +
                             'Количество решённых задач: ' + quantify, reply_markup=markup.profile)
    elif message.text == 'Помощь':
        await message.answer('''По всем вопросам обращаться к:
                     @isalahov
                @mr_smile_offical''')
    else:
        m = [r'CAACAgIAAxkBAAEEiZtiYvyBc_ylTBf_WdfNv5ni6PAybwACAgEAAladvQpO4myBy0Dk_yQE',
             r'CAACAgIAAxkBAAEEiZliYvxhxEQhHi018c1fvU-_Yx531AACwxMAAm3oEEqGY8B94dy6NCQE',
             r'CAACAgIAAxkBAAEEiaViYwaP9g8y223rq11vw9YSkqqaCAACiAIAAladvQptz6PIxIEdTSQE',
             r'CAACAgIAAxkBAAEEiadiYwbCDDYv1qZVaLY3jWK22cbhoQACxQ4AAoxEmUgDii518Wg0eyQE']
        await message.answer_sticker(random.choice(m))


@dp.message_handler()
async def est_by_category(message: types.Message):
    global TESTID, subjectInTest, ANSWER, TestIdDict
    for i in markup.d.keys():
        if message.text.split()[1] == i[:3]:
            realmarkupd = markup.d[i]
            subjectInTest = realmarkupd[0]
            print(subjectInTest)
            id = int(message.text.split()[0])
            naturalid = id - 1
            if subjectInTest == 'math':
                tests = random.choice(d_math[id - 1])
                TESTID = tests
                ANSWER = tests['answer']
                TestIdDict[message.from_user.id] = [TESTID, ANSWER]
                if len(tests['images']) == 1:
                    await bot.send_photo(chat_id=message.chat.id, photo=tests['images'][0][1],
                                         caption=emoji.emojize(':page_facing_up:') + tests['condition'])
                elif len(tests['images']) == 0:
                    await bot.send_message(chat_id=message.chat.id,
                                           text=emoji.emojize(':page_facing_up:') + tests['condition'])
                else:
                    media = []
                    for photo_id in tests['images']:
                        media.append(InputMediaPhoto(photo_id[1]))
                    await bot.send_message(chat_id=message.chat.id,
                                           text=emoji.emojize(':page_facing_up:') + tests['condition'])
                    await bot.send_media_group(message.from_user.id, media)
                    naturalid = id - 1
                if naturalid < 12:
                    await est(message)
            elif subjectInTest == 'inf':
                tests = random.choice(d_inf[id - 1])
                TESTID = tests
                ANSWER = tests['answer']
                TestIdDict[message.from_user.id] = [TESTID, ANSWER]
                if len(tests['images']) == 1:
                    await bot.send_photo(chat_id=message.chat.id, photo=tests['images'][0][1],
                                         caption=emoji.emojize(':page_facing_up:') + tests['condition'])
                elif len(tests['images']) == 0:
                    await bot.send_message(chat_id=message.chat.id,
                                           text=emoji.emojize(':page_facing_up:') + tests['condition'])
                else:
                    media = []
                    for photo_id in tests['images']:
                        media.append(InputMediaPhoto(photo_id[1]))
                    await bot.send_message(chat_id=message.chat.id,
                                           text=emoji.emojize(':page_facing_up:') + tests['condition'])
                    await bot.send_media_group(message.from_user.id, media)
                await est(message)
            else:
                try:
                    catalog = sdamgia.get_catalog(subjectInTest)
                    s = random.choice(catalog[int(id) - 1]['categories'])
                    categoryTests = sdamgia.get_category_by_id(subjectInTest, s['category_id'])
                    test = sdamgia.get_problem_by_id(subjectInTest, random.choice(categoryTests))
                    img = requests.get(test['condition']['images'][0])
                    img_file = open('C:/PycharmProjects/telegrambot/img.svg', 'wb')
                    img_file.write(img.content)
                    img_file.close()
                    convertapi.api_secret = 'PY8ZVrPVo6V5oog1'
                    convertapi.convert('png', {
                        'File': 'img.svg'
                    }, from_format='svg').save_files('my.png')
                    photo = InputFile('my.png')
                    await bot.send_photo(chat_id=message.chat.id, photo=photo,
                                         caption=emoji.emojize(':page_facing_up:') + test['condition']['text'])
                except Exception:
                    await message.answer(emoji.emojize(':page_facing_up:') + test['condition']['text'])


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


@dp.message_handler()
async def generate_test(message: types.Message, subj):
    global GenerateTestDict
    problems = {}
    for i in range(1, markup.d[subj][2] + 1):
        problems[i] = 1
    id = sdamgia.generate_test(markup.d[subj][0], problems=problems)
    GenerateTestDict[message.from_user.id] = id
    await message.answer(text='Загружается документ')
    await message.answer(
        sdamgia.generate_pdf(markup.d[subj][0], GenerateTestDict[message.from_user.id], nums=True, pdf='h'))
    await message.answer('Ответы:')
    await message.answer(sdamgia.generate_pdf(markup.d[subj][0], GenerateTestDict[message.from_user.id],
                                              nums=True, pdf='h', answers=True))


@dp.message_handler(state=None)
async def est(message: types.Message):
    await Test.test1.set()
    await bot.send_message(chat_id=message.chat.id, text=emoji.emojize(':writing_hand:') + ' Запишите ответ')


@dp.message_handler(state=Test.test1)
async def state1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data[message.from_user.id] = message.text
        trueanswer = TestIdDict[message.from_user.id][1]
        if data[message.from_user.id] == trueanswer:
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
            auth = 'hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV'
            url = 'https://egebot-79552-default-rtdb.europe-west1.firebasedatabase.app/.json'
            username = message.from_user["username"]
            supported_user = username.replace('.', '-')
            request = requests.get(url + '?auth=' + auth)
            data = request.json()
            print(data)
            quantify = int(data[supported_user]['Количество решённых задач'])
            quantify += 1
            firebase = pyrebase.initialize_app(firebaseConfig)
            username = message.from_user['username']
            db = firebase.database()
            a = db.get('hGxeiEIvUIeQeurIKqjuK7KWsBGtq7LqHa6HwTUV')
            data = {"Количество решённых задач": f"{quantify}"}
            db.child(f"{username}").set(data)
            m = [r'CAACAgIAAxkBAAEEialiYwcpTYhO6Nt_VGbJqOwCgtm69QACfgIAAladvQpBYnRfUWys5CQE',
                 r'CAACAgIAAxkBAAEEiZ1iYv1M4NJwDaV1u1dTa6uorfWP2gACRQwAAnqdmEo2Geh166RTLCQE',
                 r'CAACAgIAAxkBAAEEiatiYwdwy2wI0hF0XA5BeWq8UH3YWAACGxMAAlqS2EhjB6Z1XtCrlyQE',
                 r'CAACAgIAAxkBAAEEia1iYweGg6WebIH5kz7_nDbVl9_43AACogEAAhZCawqhd3djmk6DISQE']
            await message.answer_sticker(random.choice(m))
            await message.answer(emoji.emojize(':check_mark_button:') + 'Вы правильно ответили')
        else:
            m = [r'CAACAgIAAxkBAAEEia9iYwgCWX_QFettLvt5cdd0bsPQ2gAC6hgAAqU7iUqsosr9VrUwayQE',
                 r'CAACAgIAAxkBAAEEibFiYwhVH6O0mdyvZmC4I1AjV1NZHwAC6xQAAqPTsEmXDa8Z4Dsg8CQE',
                 r'CAACAgIAAxkBAAEEibViYwjXUl7S0nkagxJfVJz4h41DewACThcAAupwOUlnkUXWDzsgtCQE',
                 r'CAACAgIAAxkBAAEEibdiYwj4-D_lopGL9sbfLgEAAf4yPdIAAqITAALonChIn4AkeJTUYo0kBA']
            await message.answer_sticker(random.choice(m))
            await message.answer(emoji.emojize(':cross_mark:') + 'Вы дали неправильный ответ')
            await bot.send_message(chat_id=message.from_user.id, text='Решение')
            solution = TestIdDict[message.from_user.id][0]['solution']
            await bot.send_photo(chat_id=message.from_user.id, photo=solution)
    await state.finish()


@dp.message_handler(state=None)
async def requestProblem(message: types.Message):
    await Reqst.req1.set()
    await bot.send_message(chat_id=message.chat.id, text='Введите id теста')


@dp.message_handler(state=Reqst.req1)
async def req1_(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['answer'] = message.text
    id = data['answer']
    GenerateTestDict[message.from_user.id] = id
    print(GenerateTestDict[message.from_user.id])
    print(SUBJECT)
    try:
        await message.answer(text='Загружается документ')
        await message.answer(
            sdamgia.generate_pdf(markup.d[SUBJECT][0], GenerateTestDict[message.from_user.id], nums=True, pdf='h'))
    except Exception:
        await message.answer(text = 'Такого теста нет')
    await state.finish()


executor.start_polling(dp, skip_updates=True)
