# app/services/outline.py
from typing import List, Dict

ROMANCE_BEATS = [
    "Hook / Meet-cute", "Adhesion (tvingas samarbeta)", "Förnekelse / Push-pull",
    "Första närmandet", "Felsteg / Konflikt växer", "Sårbarhet / Backstory-hint",
    "Mellanspel / Lättnad", "Yttre hinder eskalerar", "Kysströskel / Intimitet",
    "Missförstånd / Breakup", "Sanning på bordet", "Grand gesture + HEA"
]

THRILLER_BEATS = [
    "Kall öppning / fara", "Inciting incident", "Undersökningen börjar",
    "Fördjupad fara", "Falsk ledtråd", "Vändpunkt 1",
    "Tiden rinner / klocka", "Förräderi / twist", "Allt verkar förlorat",
    "Sanningen avslöjas", "Final konfrontation", "Epilog / efterspel"
]

def _expand(beats: List[str], chapters: int) -> List[str]:
    # Fördela beats över valda kapitel, fyll ut med variationsrubriker
    if chapters < len(beats):
        # Trimmar om man valt få kapitel
        beats = beats[:chapters]
    out = []
    repeats = chapters // len(beats)
    remainder = chapters % len(beats)
    for i, b in enumerate(beats):
        out.append(b)
        for j in range(repeats-1):
            out.append(f"{b} (fördjupning {j+1})")
    # lägg till extra scener om några kapitel återstår
    adders = ["Komplikation", "Fördjupad konflikt", "Val med konsekvens", "Ny ledtråd", "Emotionell konsekvens"]
    k = 0
    while len(out) < chapters:
        out.append(adders[k % len(adders)])
        k += 1
    return out[:chapters]

def guess_chapters(est_words: str | int | None) -> int:
    try:
        if isinstance(est_words, str) and est_words.lower().endswith("k"):
            w = int(est_words[:-1]) * 1000
        else:
            w = int(est_words or 60000)
    except:
        w = 60000
    # grovt: 2.5k per kapitel
    ch = max(12, min(36, round(w / 2500)))
    return ch

def make_outline(genre: str, pitch: str, est_words: str|int|None, outline_hint: str="") -> List[Dict]:
    chapters = guess_chapters(est_words)
    if "romance" in genre.lower():
        beats = _expand(ROMANCE_BEATS, chapters)
        pov_cycle = ["POV A", "POV B"]
    elif "thrill" in genre.lower():
        beats = _expand(THRILLER_BEATS, chapters)
        pov_cycle = ["Protagonist", "Antagonist/Hot"]
    else:
        # generisk 3-akt
        base = ["Setup", "Rising action", "Midpoint", "Complications", "Dark night", "Climax", "Resolution"]
        beats = _expand(base, chapters)
        pov_cycle = ["POV A"]

    outline = []
    for i, beat in enumerate(beats, start=1):
        pov = pov_cycle[(i-1) % len(pov_cycle)]
        outline.append({
            "chapter": i,
            "title": f"Kapitel {i}: {beat}",
            "pov": pov,
            "goal": f"Driv {beat.lower()} framåt i linje med: {pitch}",
            "notes": outline_hint or ""
        })
    return outline
