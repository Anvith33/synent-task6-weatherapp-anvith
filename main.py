import requests

api_key = "50b8c808499b01a8a9a8121a21e08715"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

try:
    response = requests.get(url)

    data = response.json()
    if data["cod"] == 200:
        main = data["main"]
        temperature = main["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = main["humidity"]
        weather_description = data["weather"][0]["description"]

        print(f"\n----Weather Report----")
        print(f"City: {city}")
        print(f"Temperature: {temperature:.2f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather Description: {weather_description}")
    else:
        print("City not found.")
except Exception:
    print("Unable to fetch weather data.")
