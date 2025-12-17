from fastapi import FastAPI, HTTPException, Form
from typing import Optional
from pydantic import BaseModel


app = FastAPI(title='TODO API', version='v1')

class Todo(BaseModel):
    name: str
    due_date: str
    description: Optional[str]
    
store_todo= []

@app.get("/")
async def home():
    return {"message": "Welcome to the TODO API"}

@app.get("/todo/{id}")
async def get_todo(id: int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="TODO item not found")
    
@app.get("/todo/", response_model=list[Todo])
async def get_all_todos():
    return store_todo

@app.post("/todo/")
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo 



@app.put("/todo/{id}")
async def update_todo(id: int, new_todo: Optional[Todo]):
    try:
        store_todo[id] = new_todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail="TODO item not found")
    
@app.delete("/todo/{id}")
async def delete_todo(id: int):
    try:
        deleted_todo = store_todo.pop(id)
        return {"message": "TODO item deleted", "item": deleted_todo}
    except IndexError:
        raise HTTPException(status_code=404, detail="TODO item not found")