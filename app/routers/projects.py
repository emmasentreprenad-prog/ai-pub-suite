from fastapi import APIRouter
from pydantic import BaseModel
from app.services.project import save_project, list_projects, load_project

router = APIRouter(prefix="/projects", tags=["projects"])

class SaveReq(BaseModel):
    title: str
    genre: str
    pitch: str
    outline: list
    characters: list
    chapter1: dict

@router.post("/save")
def save(req: SaveReq):
    pid = save_project(
        req.title,
        req.genre,
        req.pitch,
        req.outline,
        req.characters,
        req.chapter1
    )
    return {"success": True, "project_id": pid}

@router.get("/list")
def list_all():
    return list_projects()

@router.get("/load/{pid}")
def load(pid: int):
    return load_project(pid)

