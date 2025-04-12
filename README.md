# 🌤 Weather Telegram Bot

Телеграм-бот, который предоставляет актуальную информацию о погоде и позволяет подписаться на ежедневные прогнозы.

## 🚀 Возможности

- Получение текущей погоды по команде `/weather`
- Подписка на ежедневную рассылку прогноза погоды в 08:00 по Москве
- Управление подпиской через команды `/subscribe` и `/unsubscribe`

## 📦 Стек технологий

- Python 3.10+
- [python-telegram-bot==13.15](https://github.com/python-telegram-bot/python-telegram-bot)
- APScheduler
- SQLite
- OpenWeatherMap API

## ⚙️ Установка и запуск

1. **Клонируй репозиторий**

```bash
git clone https://github.com/IsMoDex/weather-tg-bot.git
cd weather-tg-bot
```

2. **Создай виртуальное окружение**

```bash
python -m venv .venv
source .venv/bin/activate      # для Linux/macOS
.venv\Scripts\activate         # для Windows
```

3. **Установи зависимости**

```bash
pip install -r requirements.txt
```

4. **Создай `.env` файл и добавь токены**

```env
TELEGRAM_BOT_TOKEN=your_telegram_token
WEATHER_API_KEY=your_openweathermap_api_key
```

5. **Запусти бота**

```bash
python bot.py
```

## 🗂 Структура проекта

```
.
├── bot.py                  # Основной запуск бота
├── config.py               # Конфигурация и переменные окружения
├── scheduler.py            # Ежедневные задачи
├── weather_api.py          # Работа с OpenWeatherMap API
├── handlers.py             # Обработчики команд бота
├── database.py             # Работа с SQLite
├── requirements.txt        # Зависимости проекта
├── .env                    # Секреты (НЕ коммитить!)
└── .gitignore
```