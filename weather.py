import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# Load environment variables
load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    city: str
    state: str
    main: str
    description: str
    icon: str
    temperature: int

def get_lat_lon(city_name, state_code, country_code="India", API_key=api_key):
    """
    Fetch latitude and longitude for a given city, state, and country.
    """
    try:
        resp = requests.get(
            f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}'
        ).json()
        if resp:
            data = resp[0]
            lat, lon = data.get('lat'), data.get('lon')
            return lat, lon
        else:
            raise ValueError("Location not found. Please check your inputs.")
    except Exception as e:
        print(f"Error fetching coordinates: {e}")
        return None, None

def get_current_weather(lat, lon, state_name, API_key=api_key):
    """
    Fetch current weather data using latitude and longitude.
    """
    try:
        resp = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric'
        ).json()
        if resp:
            data = WeatherData(
                city=resp.get('name'),
                state=state_name,  # State info isn't directly available in the API response
                main=resp.get('weather')[0].get('main'),
                description=resp.get('weather')[0].get('description'),
                icon=resp.get('weather')[0].get('icon'),
                temperature=int(resp.get('main').get('temp')),
            )
            return data
        else:
            raise ValueError("Weather data not available.")
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def main(city_name, state_name, country_name="India"):
    """
    Main function to fetch weather data for a given city and state in India.
    """
    lat, lon = get_lat_lon(city_name, state_name, country_name)
    if lat is not None and lon is not None:
        weather_data = get_current_weather(lat, lon, state_name)
        return weather_data
    else:
        return None

if __name__ == "__main__":
    # Test for Indian locations
    city = "Pune"
    state = "Maharashtra"
    weather = main(city, state)
    if weather:
        print(f"Weather in {city}, {state}:")
        print(f"Main: {weather.main}")
        print(f"Description: {weather.description}")
        print(f"Temperature: {weather.temperature}°C")
    else:
        print("Unable to fetch weather data.")
