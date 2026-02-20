"""SQL database connector."""

class SQLConnector:
    """Connect to SQL databases."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
