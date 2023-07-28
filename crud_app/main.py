from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from crud_app import crud, models, schemas
from crud_app.database import SessionLocal, engine
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/todo/", response_model=List[schemas.Todo])
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        todos = crud.get_todos(db, skip=skip, limit=limit)
        response = {
            "status": True, 
            "message": "List of todos.",
            "error_message": None,
            "data": todos
        }
        
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": False, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.post("/todo/", response_model=schemas.Todo)
def create_user(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    try:
        todo_data = crud.create_todo(db=db, todo=todo)
        response = {
            "status": True, 
            "message": "Todo added successfully.",
            "error_message": None,
            "data": todo_data
        }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": False, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

@app.get("/todo/{id}", response_model=schemas.Todo)
def read_todo(id: int, db: Session = Depends(get_db)):
    try:
        todo = crud.get_todo(db, todo_id=id)
        if todo is None:
            response = {
                "status": True, 
                "message": "Todo not found.",
                "error_message": None,
                "data": None
            }

            return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

        response = {
                "status": True, 
                "message": "Todo data found.",
                "error_message": None,
                "data": todo
            }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": False, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

# TODO work remaining from update todo
@app.put("/todo/{id}", response_model=schemas.Todo)
def update_todo(id: int, db: Session = Depends(get_db)):
    try:
        todo = crud.get_todo(db, todo_id=id)
        if todo is None:
            response = {
                "status": True, 
                "message": "Todo not found.",
                "error_message": None,
                "data": None
            }

            return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
        
        todo_data = crud.update_todo(db=db, todo=todo)
        response = {
                "status": True, 
                "message": "Todo updated successfully.",
                "error_message": None,
                "data": todo_data
            }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": False, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)

@app.delete("/todo/{id}", response_model=schemas.Todo)
def delete_todo(id: int, db: Session = Depends(get_db)):
    try:
        todo = crud.get_todo(db, todo_id=id)
        if todo is None:
            response = {
                "status": True, 
                "message": "Todo not found.",
                "error_message": None,
                "data": None
            }

            return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)

        todo_data = crud.delete_todo(db=db, todo_id=id)
        response = {
                "status": True, 
                "message": "Todo deleted successfully.",
                "error_message": None,
                "data": todo_data
            }
        response = jsonable_encoder(response)

    except Exception as e:
        response = {
            "status": False, 
            "message": "Something went wrong",
            "error_message": str(e),
            "data": None
        }

        return JSONResponse(content=response, status_code=status.HTTP_400_BAD_REQUEST)
    
    return JSONResponse(content=response, status_code=status.HTTP_200_OK)
