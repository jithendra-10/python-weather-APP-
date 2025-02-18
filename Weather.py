import requests

API_KEY = "950fa7669aa2c70f8edb4a06fc38398f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}  # Fetch in Celsius
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        
        print(f"\n🌍 City: {city}")
        print(f"🌤️ Weather: {weather.capitalize()}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
    else:
        print("\n❌ City not found. Try again!")
city_name = input("\nEnter city name: ")
get_weather(city_name)
