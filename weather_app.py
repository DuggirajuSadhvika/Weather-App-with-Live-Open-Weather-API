
import requests

API_KEY = "1ec9aae2ce4b4d08e21e09b5e1bf599c"

URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(URL, params=params, timeout=10)
    data = response.json()

    if response.status_code == 200:
        print("\n===== WEATHER REPORT =====")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("==========================")

    else:
        print("Error:", data.get("message", "Unknown error"))

except requests.exceptions.RequestException as e:
    print("Network Error:", e)

# ===== 5 DAY WEATHER FORECAST =====

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

forecast_response = requests.get(
    FORECAST_URL,
    params=params,
    timeout=10
)

forecast_data = forecast_response.json()

if forecast_response.status_code == 200:

    print("\n===== 5 DAY WEATHER FORECAST =====")

    for item in forecast_data["list"]:

        date_time = item["dt_txt"]
        temperature = item["main"]["temp"]
        weather = item["weather"][0]["description"]

        if "12:00:00" in date_time:
            print("\nDate:", date_time)
            print("Temperature:", temperature, "°C")
            print("Weather:", weather)

else:
    print("Forecast Error:", forecast_data.get("message"))
