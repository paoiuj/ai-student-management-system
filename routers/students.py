from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from db_models import Student as StudentModel
from schemas import StudentCreate, StudentResponse
router = APIRouter()
@router.get("/students", response_model=List[StudentResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(StudentModel).all()
@router.get("/students/{student_id}", response_model=StudentResponse)
def get_one(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="学生未找到")
    return student
@router.post("/students", response_model=StudentResponse)
def create(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = StudentModel(name=student.name, age=student.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
@router.delete("/students/{student_id}")
def delete(student_id: int, db: Session = Depends(get_db)):
    student = db.query(StudentModel).filter(StudentModel.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="学生未找到")
    db.delete(student)
    db.commit()
    return {"message": f"已删除 {student.name}"}
