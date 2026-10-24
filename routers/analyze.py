# routers/analyze.py
from fastapi import APIRouter
from pydantic import BaseModel
from analyzer import analyze_text_async

# ① 创建子路由
router = APIRouter()

# ② 定义请求体形状——客户端必须传一个 text 字段
class AnalyzeRequest(BaseModel):
    text: str

# ③ 异步路由——调用大模型时不卡服务器
@router.post("/analyze")
async def analyze_endpoint(request: AnalyzeRequest):
    result = await analyze_text_async(request.text)
    return result