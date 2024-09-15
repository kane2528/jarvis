import requests

def get_weather(city):
    api_key = "2aad043edbd4c6d619b01adba5fe120c"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        description = weather["description"]
        return f"The weather in {city} is {description} with a temperature of {temperature}°C."
    else:
        return f"Could not retrieve weather data for {city}."

# Update your main code to use the real get_weather function
