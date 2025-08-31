import requests

# Base URL for OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name, api_key):
    try:
        # Prepare request
        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'  # Celsius
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # If city not found
        if response.status_code != 200:
            print("Error:", data.get("message", "Something went wrong"))
            return

        # Extract weather data
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Condition: {weather_desc.capitalize()}")

    except Exception as e:
        print("Error occurred:", e)


if __name__ == "__main__":
    api_key = "34d7892e218ad6071eeb5e3b5a34dd5a"  # 🔑 Replace this with your key
    city = input("Enter city name: ")
    get_weather(city, api_key)
