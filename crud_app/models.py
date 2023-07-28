from sqlalchemy import Column, String, UUID, Integer
from crud_app.database import Base

class Todos(Base):
    __tablename__ = "todos"

    # id = Column(UUID, primary_key=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
