from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id   = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age  = Column(Integer, nullable=False)

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    hours = Column(Integer, nullable=False)

