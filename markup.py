from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMain = KeyboardButton('Главное меню')

"""Кнопки из главного меню, выполняющие запрос или перенаправляяющие на другие отделы меню """
# --- Main menu ---
btnPog = KeyboardButton('Погода')
btnWtg = KeyboardButton('Куда пойти?')
btnCat = KeyboardButton('Какое ты животное?')
btnRand = KeyboardButton('Какую оценку поставить?')
btns1=KeyboardButton('Вода')
btns2=KeyboardButton('Земля')
btns3=KeyboardButton('Воздух')
btns4=KeyboardButton('Огонь')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPog, btnWtg, btnCat, btnRand, btns1, btns2, btns3, btns4)

"""Кнопки дополнительного меню, открывающиеся если пользователь нажал на кнопку 'Куда пойти?"""
# ---Other menu---
btnFood=KeyboardButton('Еда')
btnAttr=KeyboardButton('Достопримечательности')
btnCinema=KeyboardButton('Кинотеатры')
btnBack=KeyboardButton('Назад')
"""Добавление всех вышезаданных точек. 
resize_keyboard = True  - отвечает за то, чтобы кнопки подстраивались по размеру"""
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnFood, btnAttr, btnCinema, btnBack)




