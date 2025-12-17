from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class CoordIn(BaseModel):
    x: float
    y: float
    zoom: Optional[int] = None

class CoordOut(BaseModel):
    x: float
    y: float
    zoom: Optional[int] = None

#get
@app.get("/")
async def hello_world():
    return {"Hello": "World"}

@app.get("/component/{component_id}")
async def get_component(component_id: int):
    return {"component_id": component_id, " ": "active"}


@app.post("/position/{priority}")
async def make_location(priority: int, coord: CoordIn):
    return {"priority": priority, "New coordinates": coord}