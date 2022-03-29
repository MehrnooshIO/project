
from  fastapi import FastAPI
from uvicorn import run
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def root ():
  return {"message": "Hello World!"}


class User(BaseModel):
  username: str
  password: str
  email: str

  
@app.post("/signup")
def signup (user: User):
    return user




















if __name__ == "__main__":
 run(app, host="127.0.0.1", port=8000)
