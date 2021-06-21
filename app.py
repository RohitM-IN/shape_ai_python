import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input('Enter city name:')

request_api = 'https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api_key
req = requests.get(request_api)

api_data = req.json()

temp_city = ((api_data['main']['temp']) - 273.15)

weather_desc = api_data['weather'][0]['description']
hmdty= api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S %p')

print("----------------------------------------")
print('warther stats for - {} || {}'.format(location.upper(), date_time))
print('----------------------------------------')

print('current temp is      : {:.2f} deg C'.format(temp_city))
print('current weather desc : ',weather_desc)
print('current Humidity     : ',hmdty,'%')
print('current Wind Speed   : ',wind_spd,' kmph')


