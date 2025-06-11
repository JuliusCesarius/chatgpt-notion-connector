import os
from typing import List, Dict, Any

import openai


def search_with_chatgpt(
    query: str, pages: List[Dict[str, Any]], model: str = "gpt-3.5-turbo"
) -> str:
    """Use ChatGPT to perform semantic search over Notion page contents.

    Each page dict can contain ``title`` and optional ``content`` fields. The
    function sends the aggregated content to ChatGPT and asks it to determine
    which pages best answer the query.
    """

    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable must be set")

    formatted = []
    for p in pages:
        title = p.get("title", "Untitled")
        text = p.get("content", "")
        formatted.append(f"{title}:\n{text}")

    content = "\n\n".join(formatted)
    prompt = (
        "You are a helpful assistant that helps search Notion pages.\n"
        f"User query: {query}\n"
        "Page contents:\n" + content + "\n"
        "Return the titles of the most relevant pages."
    )

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]
