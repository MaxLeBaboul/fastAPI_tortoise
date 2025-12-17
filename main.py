from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from models import Todo_Pydantic, TodoIn_Pydantic, Todo
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise



app = FastAPI()

class Messa(BaseModel):
    message: str

#get
@app.get("/")  
async def hello_world():
    return {"Hello": "World"}

#post
@app.post("/todo/", response_model=Todo_Pydantic)
async def create_todo(todo: TodoIn_Pydantic):
    obj = await Todo.create(**todo.dict(exclude_unset=True))

    return await Todo_Pydantic.from_tortoise_orm(obj)
   


register_tortoise(
    app,    
    db_url="sqlite://store.db",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)
