from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Static Todo App")

class Todo(BaseModel):
    name: str
    desciption: str

todo_list = []

@app.get("/", description="This is main route of application.")
async def index():
    try:
        response = {
            "status": True, 
            "message": "Simple todo api using FastApi.",
            "error_message": None,
            "data": None
        }

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong.",
            "error_message": str(e),
            "data": None
        }

    return response

@app.get("/todo")
async def all_todo():
    try:
        response = {
            "status": True, 
            "message": "List of todos.",
            "error_message": None,
            "data": todo_list
        }

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

    return response

@app.get("/todo/{id}")
async def get_todo(id: int):
    try:
        data = todo_list[id]

        if data:
            response = {
                "status": True, 
                "message": "Todo data get successfully",
                "error_message": None,
                "data": data
            }
        
        else:
            response = {
                "status": True, 
                "message": "Todo data not found",
                "error_message": None,
                "data": data
            } 
            return response, 404

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

    return response

@app.post("/add-todo")
async def add_todo(todo: Todo):
    try:
        todo_list.append(todo)
        response = {
            "status": True, 
            "message": "Todo added successfully.",
            "error_message": None,
            "data": todo
        }

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

    return response

@app.put("/update-todo/{id}")
async def update_todo(id: int, todo: Todo):
    try:
        todo_list[id] = todo
        response = {
            "status": True, 
            "message": "Todo updated successfully.",
            "error_message": None,
            "data": todo
        }

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong.",
            "error_message": str(e),
            "data": None
        }

    return response

@app.delete("/delete-todo/{id}")
async def delete_todo(id: int):
    try:
        todo_list.pop(id)
        response = {
            "status": True, 
            "message": "Todo deleted successfully.",
            "error_message": None,
            "data": None
        }

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong.",
            "error_message": str(e),
            "data": None
        }

    return response
