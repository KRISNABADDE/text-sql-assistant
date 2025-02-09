from pydantic import BaseModel


class QueryRequest(BaseModel):
    natural_query: str
