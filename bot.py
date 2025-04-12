from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_BOT_TOKEN
from handlers import start, weather, subscribe, unsubscribe
from database import init_db
from scheduler import setup_scheduler

def main():
    # Инициализация БД
    init_db()

    # Запуск планировщика
    setup_scheduler()

    # Создаем и запускаем бота
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    # Регистрируем команды
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("unsubscribe", unsubscribe))

    # Стартуем
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
