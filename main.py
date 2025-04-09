import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

# Ваш токен и ссылка на канал
API_TOKEN = '7867522162:AAF3P_-a125ILYYM0FGwvMccFlSaTPRaeF0'
CHANNEL_LINK = 'https://t.me/clicktobetbot'

logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user
    username = user.username or "без username"
    print(f"🔔 Новый пользователь: {user.id} (@{username})")
    await message.answer(
        f"Привет, {user.first_name}!\n\n"
        f"Здесь публикую схемы, которые реально работают 💸\n"
        f"Подпишись на канал — всё там 👇",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton("Перейти в канал 📲", url=CHANNEL_LINK)
        )
    )

# Запуск бота
if __name__ == '__main__':
    dp.run_polling()
