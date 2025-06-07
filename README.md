# ChatGPT Notion Connector

This repository contains a minimal boilerplate for integrating the Notion API with OpenAI's ChatGPT API. The example code demonstrates how to search a Notion workspace and use ChatGPT to select relevant pages based on a natural language query.

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set the required environment variables:

- `NOTION_TOKEN` – Notion integration token.
- `OPENAI_API_KEY` – OpenAI API key.

You can export them in your shell or create a `.env` file and load it before running the script.

## Usage

Run a search query against your connected Notion workspace:

```bash
python -m src.main "<your search query>"
```

The script performs a basic Notion search and then asks ChatGPT to pick the most relevant pages from the results.

This project is only a starting point and does not provide advanced search features or error handling. Use it as a foundation for building a more complete connector.
