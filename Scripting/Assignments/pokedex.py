import json
import requests

city = input("ENTER CITY NAME: ")

def get_weather(city):
    geo_enc_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json"

    response = requests.get(geo_enc_url)

    print(response)
    print(response.status_code)

    text = response.text
    #print(text)

    data = json.loads(text)
    #print(data)

    info = data["results"][0]
    #print(info)

    for i in data["results"]:
        print(i)
        
    lat = info["latitude"]
    long = info["longitude"]
    print(f"Latitude: {lat}, Longitude: {long}")
    print()

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code"
    weather_response = requests.get(weather_url)
    print(weather_response)
    print(weather_response.status_code)

    weather_data = json.loads(weather_response.text)
    print(weather_data)
    print(weather_data["current"])

    current = weather_data["current"]
    weather_code =  current["weather_code"]
    temperature = current["temperature_2m"]
    print(f"Temperature: {temperature}°C")
    print(weather_code)
    condition = ""
    
    if weather_code >= 0 and weather_code <= 3:
        condition = "clear"
    elif weather_code >= 45 and weather_code <= 48:
        condition = "fog"
    elif weather_code >= 51 and weather_code <= 57 or weather_code >= 61 and weather_code <= 67 or weather_code >= 80 and weather_code <= 82 or weather_code >= 95 and weather_code <= 99:
        condition = "rain"
    elif weather_code >= 71 and weather_code <= 77 or weather_code >= 85 and weather_code <= 86:
        condition = "snow"
    else:
        condition = "clear"
        
    diction = {"city":city, "condition" : condition, "temperature": temperature}
    print(diction)

get_weather(city)


