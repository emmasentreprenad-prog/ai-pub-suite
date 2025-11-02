# app/services/chapters.py
from typing import List, Dict
import textwrap, random

def _paragraph(text: str) -> str:
    return textwrap.fill(text, width=88)

def _pick_pov(characters: List[Dict] | List | None, fallback: str = "POV") -> str:
    """Choose a POV name safely, even if characters are missing fields."""
    if not characters:
        return fallback

    preferred_roles = ("Protagonist", "Love Interest", "Ally", "Best Friend")
    for role in preferred_roles:
        for c in characters:
            if isinstance(c, dict) and c.get("role") == role:
                return (c.get("name") or c.get("role") or fallback)

    for c in characters:
        if isinstance(c, dict):
            return (c.get("name") or c.get("role") or fallback)
        else:
            return str(c)
    return fallback

def write_chapter_one(
    genre: str,
    pitch: str,
    outline: List[Dict] | None,
    characters: List[Dict] | None,
    words: int = 900
) -> Dict:
    # Title / opener
    opener = "Hook / Meet-cute" if "romance" in genre.lower() else "Kall öppning / fara"
    if outline:
        opener = outline[0].get("title", opener)

    pov_name = _pick_pov(characters or [], fallback="POV")
    mood = "varm, stillsam" if "romance" in genre.lower() else "spänd, hotfull"
    setting = "småstadens diner vid stängning" if "romance" in genre.lower() else "färjans vindpinade däck i mörkret"

    # Find a lead character (safe)
    pro = None
    for c in (characters or []):
        if isinstance(c, dict) and c.get("role") in ("Protagonist", "Love Interest"):
            pro = c
            break

    quirk = (pro.get("quirk") if isinstance(pro, dict) else None) or "andas lugnt för att samla mod"
    gmc = (pro.get("gmc") if isinstance(pro, dict) else None) or {}
    want = gmc.get("goal", "vill skapa trygghet")

    beats = [
        f"Kapitel 1 – {opener}",
        f"{pov_name} introduceras i {setting}; stämningen är {mood}.",
        f"{pov_name} {quirk}. Vi förstår att {pov_name.lower()} {want.lower()}.",
        f"En händelse stör vardagen och knyter till bokens pitch: {pitch}",
        "Ett val måste göras; något litet riskeras för att peka mot större insats.",
        "Scenen slutar med en krok som lovar mer konflikt."
    ]

    paras: List[str] = []
    for b in beats:
        extra = ""
        if "händelse" in b:
            extra = (" " + ("En främling kliver in med nyheter som ändrar allt."
                     if "romance" in genre.lower()
                     else "En dämpad smäll ekar under däcket, och lamporna fladdrar."))
        if "krok" in b:
            extra += " " + ("På dörren sitter ett gammalt foto – och ansiktet på bilden känns för välbekant."
                            if "romance" in genre.lower()
                            else "En röd varningslampa tänds i maskinrummet – men någon har tejpat över sensorn.")
        paras.append(_paragraph(b + extra))

    # Pad to approximate length
    fillers = [
        "Detaljer i miljön fördjupar stämningen.",
        "En tanke eller ett minne blinkar förbi och antyder ett sår.",
        "Ljud, lukt och rörelse ritar scenen tydligare.",
        "Någon säger något tvetydigt, och tystnaden blir ett svar."
    ]
    while sum(len(p) for p in paras) < words * 0.8:
        paras.insert(-1, _paragraph(random.choice(fillers)))

    return {"title": beats[0], "pov": pov_name, "text": "\n\n".join(paras)}
