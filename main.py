from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# async is optional
@app.get("/")
async def root():
    # To run the app use cmd -> uvicorn main:app --reload
    # main is from class name and app is from the veriable
    return {"message" : "Hello World!!!"}


@app.get("/post")
def get_posts():
    return {"data":"This your post"}

@app.post("/createpost")
def create_post(new_post: Post):
    # Extract all the fields from the body convert it into dictonary and save it in variable name payLoad.
    print(new_post)
    # Convert pydantic to dict
    print(new_post.dict())
    return {"data":new_post.content}
# title str, content str