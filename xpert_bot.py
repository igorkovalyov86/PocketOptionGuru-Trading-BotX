import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

# Загрузка токена из .env файла
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

# Проверка на случай, если переменная не найдена
if not API_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")

# Функция /start
def start(update, context):
    update.message.reply_text("Привет! Это PocketOptionGuru_Tradingbot. Я работаю!")

# Основной запуск
if __name__ == '__main__':
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("Бот запущен как PocketOptionGuru_Tradingbot...")
    updater.idle()
