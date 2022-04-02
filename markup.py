from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from sdamgia import SdamGIA

sdamgia = SdamGIA()
mathMenu = ReplyKeyboardMarkup(resize_keyboard=True)
infMenu = ReplyKeyboardMarkup(resize_keyboard=True)
rusMenu = ReplyKeyboardMarkup(resize_keyboard=True)
physMenu=ReplyKeyboardMarkup(resize_keyboard=True)
chemMenu =ReplyKeyboardMarkup(resize_keyboard=True)
bioMenu = ReplyKeyboardMarkup(resize_keyboard=True)
geoMenu = ReplyKeyboardMarkup(resize_keyboard=True)
socMenu = ReplyKeyboardMarkup(resize_keyboard=True)
litMenu = ReplyKeyboardMarkup(resize_keyboard=True)
histMenu = ReplyKeyboardMarkup(resize_keyboard=True)
d = {'Математика':['math',mathMenu],'Информатика':['inf',infMenu],'Русский язык':['rus',rusMenu],
     'Физика':['phys',physMenu],'Химия':['chem',chemMenu],'Биология':['bio',bioMenu],'География':['geo',geoMenu],'Обществознание':['soc',socMenu],
     'Литература':['lit',litMenu],'История':['hist',histMenu]}

btnMain = KeyboardButton('Главное меню')
#mainmenu
backButn = KeyboardButton('Назад')
back = ReplyKeyboardMarkup(resize_keyboard=True).add(backButn)
btnback = KeyboardButton('Главное меню')
profile = ReplyKeyboardMarkup(resize_keyboard=True).add(btnback)

btnHelp = KeyboardButton('Помощь')
btnChoiceSubject = KeyboardButton('Выбор предмета')
btnProfile = KeyboardButton('Профиль')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile,btnChoiceSubject,btnHelp)
#subjectsmenu
subjectsMenu = ReplyKeyboardMarkup(resize_keyboard=True)
for i in d.keys():
    btnSubject = KeyboardButton(i)
    subjectsMenu.add(btnSubject)
subjectsMenu.add(btnMain)

#categorymenu
testList = []
for i in d.keys():
    for j in sdamgia.get_catalog(d[i][0]):
        if j['topic_id'].isdigit():
            btnSubject = KeyboardButton(j['topic_id']+i[:3])
            testList.append(j['topic_id']+i[:3])
            d[i][1].add(btnSubject)
#categorynamemenu