
import requests
from datetime import datetime

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

spartanburg_id = "4597204"
spartanburg_url = f"http://api.openweathermap.org/data/2.5/weather?id={spartanburg_id}&APPID={api_key}&units=imperial"
resp = requests.get(spartanburg_url)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print(f"""
    The current weather in {weather_data["name"]} is: {weather_data["weather"][0]["description"]}
    Current temp (in Fahrenheit): {weather_data["main"]["temp"]}
    Temperature range: High: {weather_data["main"]["temp_max"]} Low: {weather_data["main"]["temp_min"]}
    Humidity: {weather_data["main"]["humidity"]}
    """)
else:
    print("ERROR: " + str(resp.status_code))

#Show 5 day forecast for vacation spot - Berlin

berlin_id = "6545310"
berlin_url_forecast = f"http://api.openweathermap.org/data/2.5/forecast?id={berlin_id}&APPID={api_key}&units=imperial"
resp = requests.get(berlin_url_forecast)

if resp.status_code in [200, 201]:
    weather_data = resp.json()
    print("The 5 day forecast for " + weather_data["city"]["name"] +  " is: ")
    for item in weather_data["list"]:
        dt_obj = datetime.strptime(item["dt_txt"], "%Y-%m-%d %H:%M:%S")
        if dt_obj.hour == 12:
            print(f"""
On {str(dt_obj.month)}, {str(dt_obj.day)} it will be {item["weather"][0]["description"]}
Temperature (in Fahrenheit): {item["main"]["temp"]}
Temp range: High: {item["main"]["temp_max"]} Low: {item["main"]["temp_min"]}
Humidity: {item["main"]["humidity"]}
            """)
            if item["weather"][0]["id"] >= 200 and item["weather"][0]["id"] < 600:
                print("You may want to bring an umbrella.")
            if item["main"]["temp"] > 70 and item["main"]["temp"] < 110:
                print("Break out the shorts!")
            elif item["main"]["temp"] < 70 and item["main"]["temp"] > 50:
                print("Jeans and maybe a light jacket.")
            elif item["main"]["temp"] < 50 and item["main"]["temp"] > 32:
                print("Definitely want a coat.")
            elif item["main"]["temp"] < 32:
                print("Bundle up, it's cold!")
            elif item["main"]["temp"] > 110:
                print("Wear SPF 1000!")
else:
    print("ERROR: " + str(resp.status_code))
