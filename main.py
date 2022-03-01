from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_post = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
           {"title": "favorite food", "content": "I like pizza", "id": 2}
           ]

# async is optional
@app.get("/")
async def root():
    # To run the app use cmd -> uvicorn main:app --reload
    # main is from class name and app is from the veriable
    return {"message" : "Hello World!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.post("/posts")
def create_post(new_post: Post):
    # Extract all the fields from the body convert it into dictonary and save it in variable name payLoad.
    print(new_post)
    # Convert pydantic to dict
    print(new_post.dict())
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    return {"data": post_dict}
# title str, content str