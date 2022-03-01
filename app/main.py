from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
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


def find_index_post(id):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i



def find_post(id):
    for p in my_post:
        if p['id'] == id:
            return p
            break

# async is optional
@app.get("/")
async def root():
    # To run the app use cmd -> uvicorn main:app --reload
    # After reformat of code -> uvicorn app.main:app --reload
    # main is from class name and app is from the veriable
    return {"message" : "Hello World!!!"}


@app.get("/posts")
def get_posts():
    return {"data": my_post}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
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



# 793146
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    print(id)
    post = find_post(id)
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} was not found"}
        # # or
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} was not found")
    return {"post_details": post}            


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # delete post
    # find the index in the array that has required ID
    index = find_index_post(id)
    print(index)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with ID:{id} does not exist")
    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    print(post)
    
    index = find_index_post(id)
    print(index)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Post with ID:{id} does not exist")
    
    post_dict = post.dict()
    # post_dict['id'] == id
    my_post[index] = post_dict
    return {"data": post_dict}