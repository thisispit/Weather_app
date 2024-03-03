import datetime as dt
import requests

user_input = input("Enter City: ")

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = open('api_key','r').read()
city = user_input

url = base_url + "&q=" + city + "&units=metric&APPID=" + api_key 


weather_data = requests.get(url)


if weather_data.json()['cod'] == '404':
    print("No city found")

else:

    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    ftemp = weather_data.json()['main']['feels_like']
    min = weather_data.json()['main']['temp_min']
    max = weather_data.json()['main']['temp_max']
    hum = weather_data.json()['main']['humidity']
    sunrise_timestamp = weather_data.json()['sys']['sunrise'] + weather_data.json()['timezone']
    sunset_timestamp = weather_data.json()['sys']['sunset'] + weather_data.json()['timezone']

    sunrise_utc = dt.datetime.fromtimestamp(sunrise_timestamp, tz=dt.timezone.utc)
    sunset_utc = dt.datetime.fromtimestamp(sunset_timestamp, tz=dt.timezone.utc)

    # sunrise = dt.datetime.utcfromtimestamp(weather_data.json()['sys']['sunrise'] + weather_data.json()['timezone'])
    # sunset = dt.datetime.utcfromtimestamp(weather_data.json()['sys']['sunset'] + weather_data.json()['timezone'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°C")
    print(f"Feels like {ftemp}°C")
    print(f"minimun temperature: {min}°C\nmaximun temperature: {max}°C")
    print(f"Humidity: {hum}%")
    print(f"Sunrise at {sunrise_utc} local time\nSunset at {sunset_utc} local time")


#print(weather_data.json())  to get json file