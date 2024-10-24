from data_sources.data_source_interface import DataSourceInterface


class HTMLGeneratorInterface:
    def __init__(self, data_source: DataSourceInterface) -> None:
        self.data_source = data_source
        
    def set_data_source(self, data_source: DataSourceInterface) -> None:
        """
        Updates the data source for the HTML generator.

        Args:
            data_source (DataSourceInterface): The data source to be set.
        """
        self.data_source = data_source
    
    def generate(self):
        """
        Generate the output.

        This method should be implemented by subclasses to generate the desired output.
        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("The generate method must be implemented by a subclass.")