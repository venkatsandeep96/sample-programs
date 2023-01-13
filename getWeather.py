# Get module required
import requests, json, sys

#if len(sys.argv) < 2:
 #   'Usage: getWeather.py location'

#location =  ' '.join(sys.argv[1:])


# Get the location from user
location = input('Enter the place: ')

# Get URL

URL = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=46f85d51153fa581b07a89913471bf2f'

# Open the URL

res = requests.get(URL)

print(res.raise_for_status())


#Convert the JSON data from API to Python

weatherData = json.loads(res.text)

# Parse and print the data

main = weatherData['weather'][0]['main']

temp = weatherData['main']['temp']

min_temp = weatherData['main']['temp_min']

max_temp = weatherData['main']['temp_max']

feel_like = weatherData['main']['feels_like']

humidity = weatherData['main']['humidity']

# printing

print('Todays weather in ', location)

print('Main weather is: ', main)

print('Temparature: ', int(temp - 273.15))
print('Minimum temp: ', int(min_temp -273.15))

print('Maximum temp: ', int(max_temp - 273.15))

print('Feels like: ', int(feel_like-273.15))

print('Humidity: ', humidity)
