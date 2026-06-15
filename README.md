Weather App

Description:

The Weather App is a Python-based command-line application that provides real-time weather information for any city using the OpenWeatherMap API.

The application allows users to enter a city name and displays the current temperature, humidity, and weather conditions.

Features:

Real-time weather information,
User-friendly Command Line Interface (CLI),
Temperature displayed in Celsius,
Humidity percentage display,
Weather condition display,
Invalid city name handling,
Network error handling using try-except.

Technologies Used:

Python 3,
Requests Library,
OpenWeatherMap API.

How It Works:

The user enters the name of a city.
The application sends a request to the OpenWeatherMap API.
The API returns weather data in JSON format.
The program extracts:
Temperature,
Humidity, and 
Weather Description
Temperature is converted from Kelvin to Celsius.
The weather information is displayed in a user-friendly format.
If the city name is invalid, an error message is shown.
If the API request fails, the application displays an appropriate error message.

Project Structure:

synent-task6-weatherapp-anvith
│

├── main.py

└── README.md

Sample Output

Enter city name: Bengaluru

----Weather Report----

City: Bengaluru

Temperature: 28.89°C

Humidity: 65%

Weather Description: overcast clouds

Output Screenshot:

weatherapp_output.png and weatherapp1_output.png

### Logic of Task6 Weather App

1. The program starts by importing the `requests` library, which is used to send HTTP requests to the weather API.

2. The user enters the name of a city.

```python
city = input("Enter city name: ")
```

3. The program creates a request URL using the city name and the OpenWeatherMap API key.

```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
```

4. A GET request is sent to the OpenWeatherMap server.

```python
response = requests.get(url)
```

5. The API returns weather information in JSON format, which is converted into a Python dictionary.

```python
data = response.json()
```

6. The program checks whether the API request was successful.

```python
if data["cod"] == 200:
```

7. If the city is found, the program extracts:

   * Temperature
   * Humidity
   * Weather Description

from the JSON response.

8. The temperature received from the API is in Kelvin, so it is converted to Celsius.

```python
temperature = main["temp"] - 273.15
```

9. The weather information is displayed to the user, including:

   * City Name
   * Temperature
   * Humidity
   * Weather Description

10. If the city name is invalid, the program displays:

```text
City not found.
```

11. Exception handling is implemented using:

```python
except Exception:
```

to handle network issues, API errors, or unexpected problems without crashing the program.

12. The application provides real-time weather information by fetching live data from the OpenWeatherMap API.

