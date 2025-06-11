# ChatGPT Notion Connector

This repository contains a minimal boilerplate for integrating the Notion API with OpenAI's ChatGPT API. The example code demonstrates how to search a Notion workspace and use ChatGPT to select relevant pages based on a natural language query. It now fetches full page contents to enable a deeper semantic search.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set the required environment variables:

- `NOTION_TOKEN` – Notion integration token.
- `OPENAI_API_KEY` – OpenAI API key.

You can export them in your shell or create a `.env` file and load it before running the script.

For development, run the unit tests with:

```bash
pytest
```

## Usage

Run a search query against your connected Notion workspace from the command line:

```bash
python -m src.main "<your search query>"
```

The script performs a basic Notion search, downloads the text of each returned page, and then asks ChatGPT to pick the most relevant pages based on their full content.

This project is only a starting point and does not provide advanced search features or error handling. Use it as a foundation for building a more complete connector.

## Server

A basic FastAPI application is available in `src/server.py`. Start it with:

```bash
uvicorn src.server:app --reload
```

The repository also contains a small HTML client in the `web` directory. You can
host this folder with GitHub Pages and set the form's fetch URL to your deployed
API server.
The server enables CORS so the client can access it from another domain.
