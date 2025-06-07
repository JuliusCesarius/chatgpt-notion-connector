import os
from typing import List, Dict, Any

import openai


def search_with_chatgpt(query: str, pages: List[Dict[str, Any]], model: str = "gpt-3.5-turbo") -> str:
    """Use ChatGPT to perform semantic search over Notion page contents.

    This is a simple implementation that feeds the list of page titles to the
    model and asks it to select the most relevant ones.
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY environment variable must be set")

    content = "\n".join(page.get("title", "") for page in pages)
    prompt = (
        "You are a helpful assistant that helps search Notion pages.\n"
        f"User query: {query}\n"
        "Available pages:\n" + content + "\n"
        "Return the titles of the most relevant pages."
    )

    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["choices"][0]["message"]["content"]
