from pydantic import BaseModel
class StudentCreate(BaseModel):
    name: str
    age: int
class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    class Config:
        from_attributes= True

class CourseCreate(BaseModel):
    title: str
    hours: int
class CourseResponse(BaseModel):
    id: int
    title: str
    hours: int
    class Config:
        from_attributes= True

