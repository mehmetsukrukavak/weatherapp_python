import requests

api_key = "333f3fca2f465d15ee72e98cda410262"
base_url = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"An error occurred: {e}")

city = input("Enter city name: ")
get_weather(city)
