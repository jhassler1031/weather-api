
import requests

#Default - shows for Moscow

api_key = "3e61296365ff0da7ca77775d7fd89edb"
"""
test_url = 'http://api.openweathermap.org/data/2.5/weather?id=524901&APPID=' + api_key
resp = requests.get(test_url)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The weather in {} is {}.".format(weather_data['name'], weather_data['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
"""
#Show current weather for hometown - Spartanburg
"""
spartanburg_id = "4597204"
spartanburg_url = f"http://api.openweathermap.org/data/2.5/weather?id={spartanburg_id}&APPID={api_key}"
resp = requests.get(spartanburg_url)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The weather in {} is {}.".format(weather_data['name'], weather_data['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
"""
#Show 5 day forecast for vacation spot - Berlin

berlin_id = "6545310"
berlin_url_forecast = f"http://api.openweathermap.org/data/2.5/forecast?id={berlin_id}&APPID={api_key}"
resp = requests.get(berlin_url_forecast)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The 5 day forecast for " + weather_data["city"]["name"] +  " is: ")
    for item in weather_data["list"]:
        print(item)
        print("On " + item["dt_txt"] + ": it will be " + item["weather"][0]["description"])
    #print("The weather in {} is {}.".format(weather_data['city']['name'], weather_data['weather'][0]['description']))
else:
    print("ERROR: " + str(resp.status_code))
