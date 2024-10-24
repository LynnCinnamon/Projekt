class DataSourceInterface:
    """
    DataSourceInterface is an abstract base class that defines a standard interface for data source retrieval.
    Methods:
        get_data(self):
            Abstract method to retrieve data from a data source. This method should be implemented by subclasses to define the specific logic for fetching data from the respective data source.
    """
    def get_data(self):
        """
        Abstract method to retrieve data from a data source.

        This method should be implemented by subclasses to define the specific
        logic for fetching data from the respective data source.

        Raises:
            NotImplementedError: If the method is not implemented by a subclass.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")