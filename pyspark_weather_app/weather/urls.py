from django.urls import path
from .views import weather_data

urlpatterns = [
    path("api/weather/", weather_data, name="weather_data"),
]
