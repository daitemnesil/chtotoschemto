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
