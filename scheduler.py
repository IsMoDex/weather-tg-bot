from apscheduler.schedulers.background import BackgroundScheduler
from weather_api import get_weather
from database import get_all_subscriptions, log_request
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, SCHEDULE_HOUR
import pytz
import logging

bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Настроим логирование
logging.basicConfig(filename='scheduler.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def send_morning_forecasts():
    subscriptions = get_all_subscriptions()
    for user_id, city in subscriptions:
        forecast = get_weather(city)
        try:
            bot.send_message(chat_id=user_id, text=f"☀ Доброе утро!\n{forecast}")
            log_request(user_id, '[daily forecast]', forecast)
            logging.info(f"Прогноз отправлен пользователю {user_id} для города {city}.")
        except Exception as e:
            log_request(user_id, '[daily forecast]', f'Ошибка отправки: {str(e)}')
            logging.error(f"Ошибка при отправке пользователю {user_id} для города {city}: {str(e)}")

def setup_scheduler():
    scheduler = BackgroundScheduler(timezone=pytz.utc)  # Используем UTC, бот будет запускаться в 8:00 UTC
    scheduler.add_job(send_morning_forecasts, 'cron', hour=SCHEDULE_HOUR, minute=0)
    scheduler.start()
