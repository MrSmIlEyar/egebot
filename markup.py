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
d = {'Математика':['math',mathMenu,18],'Информатика':['inf',infMenu,23],'Русский язык':['rus',rusMenu,27],
     'Физика':['phys',physMenu,30],'Химия':['chem',chemMenu,34],'Биология':['bio',bioMenu,28],'География':['geo',geoMenu,31],'Обществознание':['soc',socMenu,25],
     'Литература':['lit',litMenu,12],'История':['hist',histMenu,19]}

btnMain = KeyboardButton('Главное меню')
#mainmenu
subjectsButn = KeyboardButton('Выбор предмета')
#subjects = ReplyKeyboardMarkup(resize_keyboard=True).add(subjectsButn)
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
generateTestButn = KeyboardButton('Сгенерировать тест')
for i in d.keys():
    for j in sdamgia.get_catalog(d[i][0]):
        if j['topic_id'].isdigit():
            btnSubject = KeyboardButton(j['topic_id']+' '+i[:3])
            testList.append(j['topic_id']+' '+i[:3])
            d[i][1].add(btnSubject)
    d[i][1].add(generateTestButn)
    d[i][1].add(subjectsButn)