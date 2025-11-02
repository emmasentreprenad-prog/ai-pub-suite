# app/routers/chapters.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
from app.services.chapters import write_chapter_one
import traceback

router = APIRouter(prefix="/chapters", tags=["chapters"])

class ChapterReq(BaseModel):
    genre: str
    pitch: str
    outline: Optional[List[Dict]] = None
    characters: Optional[List[Dict]] = None
    target_words: int = 900

@router.post("/write")
def write(req: ChapterReq):
    try:
        ch = write_chapter_one(
            genre=req.genre,
            pitch=req.pitch,
            outline=req.outline or [],
            characters=req.characters or [],
            words=req.target_words,
        )
        return {"chapter": ch}
    except Exception as e:
        print("=== Chapter writer error ===")
        print(traceback.format_exc())
        return JSONResponse(status_code=400, content={
            "error": str(e),
            "tip": "Try with empty outline/characters []. Check request JSON."
        })
