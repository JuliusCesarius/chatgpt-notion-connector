from .notion_connector import NotionConnector
from .chatgpt_search import search_with_chatgpt


def main(query: str) -> None:
    notion = NotionConnector()
    pages = notion.search(query)

    # Format pages as simple dicts with title and id for demonstration
    formatted = []
    for page in pages:
        title = page.get('properties', {}).get('title', {}).get('title', [])
        title_text = title[0]['plain_text'] if title else 'Untitled'
        formatted.append({'id': page['id'], 'title': title_text})

    result = search_with_chatgpt(query, formatted)
    print(result)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python -m src.main '<query>'")
    else:
        main(sys.argv[1])
