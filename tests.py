import main_bot_tg
import pytest
import unittest.mock


@pytest.mark.asyncio
async def test_start():
    bot = unittest.mock.Mock()
    message = unittest.mock.Mock()
    message.text = 'start'
    message.from_user.id = 3
    message.from_user.first_name = 'Vasia'
    await main_bot_tg.command_start(message)
    bot.send_message.assert_called_with(3, 'Hello Vasia')


@pytest.mark.asyncio
async def test_bot_message():
    bot = unittest.mock.Mock()
    message = unittest.mock.Mock()
    message.text = 'Какую оценку поставить?'
    await main_bot_tg.bot_message(message)
    bot.send_message.assert_called_with('Ставьте ' + str(random.randint(8, 10)))
    bot.send_message.assert_called_with(('Ставьте 8') or ('Ставьте 9') or ('Ставьте 10'))


@pytest.mark.asyncio
async def test_bot_message():
    bot = unittest.mock.Mock()
    message = unittest.mock.Mock()
    message.text = 'Погода'
    await main_bot_tg.command_start(message)
    bot.send_message.assert_called_with('Погода')
    bot.send_message.assert_called_with('Выберите город')
