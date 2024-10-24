
from data_sources.data_source_interface import DataSourceInterface


class StaticHtmlDataSource(DataSourceInterface):
    """
    StaticHtml is a class that implements the DataSourceInterface to read static HTML content from a specified file.
    NOTE: This assumes all the HTML content is stored in a single file. If the content is spread across multiple files, this class would need to be modified accordingly.
    Attributes:
        file_path (str): The path to the file containing the static HTML content.
    Methods:
        get_data() -> str:
            Reads the content of the file specified by the instance's file_path attribute and returns it as a string.
    """
    def __init__(self, file_path:str) -> None:
        super().__init__()
        self.file_path = file_path
        
    def get_data(self) -> str:
        """
        Reads the content of a file specified by the instance's file_path attribute.

        Returns:
            str: The content of the file as a string.
        """
        with open(self.file_path, 'r', encoding="utf-8") as file:
            return file.read()