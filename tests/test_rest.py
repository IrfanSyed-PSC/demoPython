

import logging
from core.api.weather import WeatherApi

# constants
zip_code = '01803'

weather = WeatherApi()
    

def test_get_weather():

    response = weather.get_weather_byzip(zip_code)
    
    assert response['location']['name'] == 'Burlington'

def test_forecast_weather():
    forecast_by_days = 3
    response = weather.forecast_weather(forecast_by_days,zip_code)
    assert len(response['forecast']['forecastday']) == forecast_by_days

    ## assert that the forecastday has the object day with value maxtemp_c
    for day in response['forecast']['forecastday']:
        assert 'day' in day
        assert 'maxtemp_c' in day['day']
        assert day['day']['maxtemp_c'] > 0
