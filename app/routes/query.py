from fastapi import APIRouter
from starlette.responses import StreamingResponse

from app.models import QueryRequest
from app.services.llm_service import convert_to_sql

router = APIRouter()


@router.post("/query", response_class=StreamingResponse)
async def get_sql(query: QueryRequest):
    if not query.natural_query.strip():
        return StreamingResponse('PLEASE INTER QUERY')
    return StreamingResponse(convert_to_sql(query.natural_query), media_type="text/plain")
