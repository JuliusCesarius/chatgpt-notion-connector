from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .controllers.search_controller import SearchController

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

controller = SearchController()


@app.get("/search")
def search(query: str):
    """Search Notion using ChatGPT for ranking."""
    result = controller.search(query)
    return {"result": result}
