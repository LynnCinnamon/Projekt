

from data_sources.open_weather import OpenWeatherDataSource
from data_sources.static_html import StaticHtmlDataSource
from generators.open_weather_generator import OpenWeatherGenerator
from generators.static_html_generator import StaticHtmlGenerator


def main():
    data_source = OpenWeatherDataSource("fa46d8f79f8cadb23912b2574fba7a08", 51.35, 11.99)
    generator = OpenWeatherGenerator(data_source)
    
    print(generator.generate())

if __name__ == "__main__":
    main()