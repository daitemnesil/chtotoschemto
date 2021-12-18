from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

"""Кнопки из главного меню, выполняющие запрос или перенаправляяющие на другие отделы меню """
# --- Main menu ---
btnPog = KeyboardButton('Погода') #кнопка для того, чтобы узнать погоду в каком-то городе
btnWtg = KeyboardButton('Куда пойти?') #кнопка, перенаправляющая в доп меню с вариантами куда можно сходить
btnCat = KeyboardButton('Какое ты животное?')
btnRand = KeyboardButton('Какую оценку поставить?')
btns1 = KeyboardButton('Вода')
btns2 = KeyboardButton('Земля')
btns3 = KeyboardButton('Воздух')
btns4 = KeyboardButton('Огонь')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPog, btnWtg, btnCat, btnRand, btns1, btns2, btns3, btns4)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Куда пойти?"""
# ---Other menu---
btnFood = KeyboardButton('Еда')
btnAttr = KeyboardButton('Поглазеть')
btnCinema = KeyboardButton('Кино')
btnBack = KeyboardButton('Назад')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFood, btnAttr, btnCinema, btnBack)

# ---City---
btnM = KeyboardButton('Москва')
btnSp = KeyboardButton('Санкт-Петербург')
btnNov = KeyboardButton('Новосибирск')
btnEkb = KeyboardButton('Екатеринбург')
btnKaz = KeyboardButton('Казань')
btnNN = KeyboardButton('Нижний Новгород')
btnCh = KeyboardButton('Челябинск')
btnSam = KeyboardButton('Самара')
btnOm = KeyboardButton('Омск')
btnRND = KeyboardButton('Ростов-на-Дону')
btnUfa = KeyboardButton('Уфа')
btnKr = KeyboardButton('Красноярск')
btnV = KeyboardButton('Воронеж')
btnPer = KeyboardButton('Пермь')
btnVol = KeyboardButton('Волгоград')
btnBack = KeyboardButton('Назад')
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM, btnSp, btnNov, btnEkb, btnKaz, btnNN, btnCh, btnSam,
                                                         btnOm, btnRND, btnUfa, btnKr, btnV, btnPer, btnVol, btnBack)
