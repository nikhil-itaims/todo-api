from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI(title="Static Todo App")

class Todo(BaseModel):
    name: str
    description: str

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
        
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.get("/todo/{id}")
async def get_todo(id: int):
    try:
        data = todo_list[id]

        response = {
            "status": True, 
            "message": "Todo data get successfully",
            "error_message": None,
            "data": data
        }

        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": True, 
            "message": "Todo data not found",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.post("/todo")
async def add_todo(todo: Todo):
    try:
        todo_list.append(todo)

        response = {
            "status": True, 
            "message": "Todo added successfully.",
            "error_message": None,
            "data": todo
        }

        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }
        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

@app.put("/todo/{id}")
async def update_todo(id: int, todo: Todo):
    try:
        todo_list[id] = todo
        response = {
            "status": True, 
            "message": "Todo updated successfully.",
            "error_message": None,
            "data": todo
        }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong.",
            "error_message": str(e),
            "data": None
        }
        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.delete("/todo/{id}")
async def delete_todo(id: int):
    try:
        todo_list.pop(id)
        response = {
            "status": True, 
            "message": "Todo deleted successfully.",
            "error_message": None,
            "data": None
        }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": True, 
            "message": "Something went wrong.",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
