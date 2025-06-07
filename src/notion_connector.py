import os
from typing import List, Dict, Any
from notion_client import Client

class NotionConnector:
    """Simple wrapper around the Notion API."""

    def __init__(self, token: str | None = None) -> None:
        self.token = token or os.getenv("NOTION_TOKEN")
        if not self.token:
            raise ValueError(
                "Notion API token must be provided via argument or NOTION_TOKEN env variable"
            )
        self.client = Client(auth=self.token)

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Perform a search across the workspace."""
        response = self.client.search(query=query)
        return response.get("results", [])

    def get_page_content(self, page_id: str) -> Dict[str, Any]:
        """Retrieve page JSON content."""
        return self.client.pages.retrieve(page_id)
