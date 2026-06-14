import requests

api_key = "50b8c808499b01a8a9a8121a21e08715"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

print(response.status_code)
print(response.json())