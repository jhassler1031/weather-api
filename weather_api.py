
import requests

api_key = "3e61296365ff0da7ca77775d7fd89edb"
test_url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + api_key
resp = requests.get(test_url)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The weather in {} is {}.".format(weather_data['name'], weather_data['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
