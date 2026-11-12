# [1] 라우터: 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter
# router = APIRouter(prefix="/공통URL")
router = APIRouter(prefix="/api")

# [3] 다양한 REST API CRUD
# 서비스 불러오기
from Service import item_service
# 1) 전체조회
@router.get("/items")
async def items():
    # 서비스내 함수 호출
    return item_service.items()