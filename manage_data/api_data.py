from data_sources.open_weather import OpenWeatherDataSource
from generators.open_weather_generator import OpenWeatherGenerator

class weather_api_data:
    def data():
        weather_data = OpenWeatherGenerator(OpenWeatherDataSource("fa46d8f79f8cadb23912b2574fba7a08", 51.35, 11.99))
        return weather_data.generate()
        