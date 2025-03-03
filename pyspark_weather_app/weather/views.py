# from pyspark_weather.weather_processing import (
#     process_weather_data,
#     create_spark_session,
# )
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Weather
from .serializers import WeatherSerializer


# Create your views here.


@api_view(["GET"])
def weather_data(request):
    """Retrieve and return weather data in JSON format"""

    # Create spark session
    spark = pyspark_weather.weather_processing.create_spark_session()

    df = process_weather_data(spark)

    # Transform PySpark weather dataframe to Python dictionary
    weather_list = df.toPandas().to_dict(orient="records")

    return Response(weather_list)
