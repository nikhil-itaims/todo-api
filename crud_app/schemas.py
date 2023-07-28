from typing import List, Union
from pydantic import BaseModel

class TodoBase(BaseModel):
    name: str
    description: str

class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: str

    class Config:
        from_attributes = True
