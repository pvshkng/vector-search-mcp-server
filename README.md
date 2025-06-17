# Vector Search MCP Server
A FastMCP server integrated with Milvus Cloud and Google's Gemini embeddings.

## Prerequisites
- Python >= 3.11
- uv (install using pip install uv or https://docs.astral.sh/uv/)
- Milvus Cloud account (Create Milvus instance and get API key from https://zilliz.com/cloud)
- Google AI API key (https://aistudio.google.com/apikey)

## Project Structure
~~~
. 
├── app/ 
│ ├── config/         # Configuration and environment settings 
│ ├── core/           # Core functionality (embeddings, vector store) 
│ └── main.py         # MCP server entry point 
├── pyproject.toml    # Project dependencies 
└── .env              # Environment variables (copy from .env.example)
~~~

## Running the Project
1. Install prereqisites
2. Run ```uv venv``` to create a virtual environment
3. Run ```./.venv/Scripts/activate``` (Windows) or ```source ./.venv/bin/activate``` (MacOS) to activate the virtual environment
4. Run ```uv sync``` to install dependencies
5. Run ```cp .env.example .env``` and follow the instruction inside to get the required variables
6. Run ```fastmcp run --transport sse --port 8001 app/main.py``` to start the MCP server
7. (Optional) run ```fastmcp dev ./app/main.py``` to start the MCP Inspector for debug

## Running with Docker
1. Build the image: ```docker build -t llm-client-backend .```
2. Run: ```docker run -p 8000:8000 --env-file .env llm-client-backend```

## Other commands
- Exporting requirements.txt for deploying on the environment where uv is unavailable: ```uv pip freeze > requirements.txt```
