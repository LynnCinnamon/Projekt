from data_sources.open_weather import OpenWeatherDataSource
from generators.html_generator_interface import HTMLGeneratorInterface


class OpenWeatherGenerator(HTMLGeneratorInterface):
    def __init__(self, data_source: OpenWeatherDataSource) -> None:
        super().__init__(data_source)
        assert isinstance(self.data_source, OpenWeatherDataSource), "data_source must be an instance of OpenWeatherDataSource"
        
    def generate(self):
        assert isinstance(self.data_source, OpenWeatherDataSource), "data_source must be an instance of OpenWeatherDataSource"
        data = self.data_source.get_data()
        return\
f"""
<div class="weather-widget">
    <p class="temp">Temperature: {round(data.temp)}°C</p>
    <p class="temp_range">Temperature Range: {round(data.min_temp)}°C - {round(data.max_temp)}°C</p>
    <p class="weather">Weather: {data.weather}</p>
    {f'<p class="rain">Rain: {data.rain}mm</p>' if data.rain > 0 else ''}
    {f'<p class="snow">Snow: {data.snow}mm</p>' if data.snow > 0 else ''}
</div>
"""
