from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data":{"Name":"Sudip"}}

@app.get("/blog/unpublished")
def  unpublished():
    return {"Data": "All unpublished blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"Data":id}

@app.get("/blog/{id}/comment")
def comment(id):
    return {"Data":{'1', '2'}}