# ChatGPT Notion Connector

This repository contains a minimal boilerplate for integrating the Notion API with OpenAI's ChatGPT API. The example code demonstrates how to search a Notion workspace and use ChatGPT to select relevant pages based on a natural language query.

## Installation

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd chatgpt-notion-connector
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Notion integration**

   - Visit [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and create a new integration.
   - Copy the generated internal integration token.
   - Share the pages or databases you want to search with this integration so it has access.

4. **Set environment variables**

   The connector expects the following variables:

   - `NOTION_TOKEN` – the integration token you created above.
   - `OPENAI_API_KEY` – your OpenAI API key.

   You can export them in your shell or place them in a `.env` file and load it before running the script.

## Usage

Run a search query against your connected Notion workspace:

```bash
python -m src.main "<your search query>"
```

The script performs a basic Notion search and then asks ChatGPT to pick the most relevant pages from the results. This project is only a starting point and does not provide advanced search features or error handling. Use it as a foundation for building a more complete connector.
