# Installation & Setup Guide

## Prerequisites

Ensure you have the following installed:

- Python 3.8+

## Installation Steps

1. **Clone the Repository**
   ```sh
   git clone <https://github.com/KRISNABADDE/text-sql-assistant.git>
   cd <text-sql-assistant>
   ```

3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Environment Variables**
   Create a `.env` file in the project root and add:
   ```env
   GROQ_API_KEY=<your-groq-api-key>
   ```
5. **Run the Application**
   ```sh
   uvicorn main:app
   ```
6. **Access the Application**
    - API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - Web UI: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

# Documentation

## How It Works

1. **User submits a natural language query** via the frontend.
2. **FastAPI routes the request** to `/query`, which processes the request.
3. **LLM converts the natural query to SQL** using Groq's API and the provided database schema.
4. **SQL query is streamed back** to the user for execution in the database.
5. **MemoryService stores the query history** for contextual improvements.

## Project Structure

```
project-root/
│-- app/
│   ├── routes/query.py         # API Route for text-to-SQL conversion
│   ├── models.py               # Pydantic models for request validation
│   ├── services/
│   │   ├── llm.py              # LLM interaction for SQL conversion
│   │   ├── con_memory.py       # Memory service for query history
│   ├── utils/utils.py          # Helper functions and DB schema
│-- templates/
│   ├── index.html              # Frontend template
│-- main.py                      # FastAPI application entry point
│-- requirements.txt             # Dependencies
│-- .env                         # API keys and environment variables
```

## Design Choices

- **FastAPI** for high-performance asynchronous APIs.
- **Streaming Response** to send SQL output in real-time.
- **MemoryService** to track past queries and improve responses.
- **Groq LLM API** for SQL conversion with context handling.
- **Jinja2 Templates** for web UI rendering.

## Limitations

- **LLM Dependency:** Requires a valid API key for Groq's LLM.
- **SQL Schema Sensitivity:** Performance depends on a well-defined `DB_SCHEMA`.
- **Limited Query Context:** Retains only the last few queries for better performance but may lose long-term context.

