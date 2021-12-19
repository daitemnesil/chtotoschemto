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
import googlemaps

gmaps = googlemaps.Client(key='AIzaSyDIn_YgBAoiJrrxw1_HrW9rJ2kMaPggumY')

TOKEN = '5069121340:AAEFDLJLYe2HmXmBSTMhmPaj_aTI-rB0k7c'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)  # создали объект класса дистпачер, он нужен для создания хэндлеров

"""Функция, запускающая начало работы и высылающая сообщение-приветсвие.
Открывает перед пользователем главное меню."""


@dp.message_handler(commands=['start'])  # ожидает сообщения-команды
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello {0.first_name}'.format(message.from_user),
                           reply_markup=nav.mainMenu)  # автоматическое сообщение-приветсвие
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
    elif message.text == 'Погода': # при нажатии кнопки Погода пользователя перенаправляет в меню с выбором города
        await bot.send_message(message.from_user.id, 'Выберите город'.format(message.from_user),
                               reply_markup=nav.cityMenu)
    elif message.text == 'Москва' or message.text == 'Санкт-Петербург' or message.text == 'Новосибирск' or message.text == 'Казань' \
            or message.text == 'Нижний Новгород' or message.text == 'Челябинск' or message.text == 'Самара' \
            or message.text == 'Омкс' or message.text == 'Ростов-на-Дону' or message.text == 'Уфа' or message.text == 'Пермь' \
            or message.text == 'Красноярск' or message.text == 'Воронеж' or message.text == 'Волгоград':

        """Функция, получает на вход сообщение исходя из выбранной пользователем кнопки с городом"""
        async def mainw():
            city = message.text
            await get_weather(city, open_weather_token)

        """"Функция проводит поиск информации на openweather maps b возвращающает погодные условия в определенном городе"""
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
                await message.reply(f"----{datetime.datetime.now ().strftime ('%d-%m-%y %H:%M')}----\n"
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

    elif message.text == 'Куда пойти?': # при нажатии 'Куда пойти?' попадаем в меню вариантов досуга
        """reply_markup перенаправляет пользователя в новое место, в данном случае в доп меню"""
        await bot.send_message(message.from_user.id, 'Пока что данная функция доступна только для Москвы.', reply_markup=nav.otherMenu)
    elif message.text == 'Еда':
        await bot.send_message(message.from_user.id, 'Тебе бы на диету, но ладно...')
        await message.reply(f"САЛЮТ\n"
                            f"каждый день с 08.00 до 23.00\n"
                            f"https://instagram.com/salutecoffee?utm_medium=copy_link\n"
                            f"Strastnoy boulevard 12 bld. 5\n"
                            f"\n"
                            f"YUMBAKER\n"
                            f"Yumbaker Home с 08.00 до 20.00\n"
                            f"Yumbaker Gardens с 09.00 до 21.00\n"
                            f"https://now.yumbaker.ru/\n"
                            f"Yumbaker Home м. Добрынинская, Пятницкая 66с1\n"
                            f"Yumbaker Gardens м. Проспект Мира, пр-т. Мира 26с1\n"
                            f"\n"
                            f"KAIF BURGER\n"
                            f"каждый день с 11.00 до 23.00\n"
                            f"https://instagram.com/kaif_burger?utm_medium=copy_link\n"
                            f"Никольская ул., 10/2, стр.2Б\n")


    elif message.text == 'Поглазеть': # при нажатии кнопки Поглазеть получаем варианты того, что можно посетить
        await bot.send_message(message.from_user.id, 'Надо же, удивительно, не вариант с едой...')
        await message.reply(f"Как стретить Новый год экологично - онлайн-дискуссия\n"
                            f"21 декабря в 18.00\n"
                            f"https://dvizhenie-razdelnyy-event.timepad.ru/event/1856971/\n"
                            f"Бесплатно при регистрации\n"
                            f"\n"
                            f"Арт-бранч 'Щелкунчик'\n"
                            f"24 декабря в 20.00\n"
                            f"https://creativediaspora.timepad.ru/event/1870789/\n"
                            f"Стоимость билета - 700р\n"
                            f"\n"
                            f"Благотворительная ярмарка Rassvet Christmas Fair\n"
                            f"25 и 26 декабря в 12.00\n"
                            f"Вход свободный по регистрации\n"
                            f"https://dkrassvet.space/events/rassvet-christmas-fair/\n"
                            f"\n"
                            f"Рождественский киноквиз\n"
                            f"25 декабря в 17.00\n"
                            f"Стоимость билета - 400р\n"
                            f"https://www.museikino.ru/events/rozhdestvenskiy-kinokviz-podvedenie-itogov-kinogoda/\n")
    elif message.text == 'Бары':  # при нажатии кнопки Бары получаем варианты баров
        await bot.send_message(message.from_user.id, 'Мда...алкоголизм...ладно, ищу...')
        await message.reply( f"MEOW BAR\n"
                             f"по будням с 17.00 до 04.00\n"
                             f"по выходным с 12.00 до 04.00\n"
                             f"http://meowbar.ru/\n"
                             f"ул. Кузнецкий мост 19 с1\n"
                             f"\n"
                             f"ДЕЛАЙ КУЛЬТУРУ\n"
                             f"пн с 18.00 до 00.00\n"
                             f"вт-чт с 16.00 до 00.00\n"
                             f"пт-сб с 16.00 до 01.00\n"
                             f"https://delaikultu.ru/\n"
                             f"Милютинский переулок, дом 15 с1\n"
                             f"\n"
                             f"ЙУХ\n"
                             f"пн-пт с 12.00 до 23.00\n"
                             f"сб-вс с 14.00 до 23.00\n"
                             f"https://delaikultu.ru/\n"
                             f"Милютинский переулок, дом 15 с1\n")
    elif message.text == 'Приколюхи':
        await bot.send_message(message.from_user.id, 'Добро пожаловать в самую странную часть:',
                               reply_markup=nav.prikMenu)
    elif message.text == 'Какое ты животное?':
        await bot.send_message(message.from_user.id, 'Правда хочешь узнать?!')
        img_list = ['img_list/img_1.jpg', 'img_list/img_2.jpg', 'img_list/img_3.jpg', 'img_list/img_4.jpg',
                    'img_list/img_5.jpg', 'img_list/img_6.jpg', 'img_list/img_7.jpg']
        img_path = random.choice(img_list)  # выбирается рандомная картинка
        await bot.send_photo(message.chat.id, photo=open(img_path, 'rb'))  # рандомная картинка отправляется пользователю
    elif message.text == 'Узнай...':
        await bot.send_message(message.from_user.id, 'Выбери, что хочешь о себе узнать:', reply_markup=nav.gadMenu)
    elif message.text == 'Жизненный настрой':
        await message.reply(f"Внимательно посмотрите на амулеты и долго не думая выберите понравившийся!\n")
        pic_list = ['pic_list/p_1.jpg']
        img_path2 = random.choice(pic_list)
        await bot.send_photo(message.chat.id, photo=open(img_path2, "rb"))
        await message.reply(
            f"1. Этот амулет предпочитают люди стремящиеся к личностному росту.\n"  # \n переносит на новую строку
            f"Вы сейчас находитесь в поиске различных идей, от результата которого будет зависеть вся\n"  # f - начало новой строки
            f"дальнейшая жизнь. Постарайтесь скорее обрести себя и сформировать желания и цели на\n"
            f"дальнейшую жизнь.Чем раньше вы это сделаете, тем больших успехов сможете достичь.\n"
            f"\n"
            f"2. Скорее всего, вам мешают внешние обстоятельства или другие люди! В скором времени вы\n"
            f"сможете расширить свои границы и возможности. Не позволяйте другим людям препятствовать вам.\n"
            f"Установите четкие личные границы.\n"
            f"\n"
            f"3. Амулет указывает на то, что вы морально истощились и физически устали.\n"
            f"Этот амулет ассоциируется с грядущей свободой и раскрепощением. Сейчас самое время\n"
            f"отдохнуть, и разработать четкий план.\n"
            f"\n"
            f"4. Значение этого амулета наиболее благоприятное. Его выбирают удачливые люди.\n"
            f"Если на данном этапе у вас и имеются некоторые проблемы, то в скором времени они\n"
            f"разрешатся, и все сложится наилучшим образом. Сохраняйте свой жизненный настрой,\n"
            f"и вам всегда будет сопутствовать удача.\n"
            f"\n"
            f"5. У вас хорошо развита интуиция, но вы еще не до конца разобрались, как этим воспользоваться.\n"
            f"Если сейчас имеются вопросы, то в скором времени вы получите знак, как их лучше разрешить.\n"
            f"Доверяйте своему внутреннему голосу, и присмотритесь к знакам судьбы.\n"
            f"\n"
            f"6. Такой выбор говорит о грядущих событиях, которые изменят вашу жизнь к лучшему.\n"
            f"Этот амулет определяет вам финансовый достаток и успех в делах. Не следует надеяться,\n"
            f"что все разрешится без вашего участия. Продолжайте работать, и тогда вас ожидает успех.\n")
    elif message.text == 'Комплексы':
        await message.reply(f"Выберете узел, не стоит долго думать.\n")
        pic_list = ['pic_list/p_2.jpg']
        img_path3 = random.choice(pic_list)
        await bot.send_photo(message.chat.id, photo=open(img_path3, "rb"))
        await message.reply(
            f"1. Вы очень сильно комплексуете по поводу своей внешности. Вас не устраивают ваши параметры\n"  # \n переносит на новую строку
            f"вашего тела или некоторые черты лица. Вам хотелось бы выглядеть лучше и красивее.\n"  # f - начало новой строки
            f"Но на самом деле, вся наша красота внутри нас. Важно принять себя и полюбить таким,\n"
            f"какой вы есть на самом деле. Стремиться быть лучше это хорошо. Но важно сначала полюбить себя.\n"
            f"\n"
            f"2. Ваш комплекс состоит в том, что вам трудно найти общий язык с другими людьми.\n"
            f"Вы зажаты в разговоре. Вам сложно начать диалог с посторонним, незнакомым человеком.\n"
            f"Необходимо пройти курс по психологии, чтобы избавиться от этого комплекса.\n"
            f"\n"
            f"3. Вы сравниваете себя постоянно с другими людьми. Вам кажется, что кто-то умнее, красивее,\n"
            f"талантливее вас. И это так. Всегда найдется такой человек. Но вы смотрите на эту проблему\n"
            f"не под тем углом. Вам нужно находить ваши достоинства, которых нет ни у кого кроме вас.\n"
            f"Ищите в себе больше плюсов, а не минусов.\n"
            f"\n"
            f"4. А вот у вас комплекс отличника. Вы любите доводить все до идеала. У вас дома и пылинки не\n"
            f"найдешь. Вы вымываете свои тарелки сразу же после еды. Не дай бог они у вас простоят\n"
            f"лишних 5 минут без присмотра. На эту тему можно много утрировать, но лучше понять суть\n"
            f"проблемы. Вы несчастный человек, потому что не можете себе позволить расслабиться.\n"
            f"Вам нужно делать все безупречно. Конечно, если вас делает это счастливым человеком — делайте это.\n"
            f"Просто помните, что вы можете позволить себе совершать иногда ошибки и не быть идеальной личностью.\n")
    elif message.text == 'Бизнесмен':
        await message.reply(f"Выберите только 1 картинку.\n")
        pic_list = ['pic_list/p_3.jpg']
        img_path4 = random.choice(pic_list)
        await bot.send_photo(message.chat.id, photo=open(img_path4, "rb"))
        await message.reply(
            f"1. Вы являетесь творческим человеком, поэтому, вероятнее всего, вам не стоит заниматься\n"  # \n переносит на новую строку
            f"бизнесом. В крайнем случае попробуйте совместить бизнес и творчество, тогда вас может ждать\n"  # f - начало новой строки
            f"успех. Вы привыкли мыслить ни как все, поэтому рядом с вами должен быть человек,\n"
            f"который будет помогать в некоторых вопросах.\n"
            f"\n"
            f"Вам суждено стать бизнесменом, причем довольно успешным. Вы имеете аналитический склад ума,\n"
            f"поэтому сложные задачи, которые сложны для других, вы решаете на автоматизме. Даже если\n"
            f"вы не можете найти общую точку зрения с человеком, то вы сделаете все, чтобы уговорить\n"
            f"его встать на вашу сторону. Любой бизнес вам дастся с легкостью.\n"
            f"\n"
            f"У вас есть шанс стать бизнесменом, однако, вам не хватает опыта. Посещайте курсы,\n"
            f"читайте больше книг, и тогда вы придете к совершенству. Возможно, вам нужно познакомиться\n"
            f"с человеком, который уже имеет опыт в этом деле. И помните, что любое дело требует не только\n"
            f"ответственности, но и усердных стараний.\n")
    elif message.text == 'Вода':
        await message.reply(
                            f"----Рыбы----\n"  # \n переносит на новую строку
                             f"Стихия - Вода\n"  # f - начало новой строки
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
    elif message.text == 'Гороскоп':
        await bot.send_message(message.from_user.id, 'Выберите свою стихию:', reply_markup=nav.gorMenu)
    elif message.text == 'Воздух':
        await message.reply(
                            f"----Водолей----\n"
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
        await message.reply(
                            f"----Телец----\n"
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
        await message.reply(
                            f"----Овен----\n"
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
    elif message.text == 'Криминальная Россия':
        await bot.send_message(message.from_user.id, 'Выпуски какого года?', reply_markup=nav.krimMenu)
    elif message.text == '1995':
        kr95_list = ["https://youtu.be/26YEFSJGixY", "https://youtu.be/KeYRbrQ1_6k", "https://youtu.be/q9aevIXuaWY",
                     "https://youtu.be/vjdE9cNr69U", "https://youtu.be/RkaXHH9p9Hg", "https://youtu.be/G6b9z_6BnNk",
                     "https://youtu.be/GL1_SOC35Bc", "https://youtu.be/rxxfJMzBpCY", "https://youtu.be/xYwGlMBFsQk",
                     "https://youtu.be/SFES1rT1ob0", "https://youtu.be/hz-BBa-NzYg", "https://youtu.be/bQoXv2jzoDo",
                     "https://youtu.be/2f1IaZyAH-4"]
        await message.reply(random.choice(kr95_list))
    elif message.text == '1997':
        kr97_list = ["https://youtu.be/Z6awn_67JHI", "https://youtu.be/rMgT523vV8M", "https://youtu.be/xWyPLqxFd2E",
                     "https://youtu.be/xAgVYCAJYKM", "https://youtu.be/H0eZae2RZ7o", "https://youtu.be/fNDRbaQsjwY",
                     "https://youtu.be/qEmtNJnJKVk"]
        await message.reply(random.choice(kr97_list))
    elif message.text == '1998':
        kr98_list = ["https://youtu.be/TkGinelJZ1I", "https://youtu.be/filyf2cvsEI", "https://youtu.be/YSDsr8PmTbY",
                     "https://youtu.be/Znd9UFaH1xc", "https://youtu.be/PHJLKatR3Xk", "https://youtu.be/OiwTyMmZkhA",
                     "https://youtu.be/4wqd2P33qFo", "https://youtu.be/-7W6S2-3FOg", "https://youtu.be/IPXBoIchFlQ",
                     "https://youtu.be/x_nbiiSFFlY", "https://youtu.be/S261nGfcNGU", "https://youtu.be/tsPvsDIfNP8",
                     "https://youtu.be/yemsD1mUlUM", "https://youtu.be/UJszlW-S-7U", "https://youtu.be/jtd43ehuWAM",
                     "https://youtu.be/2HEHceD6nK4", "https://youtu.be/x5nm9K_iwFQ, https://youtu.be/4EQ9gDuUnWo"]
        await message.reply(random.choice(kr98_list))
    elif message.text == '2001':
        kr1_list = ["https://youtu.be/oKJ2o-eVv7Q", "https://youtu.be/nWoBalBUnxk", "https://youtu.be/sAAixJP8g0I",
                    "https://youtu.be/EAJdMUvYB2c", "https://youtu.be/JL6GESZia1s", "https://youtu.be/2OhAR2snIh4",
                    "https://youtu.be/OwWuVzGuv9s", "https://youtu.be/sorDRTuSj7Q", "https://youtu.be/Cp55JzksV0I"]
        await message.reply(random.choice(kr1_list))
    elif message.text == '2002':
        kr2_list = ["https://youtu.be/DHjwjlaGxRk", "https://youtu.be/e7t-L0tXzE0", "https://youtu.be/0_ipDmd4qFM",
                     "https://youtu.be/7XGR_TtvBBI", "https://youtu.be/cfKFS1Hitz8", "https://youtu.be/VRMqmt7enHU",
                     "https://youtu.be/qENZIpYXQZ0", "https://youtu.be/uEP-Bp_QE9Y", "https://youtu.be/ylKxcorx0rM",
                     "https://youtu.be/qtYB786KDpw"]
        await message.reply(random.choice(kr2_list))
    elif message.text == 'Главное меню':  # возвращает пользователя в главное меню
        await bot.send_message(message.from_user.id, 'Только что же там были...', reply_markup=nav.mainMenu)
    elif message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'Только что же там были...', reply_markup=nav.prikMenu)



bot.polling()
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
