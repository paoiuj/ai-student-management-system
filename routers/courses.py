from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.engine import create
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from db_models import Course as CourseModel
from schemas import CourseCreate, CourseResponse

router = APIRouter()
@router.get("/courses", response_model=List[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()
@router.get("/courses/{id}", response_model=CourseResponse)
def get_course(id=int, db: Session = Depends(get_db)):
    course = db.query(CourseModel).filter(CourseModel.id == id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
@router.post("/courses", response_model=CourseResponse)
def create_course(db: Session = Depends(get_db)):
    new_course = CourseModel(title=course.title, hours=course.hours)
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course
@router.delete("/courses/{id}")
def delete_course(id: int, db: Session = Depends(get_db)):
    course = db.query(CourseModel).filter(CourseModel.id == id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return{"message": "Course deleted successfully"}
