"""Microsoft Fabric connector."""

class FabricConnector:
    """Connect to Microsoft Fabric."""
    
    def __init__(self, workspace_id: str, capacity_id: str):
        self.workspace_id = workspace_id
        self.capacity_id = capacity_id
