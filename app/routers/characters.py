# app/routers/characters.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from app.services.characters import make_characters

router = APIRouter(prefix="/characters", tags=["characters"])

class CharReq(BaseModel):
    genre: str
    pitch: str
    count: Optional[int] = 3  # reserverad, används senare

@router.post("/generate")
def generate_characters(req: CharReq):
    chars = make_characters(req.genre, req.pitch)
    return {"characters": chars}
