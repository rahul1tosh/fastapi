from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

post: list[dict] = [
    {
        "name": "Rahul",
        "age": 23
    },
    {
        "name": "Sumit",
        "age": 25
    }
]

@app.get("/")
def main():
    return {"message":"Hello Rahul !!! "}

@app.get("/apis/post")
def get_json():
    return post

@app.get("/post", response_class=HTMLResponse, include_in_schema=False)
def html():
    return f"<h1>Hello Rahul!!!</h1> <h2>{post[0]}</h2>"