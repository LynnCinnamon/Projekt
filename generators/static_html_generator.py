
from data_sources.static_html import StaticHtmlDataSource
from generators.html_generator_interface import HTMLGeneratorInterface


class StaticHtmlGenerator(HTMLGeneratorInterface):
    """
    StaticHtmlGenerator is a class that generates static HTML content from a given data source.
    Attributes:
        data_source (StaticHtml): The data source from which the static HTML content is generated.
    Methods:
        generate():
            Generates and returns data from the data source.
    """
    def __init__(self, data_source: StaticHtmlDataSource):
        super().__init__(data_source)
        assert isinstance(self.data_source, StaticHtmlDataSource), "Data source is not a StaticHtml instance."
        
    def generate(self):
        """
        Generates and returns data from the data source.
        
        We can safely just pass it on, as it is assumed to be a static HTML data source.

        Returns:
            Any: The data retrieved from the data source.
        """
        assert isinstance(self.data_source, StaticHtmlDataSource), "Data source is not a StaticHtml instance."
        data = self.data_source.get_data()
        return data