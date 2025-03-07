from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from pyspark_weather_app import urls


import requests
from .config import OPENAPI_KEY, BASE_URL, CITIES


def fetch_weather_data_of_city(city):
    params = {"q": city, "appid": OPENAPI_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}")
        return None


def create_spark_session():
    return SparkSession.builder.appName("WeatherDataProcessing").getOrCreate()


def get_weather_data():
    """Fetch weather data for multiple cities and normalize data types."""
    raw_data = []

    for city in CITIES:
        data = fetch_weather_data_of_city(city)
        if data:
            # Normalize data types (convert integers to floats where needed)
            processed_data = {
                "city": data["name"],
                "temperature": float(data["main"]["temp"]),  # Convert to float
                "humidity": float(data["main"]["humidity"]),  # Convert to float
                "wind_speed": float(data["wind"]["speed"]),  # Convert to float
                "description": data["weather"][0]["description"],
            }
            raw_data.append(processed_data)

    return raw_data


def process_weather_data(spark):
    raw_data = get_weather_data()

    if not raw_data:
        print("Data not available")
        return None

    df = spark.createDataFrame(raw_data)

    # Select relevant fields
    df = df.select(
        col("city").alias("city"),
        col("temperature").alias("temperature"),
        col("humidity").alias("humidity"),
        col("wind_speed").alias("wind_speed"),
        col("description").alias("description"),
    )

    df.show()
    return df


if __name__ == "__main__":
    spark = create_spark_session()
    process_weather_data(spark)
