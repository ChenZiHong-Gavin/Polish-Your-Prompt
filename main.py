import uvicorn
from fastapi import FastAPI
from handlers import router

app = FastAPI()
app.include_router(router)


@app.get("/")
def welcome():
    return {"Polish Your Prompt": "Welcome!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
