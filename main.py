import uvicorn
from fastapi import FastAPI, Request

from app.routes import query

app = FastAPI(title="TEXT TO SQL")

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")

app.include_router(query.router, tags=["Natural Language to SQL"])


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
