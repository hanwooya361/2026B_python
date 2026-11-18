import asyncio
import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from Service import service

router = APIRouter(prefix="/api")


@router.post("/predict")
async def predict(data: dict):
    return service.predict(data)

class PredictStream:
    def __init__(self, data):
        self.data = data
        self.step = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.step += 1
        if self.step == 1:
            return