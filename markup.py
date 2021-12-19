from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

"""Кнопки из главного меню, выполняющие запрос или перенаправляяющие на другие отделы меню """
# --- Main menu ---
btnPog = KeyboardButton('Погода') #кнопка для того, чтобы узнать погоду в каком-то городе
btnWtg = KeyboardButton('Куда пойти?') #кнопка, перенаправляющая в доп меню с вариантами куда можно сходить
btnRand = KeyboardButton('Какую оценку поставить?') #кнопка, выполняющая запрос
btnPr = KeyboardButton('Приколюхи') #кнопка открывающая меню с разными прикольными функциями
btnKR = KeyboardButton('Криминальная Россия') #Кнопка, открывающая меню с выпусками Криминальной Росии
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPog, btnWtg, btnRand, btnPr, btnKR)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Куда пойти?'"""
# ---Other menu---
btnFood = KeyboardButton('Еда')
btnAttr = KeyboardButton('Поглазеть')
btnCinema = KeyboardButton('Кино')
btnBack = KeyboardButton('Главное меню')
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFood, btnAttr, btnCinema, btnBack)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Приколюхи'"""
# ---Prikolukhi menu---
btnZZ = KeyboardButton('Гороскоп') #при нажатии на эту кнопку откроется меню с гороскопом
btnCat = KeyboardButton('Какое ты животное?') #при нажатии на эту кнопку рандомайзер выдаст картинку
btnTaro = KeyboardButton('Узнай...') #при нажатии на эту кнопку откроется меню с мини-тестами
btnBack1 = KeyboardButton('Главное меню') #при нажатии на эту кнопку пользователь вернется назад в Главное меню
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
prikMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnZZ, btnCat, btnTaro, btnBack1)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Гороскоп'"""
# ---Goroskop menu---
btns1 = KeyboardButton('Вода') #при нажатии на эту кнопку бот отправит гороскоп для водных знаков
btns2 = KeyboardButton('Земля') #при нажатии на эту кнопку бот отправит гороскоп для земных знаков
btns3 = KeyboardButton('Воздух') #при нажатии на эту кнопку бот отправит гороскоп для воздушных знаков
btns4 = KeyboardButton('Огонь') #при нажатии на эту кнопку бот отправит гороскоп для огненных знаков
btnBack2 = KeyboardButton('Назад') #при нажатии на эту кнопку пользователь вернется назад в меню Приколюхи
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
gorMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btns1, btns2, btns3, btns4, btnBack2)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Узнай...'"""
# ---Gadanie menu---
btnf1 = KeyboardButton('Жизненный настрой') #при нажатии на эту кнопку появится мини-тест
btnf2 = KeyboardButton('Комплексы') #при нажатии на эту кнопку появится мини-тест
btnf3 = KeyboardButton('Бизнесмен') #при нажатии на эту кнопку появится мини-тест
btnBack3 = KeyboardButton('Назад') #при нажатии наэту кнопку пользователь вернется назад в меню Приколюхи
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
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
btnBack4 = KeyboardButton('Главное меню') #при нажатии на эту кнопку пользователь вернется назад в Главное меню
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM, btnSp, btnNov, btnEkb, btnKaz, btnNN, btnCh, btnSam,
                                                         btnOm, btnRND, btnUfa, btnKr, btnV, btnPer, btnVol, btnBack4)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Криминальная Россия'"""
# ---Krimenalnaya Rossia---
btnkr95 = KeyboardButton('1995') #при нажатии на эту кнопку бот выдаст рандомную серии 1995 года
btnkr97 = KeyboardButton('1997') #при нажатии на эту кнопку бот выдаст рандомную серии 1997 года
btnkr98 = KeyboardButton('1998') #при нажатии на эту кнопку бот выдаст рандомную серии 1998 года
btnkr1 = KeyboardButton('2001') #при нажатии на эту кнопку бот выдаст рандомную серии 2001 года
btnkr2 = KeyboardButton('2002') #при нажатии на эту кнопку бот выдаст рандомную серии 2002 года
btnBack5 = KeyboardButton('Главное меню') #при нажатии на эту кнопку пользователь вернется назад в Главное меню
"""Добавление всех вышезаданных точек. resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
krimMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnkr95, btnkr97, btnkr98, btnkr1, btnkr2, btnBack5)

