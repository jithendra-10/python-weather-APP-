
import requests
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
API_KEY = "950fa7669aa2c70f8edb4a06fc38398f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return 
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["main"].lower()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        image_map = {
            "clear": "sun.png",
            "rain": "rain.png",
            "cloud": "cloud.png",
            "snow": "snow.png"
        }
        img_file = image_map.get(weather, "default.png")
        img_path = os.path.join(os.path.dirname(__file__), img_file) 
        if not os.path.exists(img_path):
            img_path = os.path.join(os.path.dirname(__file__), "default.png")
        try:
            weather_icon = Image.open(img_path).resize((200, 200))
            weather_icon = ImageTk.PhotoImage(weather_icon)
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")
            return
        result_label.config(
            text=f"🌍 {city.capitalize()}\n🌤️ {weather.capitalize()}\n🌡️ {temp}°C\n💧 {humidity}%"
        )
    else:
        messagebox.showerror("Error", "City not found!")
root = tk.Tk()
root.title("Weather App 🌦️")
root.geometry("350x400")
root.config(bg="#ADD8E6")
city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)
search_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
search_btn.pack()
icon_label = tk.Label(root, bg="#ADD8E6")
icon_label.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#ADD8E6")
result_label.pack(pady=20)
root.mainloop()
