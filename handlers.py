from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from weather_api import get_weather
from database import log_request, add_subscription, get_user_subscription, remove_subscription

# /start
def start(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    message = "Привет! Я бот прогноза погоды.\n\nДоступные команды:\n" \
              "/weather <город> — узнать погоду\n" \
              "/subscribe <город> — получать погоду каждый день в 8 утра\n" \
              "/unsubscribe — отменить подписку"
    update.message.reply_text(message)
    log_request(user_id, '/start', message)

# /weather <город>
def weather(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if not context.args:
        msg = "❗ Укажите город. Пример: /weather Москва"
        update.message.reply_text(msg)
        log_request(user_id, '/weather', msg)
        return

    city = ' '.join(context.args)
    forecast = get_weather(city)
    update.message.reply_text(forecast)
    log_request(user_id, f'/weather {city}', forecast)

# /subscribe <город>
def subscribe(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if not context.args:
        msg = "❗ Укажите город для подписки. Пример: /subscribe Москва"
        update.message.reply_text(msg)
        log_request(user_id, '/subscribe', msg)
        return

    city = ' '.join(context.args)
    add_subscription(user_id, city)
    msg = f"✅ Вы подписались на ежедневную погоду по городу: {city}"
    update.message.reply_text(msg)
    log_request(user_id, f'/subscribe {city}', msg)

# /unsubscribe
def unsubscribe(update: Update, context: CallbackContext):
    user_id = update.effective_user.id

    if get_user_subscription(user_id):
        remove_subscription(user_id)
        msg = "❌ Подписка отменена."
    else:
        msg = "ℹ У вас нет активной подписки."

    update.message.reply_text(msg)
    log_request(user_id, '/unsubscribe', msg)
