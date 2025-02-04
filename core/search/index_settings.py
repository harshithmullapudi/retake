from opensearchpy import OpenSearch
from typing import Dict, Any


class IndexSettings:
    def __init__(self, name: str, client: OpenSearch):
        self.name = name
        self.client = client

    def update(self, settings: Dict[str, Any]) -> None:
        # Close the index, update the settings, and reopen the index
        self.client.indices.close(index=self.name)
        self.client.indices.put_settings(index=self.name, body=settings)
        self.client.indices.open(index=self.name)
