import requests
from config import WEATHER_API_KEY, WEATHER_API_URL

def get_weather(city: str) -> str:
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }

    try:
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data['name']
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']

        forecast = f"📍 {city_name}\n🌡 Температура: {temp}°C\n🌥 Погода: {weather_desc}\n💨 Ветер: {wind_speed} м/с"
        return forecast

    except requests.RequestException:
        return "⚠ Не удалось получить данные. Попробуйте позже."
    except KeyError:
        return "❌ Город не найден. Проверьте правильность названия."
