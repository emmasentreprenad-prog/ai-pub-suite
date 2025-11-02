from fastapi import APIRouter, Query
router = APIRouter(prefix="/topics", tags=["topics"])

ROMANCE = [
    {"pitch":"A city chef inherits a failing diner and clashes with a mountain rescuer.",
     "id":1,"est_words":"65k","genre":"Romance","trope":"Grumpy/Sunshine, Small Town",
     "comps":"Abby Jimenez, Emily Henry","outline_hint":"24 chapters slow-burn, dual POV"},
    {"pitch":"A librarian fakes a relationship with the town firefighter to save the library.",
     "id":2,"est_words":"70k","genre":"Romance","trope":"Fake dating, found family",
     "comps":"Ali Hazelwood","outline_hint":"Slow burn, banter-heavy"}
]
THRILLER = [
    {"pitch":"A med student on a ferry witnesses a staged accident hiding a bio-lab coverup.",
     "id":3,"est_words":"80k","genre":"Thriller","trope":"Island conspiracy",
     "comps":"Taylor Adams","outline_hint":"Short chapters, multi-POV"},
    {"pitch":"A climate journalist uncovers a data-tampering plot before a storm hits.",
     "id":4,"est_words":"85k","genre":"Thriller","trope":"Deadline race",
     "comps":"Michael Crichton","outline_hint":"Tight pacing, rising stakes"}
]

@router.get("")
def list_topics(genre: str = Query("Romance")):
    g = (genre or "").lower()
    if "thrill" in g:
        return THRILLER
    return ROMANCE
