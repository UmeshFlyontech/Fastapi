from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get("/blog")
def index(limit: int=20, published: bool=True, sort: Optional[str]= None):
    if published:
        return {'Data': f'{limit} published blogs from the DB'}
    else:
        return {'Data': f'{limit} blogs from the DB'}

@app.get("/blog/unpublished")
def  unpublished():
    return {"Data": "All unpublished blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"Data":id}

@app.get("/blog/{id}/comment")
def comment(id, limit=10):
    return limit
    return {"Data":{'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
@app.post("/blog")
def create_blog(blog: Blog):
    return {"Data": f"Blog is created with title as {blog.title}"}


