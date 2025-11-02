# app/routers/outline.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, List, Dict
from app.services.outline import make_outline

router = APIRouter(prefix="/outline", tags=["outline"])

class OutlineReq(BaseModel):
    genre: str
    pitch: str
    est_words: Optional[str] = "60k"
    outline_hint: Optional[str] = ""
    chapters: Optional[int] = None  # om du vill tvinga antal

@router.post("/generate")
def generate_outline(req: OutlineReq):
    outline = make_outline(req.genre, req.pitch, req.est_words, req.outline_hint)
    # om chapters anges, trimmar/ökar listan
    if req.chapters:
        if req.chapters > len(outline):
            # fyll ut
            while len(outline) < req.chapters:
                i = len(outline) + 1
                outline.append({
                    "chapter": i,
                    "title": f"Kapitel {i}: Extra scen",
                    "pov": outline[-1]["pov"] if outline else "POV",
                    "goal": "Fördjupa konflikten",
                    "notes": ""
                })
        outline = outline[:req.chapters]
        # uppdatera kapitelnummer
        for i, ch in enumerate(outline, start=1):
            ch["chapter"] = i
    return {"outline": outline}
