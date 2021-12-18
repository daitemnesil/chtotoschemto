import re
from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import telebot
import constants
from telebot import types
from main import get_weather
from telebot import types
import asyncio
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

TOKEN = '5069121340:AAEFDLJLYe2HmXmBSTMhmPaj_aTI-rB0k7c'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot) #создали объект класса дистпачер, он нужен для создания хэндлеров

"""Функция, запускающая начало работы и высылающая сообщение-приветсвие.
Открывает перед пользователем главное меню."""
@dp.message_handler(commands=['start']) #ожидает сообщения-команды
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu) #автоматическое сообщение-приветсвие
                           # reply_markup перенаправляет пользователя, в данном случае в главное меню

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
        await bot.send_message(message.from_user.id, 'Выберите город'.format(message.from_user),reply_markup=nav.cityMenu)
    elif message.text == 'Москва' or message.text == 'Санкт-Петербург' or message.text == 'Новосибирск' or message.text == 'Казань'\
        or message.text == 'Нижний Новгород' or message.text == 'Челябинск' or message.text == 'Самара'\
            or message.text == 'Омкс' or message.text == 'Ростов-на-Дону' or message.text == 'Уфа' or message.text == 'Пермь'\
            or message.text == 'Красноярск' or message.text == 'Воронеж' or message.text == 'Волгоград':

        async def mainw():
            city=message.text
            await get_weather(city, open_weather_token)
        async def get_weather(city, open_weather_token):
            # библиотека
            code_to_smile = {
                "Clear": "Ясно \U00002600",
                "Clouds": "Облачно \U00002601",
                "Rain": "Дождливо \U00002614",
                "Drizzle": "Дождливо \U00002614",
                "Thundershtorm": "Гроза \U000026A1",
                "Snow": "Снег \U0001F328"
            }
            try:  # запрос на openweathermap для получения данных
                r = requests.get(
                    f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
                )
                data = r.json()
                # pprint(data)

                city = data["name"]
                cur_weather = data["main"]["temp"]

                weather_description = data["weather"][0]["main"]
                if weather_description in code_to_smile:
                    wd = code_to_smile[weather_description]
                else:
                    wd = "\U00000001"

                humidity = data["main"]["humidity"]  # значение влажности
                pressure = data["main"]["pressure"]  # значение давления
                wind = data["wind"]["speed"]  # значение скорости ветра
                sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])  # время рассвета
                sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])  # ремя заката

                # Возвращаются необходимые данные, задается оформление
                await message.reply(f"----{datetime.datetime.now().strftime('%d-%m-%y %H:%M')}----\n"
                             f"Погода в городе {city} на текущий момент:\nТемпература: {cur_weather}°С {wd}\n"
                             f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст.\n"
                             f"Скорость ветра: {wind}м/с\nВремя рассвета: {sunrise}\nВремя заката: {sunset}\n"
                             f"\n"
                             f"Защити себя от коронавируса - ПОСТАВЬ ПРИВИВКУ\n"
                             f"Госуслуги - проще, чем кажется\n"
                             f"Не болейте!")
            except:
                await message.reply('Ошибка! Проверьте название введенного города.')
                handle = None

        if __name__ == "__main__":
            await mainw()

    elif message.text == 'Куда пойти?':
        """reply_markup перенаправляет пользователя в новое место, в данном случае в доп меню"""
        await bot.send_message(message.from_user.id, 'Выберите:', reply_markup=nav.otherMenu)
    elif message.text == 'Еда':
        await bot.send_message(message.from_user.id, 'Тебе бы на диету, но ладно...')
    elif message.text == 'Поглазеть':
        await bot.send_message(message.from_user.id, 'Надо же, удивительно, не вариант с едой...')
    elif message.text == 'Кино':
        await bot.send_message(message.from_user.id, 'Хочешь спойлер? Ладно-ладно, не буду...')
    elif message.text == 'Какое ты животное?':
        await bot.send_message(message.from_user.id, 'Какое ты животное? Правда хочешь узнать?!')
        await message.reply(f"Скоро функционал данного бота будет раширен.\n"
                            f"Следите за обновлениями!\n")
    elif message.text == 'Вода':
        await message.reply(f"----Рыбы----\n" #\n переносит на новую строку
                            f"Стихия - Вода\n" #f - начало новой строки
                            f"Планета - Нептун\n"
                            f"Рыбы – изменчивые и непрактичные. Хорошо развитое воображение и богатый внутренний мир\n"
                            f"часто уводят Рыб в страну грез. Фантазии и мечты настолько заполняют жизнь, что порой\n"
                            f"этому знаку очень трудно адаптироваться к реальному миру. Рыбы умеют сочувствовать\n"
                            f"и сопереживать, они всегда утешат в трудную минуту и помогут нуждающимся.\n"
                            f"\n"
                            f"----Рак----\n"
                            f"Стихия - Вода\n"
                            f"Планета - Луна\n"
                            f"Рак – чувствительный и проницательный. Эмоциональное состояние этого знака напрямую\n"
                            f"зависит от взаимоотношений с окружающими людьми и часто меняется. Смена настроений\n"
                            f"приводит к тому, что Раки переходят от активной деятельности к пассивному состоянию.\n"
                            f"Однако отличная интуиция и внимание к мелочам помогают им выйти из самых сложных ситуаций.\n"
                            f"\n"
                            f"----Скорпион----\n"
                            f"Стихия - Вода\n"
                            f"Планета - Плутон\n"
                            f"Скорпион – мужественный и стойкий. Бури страстей, одолевающие этот знак, не всегда\n"
                            f"находятся под контролем. Скорпионам свойственны страстные увлечения, отчаянная ревность\n"
                            f"и даже агрессия. Однако в большинстве случаев эти эмоции не выходят наружу, а остаются внутри,\n"
                            f"провоцируя глубокие переживания.\n")
    elif message.text == 'Воздух':
        await message.reply(f"----Водолей----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Уран\n"
                            f"Водолей – свободолюбивый и эксцентричный. Всегда настаивает на своей правоте и имеет\n"
                            f"обо всем свое суждение. Необычный и независимый Водолей всегда идет по своему пути,\n"
                            f"не обращая внимания на установленные в обществе правила. Бунтарский характер этого знака\n"
                            f"уравновешивается обостренным чувством справедливости и безграничной честностью.\n"
                            f"\n"
                            f"----Близнецы----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Меркурий\n"
                            f"Близнецы – любознательны и контактны. Могут обрабатывать огромное количество информации,\n"
                            f"постоянно пополняя копилку своих знаний. Имеют развитый интеллект,\n"
                            f"нестандартное мышление и огромное количество друзей и знакомых.\n"
                            f"\n"
                            f"----Весы----\n"
                            f"Стихия - Воздух\n"
                            f"Планета - Венера\n"
                            f"Весы – уравновешены и дипломатичны. Редко проявляют эмоции,\n"
                            f"оставляя все переживания внутри, и стараются поддерживать со всеми хорошие отношения.\n"
                            f"Они влюбчивы и эстетичны, тонко чувствуют красоту окружающего мира,\n"
                            f"нетерпимы к грубости и дурному вкусу.\n")
    elif message.text == 'Земля':
        await message.reply(f"----Телец----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Венера\n"
                            f"Телец – талантливый и трудолюбивый. Этот знак отличает постоянство и стремлениек комфорту,\n"
                            f"а также запасливость, расчетливость и практичность. Тельцы настоящие коллекционеры,\n"
                            f"причем не только материальных ценностей, но и жизненного опыта.\n"
                            f"\n"
                            f"----Дева----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Меркурий\n"
                            f"Дева – чувственная и ранимая. Дева отлично приспосабливается к обстоятельствам,\n"
                            f"обладает безграничным терпением и поразительной работоспособностью.\n"
                            f"Аккуратные и педантичные Девы выполняют любое дело неторопливо и основательно,\n"
                            f"предъявляя высокие требования к себе и окружающим.\n"
                            f"\n"
                            f"----Козерог----\n"
                            f"Стихия - Земля\n"
                            f"Планета - Сатурн\n"
                            f"Козерог – надежный и прагматичный. Организаторские способности Козерогов, а также умение\n"
                            f"планировать возносят их на самый верх социальной пирамиды. Талантливые руководители и\n"
                            f"прирожденные лидеры, Козероги все держат под контролем и могут справиться с любой ситуацией.\n")
    elif message.text == 'Огонь':
        await message.reply(f"----Овен----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Марс\n"
                            f"Овен – импульсивный и независимый. Смел, уверен в себе и энергичен,\n"
                            f"проявляет невероятное упорство в достижении целей и колоссальное трудолюбие.\n"
                            f"Острый ум и сильная воля делают этот знак одним из самых ярких,\n"
                            f"однако ладить с Овнами весьма непросто.\n"
                            f"\n"
                            f"----Лев----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Солнце\n"
                            f"Лев – харизматичный и притягательный. Он открыт, дружелюбен и силен,\n"
                            f"может с легкостью повести за собой людей, поэтому имеет много друзей и почитателей.\n"
                            f"От своего окружения требует безоговорочного подчинения и преданности,\n"
                            f"очень ценит крепкую дружбу и всегда готов придти на помощь.\n"
                            f"\n"
                            f"----Стрелец----\n"
                            f"Стихия - Огонь\n"
                            f"Планета - Юмитер\n"
                            f"Cтрелец - мечтательный и бесстрашный. Стрелец - путешественник и первооткрыватель,\n"
                            f"он отличается любознательностью и жаждой знаний,\n"
                            f"однако порой вспыльчив и чересчур эмоционален.\n")
    elif message.text == 'Назад': # возвращает пользователя в главное меню
        await bot.send_message(message.from_user.id, 'ну вы и дурак...', reply_markup=nav.mainMenu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
