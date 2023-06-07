import requests


def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change the units to imperial for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
    else:
        print("Failed to fetch weather information.")


def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter a city name: ")
    get_weather(api_key, city)


if __name__ == "__main__":
    main()
