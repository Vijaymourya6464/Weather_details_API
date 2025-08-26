import requests
import json
city = input("Enter your City Name: ")
# Construct the API URL with the city name and your API key
url = f"https://api.weatherapi.com/v1/current.json?key=d273b15b7ded4887b3281832252608&q={city}"
	
# Fetch weather details

r = requests.get(url)

  #data loading in json format

wdic = json.loads(r.text)
		
	# Extract useful  main details
    
location = wdic["location"]["name"]
country = wdic["location"]["country"]
temp_c = wdic["current"]["temp_c"]
condition = wdic["current"]["condition"]["text"]
humidity = wdic["current"]["humidity"]
wind_kph = wdic["current"]["wind_kph"]
		
# Display what you want to show

print(" --- Weather Report ---")
print(f"📍 Location: {location}, {country}")
print(f"🌡️ Temperature: {temp_c} °C")
print(f"☁️ Condition: {condition}")
print(f"💧 Humidity: {humidity}%")
print(f"💨 Wind Speed: {wind_kph} kph")


