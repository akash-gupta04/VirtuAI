import requests

def get_current_weather(city):
    api_key = 'API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if data['cod'] == '404':
        return None
    else:
        cloudiness = data['weather'][0]['description']
        temperature = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"\nThe weather in {city} is {cloudiness}. The temperature is {temperature}°C, and it feels like {feels_like}°C. The humidity is {humidity}%, and the wind speed is {wind_speed} m/s."

#print(get_current_weather("Jammu"))
