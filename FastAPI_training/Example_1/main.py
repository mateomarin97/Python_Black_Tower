from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Blog(BaseModel):
    title: str
    content: str
    published: Optional[bool] = True

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"About": "This is a sample FastAPI application."}

@app.get("/blog")
def read_blog_list(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"Blogs": f"List of {limit} published blog posts."}
    return {"Blogs": f"List of {limit} unpublished blog posts."}

@app.get("/blog/unpublished")
def read_unpublished_blogs():
    return {"Unpublished Blogs": ["Blog Post 1", "Blog Post 2"]}

@app.get("/blog/{blog_id}")
def read_blog(blog_id: int):
    return {"Blog ID": blog_id, "Title": f"Blog Post {blog_id}"}

@app.post("/blog")
def create_blog(blog: Blog):
    return {"Message": "Blog created", "Title": blog.title, "Content": blog.content}

#With this line, ypu can lunch the API with python main.py
#and you can choose the port and host.
#But I prefer to use uvicorn main:app --reload in the terminal.
#if __name__ == "__main__":
    #uvicorn.run(app, host="127.0.0.1", port=8000)