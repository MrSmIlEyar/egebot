from dicts import d_inf
import json
from aiogram.types import InputFile
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from sdamgia import SdamGIA
import convertapi
import requests

d = {'Математика': ['math', 18], 'Информатика': ['inf', 23], 'Русский язык': ['rus'],
     'Физика': ['phys'], 'Химия': ['chem'], 'Биология': ['bio'], 'География': ['geo'], 'Обществознание': ['soc'],
     'Литература': ['lit'], 'История': ['hist']}
TOKEN = '5120464715:AAHnuFfZcZW4wnFVhReAE6SRpMiE6S7mouY'
MY_ID = '612579531'
sdamgia = SdamGIA()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
s = d_inf

@dp.message_handler()
async def est_by_category(message: types.Message):
    for idc in range(7,23):
        for i in range(len(s[idc])):
            path_to_img = 'img.jpg'
            sdamgia.get_problem_by_id('inf', s[idc][i]['id'], img='grabzit', path_to_img=path_to_img,
                                      grabzit_auth={"AppKey": "YjhhN2Q3YTFlNWI0NDIxNjlhZmEyMTRmZTA1OWJmNDk=",
                                                    "AppSecret": "Yj9YQT8/bD9aWT96Pz8hPz8/Pz8/P1YNPT9ZTUlybUI="})
            photos = InputFile('img.jpg')
            id_photo = await bot.send_photo(chat_id=MY_ID, photo=photos)
            id = id_photo['photo'][0]['file_id']
            s[idc][i]['solution'] = id
        print(s)

print(s)
s_json = json.dumps(s)
with open("main.json", "w") as my_file:
    my_file.write(s_json)
executor.start_polling(dp, skip_updates=True)