from fastapi import FastAPI
from routers.courses  import router as courses_router
from routers.students import router as students_router
from routers.analyze  import router as analyze_router

app = FastAPI()

app.include_router(courses_router)
app.include_router(students_router)
app.include_router(analyze_router)


@app.get("/")
def root():
    return {"message": "欢迎使用学校管理系统，请访问 /docs"}
