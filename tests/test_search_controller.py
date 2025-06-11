import os
from unittest.mock import patch

import pytest

from src.controllers.search_controller import SearchController


@pytest.fixture
def controller():
    return SearchController(notion_token="dummy")


def test_search_returns_chatgpt_result(controller):
    pages = [
        {
            "id": "123",
            "properties": {"title": {"title": [{"plain_text": "Page"}]}},
        }
    ]
    with patch.object(controller.notion, "search", return_value=pages):
        with patch.object(
            controller.notion, "get_page_text", return_value="hello world"
        ):
            with patch("openai.ChatCompletion.create") as mock_create:
                with patch.dict(os.environ, {"OPENAI_API_KEY": "x"}):
                    mock_create.return_value = {
                        "choices": [{"message": {"content": "result"}}]
                    }
                    result = controller.search("hi")
                    assert result == "result"
