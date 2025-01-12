import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch Data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.json())
        return None

# Process Data
def process_weather_data(data):
    weather_list = data['list']
    df = pd.DataFrame({
        'Date': [item['dt_txt'] for item in weather_list],
        'Temperature': [item['main']['temp'] for item in weather_list],
        'Humidity': [item['main']['humidity'] for item in weather_list],
        'Wind Speed': [item['wind']['speed'] for item in weather_list],
    })
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Visualize Data
def visualize_weather_data(df):
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(3, 1, figsize=(10, 8))

    # Temperature over time
    sns.lineplot(ax=axes[0], x='Date', y='Temperature', data=df, color='b')
    axes[0].set_title("Temperature Over Time")
    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Temperature (°C)")

    # Humidity over time
    sns.lineplot(ax=axes[1], x='Date', y='Humidity', data=df, color='g')
    axes[1].set_title("Humidity Over Time")
    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Humidity (%)")

    # Wind Speed over time
    sns.lineplot(ax=axes[2], x='Date', y='Wind Speed', data=df, color='r')
    axes[2].set_title("Wind Speed Over Time")
    axes[2].set_xlabel("Date")
    axes[2].set_ylabel("Wind Speed (m/s)")

    plt.tight_layout()
    plt.show()

# Main Program
if __name__ == "__main__":
    # OpenWeatherMap API key
    API_KEY = "af1474082f146e318c465695af05f37c"
    city = "Mumbai"  # Desired city

    print("Fetching weather data...")
    data = fetch_weather_data(city, API_KEY)

    if data:
        print("Processing data...")
        df = process_weather_data(data)

        print("Visualizing data...")
        visualize_weather_data(df)
