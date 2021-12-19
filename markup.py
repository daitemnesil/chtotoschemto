from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

"""Кнопки из главного меню, выполняющие запрос или перенаправляяющие на другие отделы меню """
# --- Main menu ---
btnPog = KeyboardButton('Погода') #кнопка для того, чтобы узнать погоду в каком-то городе
btnWtg = KeyboardButton('Куда пойти?') #кнопка, перенаправляющая в доп меню с вариантами куда можно сходить
btnRand = KeyboardButton('Какую оценку поставить?')
btnPr = KeyboardButton('Приколюхи')
btnKR = KeyboardButton('Криминальная Россия')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPog, btnWtg, btnRand, btnPr, btnKR)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Куда пойти?'"""
# ---Other menu---
btnFood = KeyboardButton('Еда')
btnAttr = KeyboardButton('Поглазеть')
btnCinema = KeyboardButton('Кино')
btnBack = KeyboardButton('Главное меню')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFood, btnAttr, btnCinema, btnBack)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Приколюхи'"""
# ---Prikolukhi menu---
btnZZ = KeyboardButton('Гороскоп')
btnCat = KeyboardButton('Какое ты животное?')
btnTaro = KeyboardButton('Узнай...')
btnBack1 = KeyboardButton('Главное меню')
prikMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnZZ, btnCat, btnTaro, btnBack1)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Гороскоп'"""
# ---Goroskop menu---
btns1 = KeyboardButton('Вода')
btns2 = KeyboardButton('Земля')
btns3 = KeyboardButton('Воздух')
btns4 = KeyboardButton('Огонь')
btnBack2 = KeyboardButton('Назад')
gorMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btns1, btns2, btns3, btns4, btnBack2)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Узнай...'"""
# ---Gadanie menu---
btnf1 = KeyboardButton('Жизненный настрой')
btnf2 = KeyboardButton('Комплексы')
btnf3 = KeyboardButton('Бизнесмен')
btnBack3 = KeyboardButton('Назад')
gadMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnf1, btnf2, btnf3, btnBack3)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Погода'"""
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
btnBack4 = KeyboardButton('Главное меню')
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM, btnSp, btnNov, btnEkb, btnKaz, btnNN, btnCh, btnSam,
                                                         btnOm, btnRND, btnUfa, btnKr, btnV, btnPer, btnVol, btnBack4)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Криминальная Россия'"""
# ---Krimenalnaya Rossia---
btnkr95 = KeyboardButton('1995')
btnkr97 = KeyboardButton('1997')
btnkr98 = KeyboardButton('1998')
btnBack5 = KeyboardButton('Главное меню')
krimMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnkr95, btnkr97, btnkr98, btnBack5)

