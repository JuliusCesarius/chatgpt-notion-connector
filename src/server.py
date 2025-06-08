from fastapi import FastAPI
from .controllers.search_controller import SearchController

app = FastAPI()
controller = SearchController()


@app.get("/search")
def search(query: str):
    """Search Notion using ChatGPT for ranking."""
    result = controller.search(query)
    return {"result": result}
