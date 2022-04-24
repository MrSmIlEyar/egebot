from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from sdamgia import SdamGIA

sdamgia = SdamGIA()
mathMenu = ReplyKeyboardMarkup(resize_keyboard=True)
infMenu = ReplyKeyboardMarkup(resize_keyboard=True)
rusMenu = ReplyKeyboardMarkup(resize_keyboard=True)
physMenu = ReplyKeyboardMarkup(resize_keyboard=True)
chemMenu = ReplyKeyboardMarkup(resize_keyboard=True)
bioMenu = ReplyKeyboardMarkup(resize_keyboard=True)
geoMenu = ReplyKeyboardMarkup(resize_keyboard=True)
socMenu = ReplyKeyboardMarkup(resize_keyboard=True)
litMenu = ReplyKeyboardMarkup(resize_keyboard=True)
histMenu = ReplyKeyboardMarkup(resize_keyboard=True)
d = {'Математика': ['math', mathMenu, 18, '''https://www.youtube.com/c/ШколковоЕГЭпоматематике
https://www.youtube.com/c/pifagor1
https://www.youtube.com/channel/UCSdmht0kbvfnItRMNcr4qZA
https://www.youtube.com/channel/UCvffROOTDLzYGb4_9-ReyOg'''], 'Информатика': ['inf', infMenu, 23, '''https://www.youtube.com/channel/UCqZvYprH2ornRwwMYbPoDYA
https://www.youtube.com/c/%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%91%D0%A3
https://www.youtube.com/channel/UCMaXzRQ7_TpfVWgbEXQOH7w'''], 'Русский язык': ['rus', rusMenu, 27, 'В разработке'],
     'Физика': ['phys', physMenu, 30, 'В разработке'], 'Химия': ['chem', chemMenu, 34, 'В разработке'],
     'Биология': ['bio', bioMenu, 28, 'В разработке'], 'География': ['geo', geoMenu, 31, 'В разработке'],
     'Обществознание': ['soc', socMenu, 25, 'В разработке'],
     'Литература': ['lit', litMenu, 12, 'В разработке'], 'История': ['hist', histMenu, 19, 'В разработке']}

btnMain = KeyboardButton('Главное меню')
# mainmenu
subjectsButn = KeyboardButton('Выбор предмета')
# subjects = ReplyKeyboardMarkup(resize_keyboard=True).add(subjectsButn)
btnback = KeyboardButton('Главное меню')
profile = ReplyKeyboardMarkup(resize_keyboard=True).add(btnback)

btnHelp = KeyboardButton('Помощь')
btnChoiceSubject = KeyboardButton('Выбор предмета')
btnProfile = KeyboardButton('Профиль')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnProfile, btnChoiceSubject, btnHelp)
# subjectsmenu
subjectsMenu = ReplyKeyboardMarkup(resize_keyboard=True)
for i in d.keys():
    btnSubject = KeyboardButton(i)
    subjectsMenu.add(btnSubject)
subjectsMenu.add(btnMain)

# categorymenu
testList = []
generateTestButn = KeyboardButton('Сгенерировать тест')
infoButn = KeyboardButton('Полезные ссылки')
requestButn = KeyboardButton("Получить тест по id")
for i in d.keys():
    for j in sdamgia.get_catalog(d[i][0]):
        if j['topic_id'].isdigit():
            btnSubject = KeyboardButton(j['topic_id'] + ' ' + i[:3])
            testList.append(j['topic_id'] + ' ' + i[:3])
            d[i][1].add(btnSubject)
    d[i][1].add(generateTestButn)
    d[i][1].add(infoButn)
    d[i][1].add(requestButn)
    d[i][1].add(subjectsButn)
