import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/gem/{name}")
async def read_gem(name: str):
    return {"name": name}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
