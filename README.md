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
