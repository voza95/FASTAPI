from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

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
def create_post(payLoad: dict = Body(...)):
    # Extract all the fields from the body convert it into dictonary and save it in variable name payLoad.
    print(payLoad)
    return {"new_post": f"title {payLoad['title']}", "content": f"{payLoad['content']}"}