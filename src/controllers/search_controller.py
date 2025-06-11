from ..models.notion_connector import NotionConnector
from ..chatgpt_search import search_with_chatgpt


class SearchController:
    """Controller that coordinates Notion and ChatGPT searches."""

    def __init__(self, notion_token: str | None = None) -> None:
        self.notion = NotionConnector(notion_token)

    def search(self, query: str) -> str:
        pages = self.notion.search(query)
        formatted = []
        for page in pages:
            props = page.get("properties", {}).get("title", {})
            title_data = props.get("title", [])
            title = title_data[0]["plain_text"] if title_data else "Untitled"
            content = self.notion.get_page_text(page["id"])
            formatted.append(
                {
                    "id": page["id"],
                    "title": title,
                    "content": content,
                }
            )
        return search_with_chatgpt(query, formatted)
