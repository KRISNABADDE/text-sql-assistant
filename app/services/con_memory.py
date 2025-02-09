from typing import List, Dict, Any


class MemoryService:

    def __init__(self) -> None:
        self.history: List[Dict[str, Any]] = []

    def add_query(self, user_query: str, sql_query: str) -> None:
        self.history.append({"user_query": user_query, "sql_query": sql_query})

    def get_recent_queries(self, n: int = 10) -> str:
        recent = self.history[-n:]
        return "\n".join(
            [f"User: {item['user_query']} -> SQL: {item['sql_query']}" for item in recent]
        )


memory = MemoryService()
