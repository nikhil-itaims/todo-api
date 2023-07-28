from sqlalchemy.orm import Session
from crud_app import models, schemas

def get_todo(db: Session, todo_id: int):
    return db.query(models.Todos).filter(models.Todos.id == todo_id).first()

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todos).offset(skip).limit(limit).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    todo_data = models.Todos(name=todo.name, description=todo.description)
    db.add(todo_data)
    db.commit()
    db.refresh(todo_data)
    return todo_data

# def update_todo(db: Session, todo_id: int, todo: schemas.TodoCreate):
#     db.query(models.Todos).filter(models.Todos.id == todo_id).first()
#     todo_data = models.Todos(name=todo.name, description=todo.description)
#     db.add(todo_data)
#     db.commit()
#     db.refresh(todo_data)
#     return todo_data

def delete_todo(db: Session, todo_id: int):
    todo = db.query(models.Todos).filter(models.Todos.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return todo
