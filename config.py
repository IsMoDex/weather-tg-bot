import os
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env файла

# Токен бота Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Используй имя переменной окружения

# Ключ API погоды (например, OpenWeatherMap)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")  # Используй имя переменной окружения

# URL API (OpenWeatherMap — бесплатный тариф)
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

# Путь к SQLite базе данных
DATABASE_PATH = "weather_bot.db"

# Время для утренней рассылки (UTC — с поправкой учитывать при планировании)
SCHEDULE_HOUR = 8
