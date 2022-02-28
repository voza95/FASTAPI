from fastapi import FastAPI

app = FastAPI()

# async is optional
@app.get("/")
async def root():
    # To run the app use cmd -> uvicorn main:app --reload
    # main is from class name and app is from the veriable
    return {"message" : "Hello World!!!"}
