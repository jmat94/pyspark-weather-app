# main.py
from pyspark_weather.weather_processing import create_spark_session, process_weather_data

if __name__ == "__main__":
    spark = create_spark_session()
    df = process_weather_data(spark)

    if df:
        # Save processed data as CSV
        df.write.csv("output/weather_data.csv", header=True)
