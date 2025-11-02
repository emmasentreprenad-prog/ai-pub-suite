from fastapi import APIRouter
router = APIRouter(prefix="/vault", tags=["vault"])
DATA = [
    {"genre":"Romance","title":"Romancing the Beat Map","id":1,"type":"prompt","tags":"beats,slow-burn",
     "body_md":"# Beat Map\n1. Meet Cute\n2. Adhesion\n3. Retreat"},
    {"genre":"Thriller","title":"High-Tension Scene Starter","id":2,"type":"prompt","tags":"pacing,cliffhanger",
     "body_md":"Open with a sensory jolt, then obstacle, then a choice with stakes."}
]
@router.get("")
def get_vault():
    return DATA
