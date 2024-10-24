from dataclasses import dataclass
import requests
from data_sources.data_source_interface import DataSourceInterface


@dataclass
class OpenWeatherData:
    temp: float
    weather: str
    min_temp: float
    max_temp: float
    rain: float
    snow: float

class OpenWeatherDataSource(DataSourceInterface):
    def __init__(self, api_key:str, lat:float, lon:float) -> None:
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        
    def get_data(self) -> OpenWeatherData:
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.api_key}&units=metric'
        data = requests.get(url, timeout=2.0).json()
        return OpenWeatherData(
            temp=data['main']['temp'],
            weather=data['weather'][0]['description'],
            min_temp=data['main']['temp_min'],
            max_temp=data['main']['temp_max'],
            rain=data['rain']["1h"] if 'rain' in data else 0.0,
            snow=data['snow']["1h"] if 'snow' in data else 0.0,
        )
            