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

    def get_block_children(self, block_id: str) -> List[Dict[str, Any]]:
        """Return all children blocks of a block, handling pagination."""
        response = self.client.blocks.children.list(block_id=block_id)
        children = response.get("results", [])
        while response.get("has_more"):
            response = self.client.blocks.children.list(
                block_id=block_id, start_cursor=response.get("next_cursor")
            )
            children.extend(response.get("results", []))
        return children

    def _extract_text(self, block: Dict[str, Any]) -> str:
        """Extract plain text from a Notion block."""
        data = block.get(block.get("type", ""), {})
        rich = data.get("text") or data.get("rich_text") or []
        return "".join(t.get("plain_text", "") for t in rich)

    def get_page_text(self, page_id: str) -> str:
        """Recursively fetch all text content from a page."""

        def _collect(block_id: str) -> List[Dict[str, Any]]:
            blocks = self.get_block_children(block_id)
            all_blocks = []
            for b in blocks:
                all_blocks.append(b)
                if b.get("has_children"):
                    all_blocks.extend(_collect(b["id"]))
            return all_blocks

        blocks = _collect(page_id)
        lines = [self._extract_text(b) for b in blocks]
        return "\n".join(l for l in lines if l)
