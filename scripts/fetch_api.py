import requests
import pandas as pd

def load_pop(path: str) -> pd.DataFrame:
    """Loads the demographic dataset."""
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip()
    return df.head(50)

def fetch_weather_data(data: pd.DataFrame) -> pd.DataFrame:
    """Featching Weather Data."""

    weather_data = []

    for _, row in data.iterrows():
        city = row["City"]
        latitude = row["Latitude"]
        longitude = row["Longitude"]

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

        try:
            response = requests.get(url, timeout=40)

            if response.status_code == 200:
                    current = response.json().get("current_weather", {})
                    weather_data.append({
                        "City": city,
                        "Temperature": current.get("temperature"),
                        "Windspeed": current.get("windspeed")
                    })
            else:
                print(f"API returned {response.status_code} for {city}")

        except requests.RequestException as e:
            print(f"Could not get weather for {city}): {e}")

    return pd.DataFrame(weather_data)