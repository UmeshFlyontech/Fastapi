from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data":{"Name":"Sudip"}}

@app.get("/about")
def about():
    return "About:"

@app.put("/update")
def info():
    return {"Update":"Update"}
