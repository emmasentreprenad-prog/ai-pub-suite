from fastapi import APIRouter
router = APIRouter(prefix="/sops", tags=["sops"])
DATA = [
    {"id":1,"title":"KDP Upload Checklist",
     "steps_md":"- Export EPUB\n- Fill metadata\n- Select categories\n- Upload cover\n- Mark AI-generated content if applicable\n- Submit & review proof"},
    {"id":2,"title":"$100 Budget Publishing",
     "steps_md":"- Self-edit pass\n- AI polish + human skim\n- Canva cover\n- Free ISBN via KDP\n- Soft launch to ARC list"}
]
@router.get("")
def get_sops():
    return DATA
