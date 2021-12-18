import re
from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import telebot
import constants
from telebot import types
from main import get_weather
from telebot import types
import requests
import datetime
from urllib3.util import url
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton
import markup as nav
import random
import os

TOKEN = '5069121340:AAEFDLJLYe2HmXmBSTMhmPaj_aTI-rB0k7c'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

"""Функция, запускающая начало работы и высылающая сообщение-приветсвие.
Открывает перед пользователем главное меню."""


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu)


"""Функция, отвечающая за то, какую информацию выдать в зависимости от того,
на какую из предложенных кнопок нажал пользователь. 
Прописываются все исходы событий и выдают информацию исходя из назначения кнопки."""


@dp.message_handler()
async def bot_message(message: types.Message):
    """Исходя из нажатой кнопки отправляется определнный текст"""
    await bot.send_message(message.from_user.id, message.text)
    """Если отправленный текст совпадает с текстом на кнопке, то эта кнопка и используется"""
    if message.text == 'Какую оценку поставить?':
        """random.randint генерирует рандомное число в заданном диапазоне"""
        await bot.send_message(message.from_user.id, 'Ставьте ' + str(random.randint(8, 10)))
    elif message.text == 'Погода':
        await bot.send_message(message.from_user.id, 'Погода в каком городе вас интересует?')
    elif message.text == 'Куда пойти?':
        """reply_markup перенаправляет пользователя в новое место, в данном случае в доп меню"""
        await bot.send_message(message.from_user.id, 'Вот:', reply_markup=nav.otherMenu)
        await message.reply(f"Скоро функционал данного бота будет раширен.\n"
                            f"Следите за обновлениями!\n")
    elif message.text == 'Какое ты животное?':
        await bot.send_message(message.from_user.id, 'Какое ты животное? Правда хочешь узнать?!')
        await message.reply(f"Скоро функционал данного бота будет раширен.\n"
                            f"Следите за обновлениями!\n")
    elif message.text == 'Вода':
        await message.reply(f"----Рыбы----\n"
                            f"Стихия - Вода\n"
                            f"Планета - Нептун\n"
                            f"\n"
                            f"----Рак----\n"
                            f"Стихия - Вода\n"
                            f"Планета - Луна\n"
                            f"\n"
                            f"----Скорпион----\n"
                            f"Стихия - Вода\n"
                            f"Планета - Плутон\n")
    elif message.text == 'Воздух':
        await message.reply(f"----Водолей----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Уран\n"
                            f"\n"
                            f"----Близнецы----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Меркурий\n"
                            f"\n"
                            f"----Весы----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Венера\n")
    elif message.text == 'Земля':
        await message.reply(f"----Телец----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Венера\n"
                            f"\n"
                            f"----Дева----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Меркурий\n"
                            f"\n"
                            f"----Козерог----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Сатурн\n")
    elif message.text == 'Огонь':
        await message.reply(f"----Овен----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Марс\n"
                            f"\n"
                            f"----Лев----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Солнце\n"
                            f"\n"
                            f"----Стрелец----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Юмитер\n")
    elif message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'ну вы и дурак...', reply_markup=nav.mainMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
