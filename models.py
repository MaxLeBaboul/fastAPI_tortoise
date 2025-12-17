from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
from typing import Type

class Todo(Model):
    id = fields.IntField(pk=True)
    todo = fields.CharField(max_length=250)
    due_date = fields.CharField(max_length=250)

    class PydanticMeta:
        pass

Todo_Pydantic: Type[BaseModel] = pydantic_model_creator(Todo, name="Todo")
TodoIn_Pydantic: Type[BaseModel] = pydantic_model_creator(Todo, name="TodoIn", exclude_readonly=True)
