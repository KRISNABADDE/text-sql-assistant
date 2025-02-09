import os

from dotenv import load_dotenv
from groq import Groq

from app.services.con_memory import memory
from app.utils.utils import DB_SCHEMA

load_dotenv()

GROQ_API_KEY = os.getenv('GROQ_API_KEY')


async def convert_to_sql(natural_query: str):
    messages = [{"role": "system", "content": "You are an AI SQL assistant."}, {
        "role": "system",
        "content": f"""Here is the database schema:\n{DB_SCHEMA}.
                   Just give me a SQL query.
                   If User asked out of context query that time give him/her answer as ask sql related queries..."""
    }]
    for record in memory.history:
        messages.append({"role": "user", "content": record["user_query"]})
        messages.append({"role": "assistant", "content": record["sql_query"]})

    messages.append({"role": "user", "content": natural_query})

    client = Groq(
        api_key=GROQ_API_KEY
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        stream=True

    )
    full_response = ""
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            full_response += content
            yield content
    memory.add_query(natural_query, full_response)
