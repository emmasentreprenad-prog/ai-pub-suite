# app/services/characters.py
from typing import List, Dict
import random

ROMANCE_ARCHETYPES = [
    ("Protagonist", "Driven, varm, sårbar", "Vill skapa trygghet", "Räds att bli sviken"),
    ("Love Interest", "Stillsam, lojal, hemlighetsfull", "Vill våga älska", "Räds att förlora kontrollen"),
    ("Best Friend", "Vitsig, stödjande", "Vill huvudpersonen väl", "Räds förändring"),
]

THRILLER_ARCHETYPES = [
    ("Protagonist", "Skärpt, envis, moraliskt kompass", "Vill avslöja sanningen", "Räds att misslyckas"),
    ("Antagonist", "Karisma, iskall, kalkylerande", "Vill dölja sanningen", "Räds att bli avslöjad"),
    ("Ally", "Resursstark, osäker lojalitet", "Vill överleva", "Räds att välja fel sida"),
]

ROMANCE_QUIRKS = ["bitar på läppen när nervös", "sparar kvitton i en burk", "sjunger i duschen", "samlar på vykort"]
THRILLER_QUIRKS = ["sover med lampan tänd", "kodar små skript", "fail-safe ritual", "spelar schack ensam"]

FIRST_NAMES = ["Ava","Maya","Liam","Noah","Elena","Sophia","Leo","Mika","Aria","Isak","Nora","Milan"]
LAST_NAMES  = ["Andersson","Lind","Berg","Holm","Svensson","Ek","Dahl","Sand","Nyberg","Lund"]

def rand_name() -> str:
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def gmc(goal:str, motivation:str, conflict:str)->Dict:
    return {"goal":goal, "motivation":motivation, "conflict":conflict}

def make_characters(genre:str, pitch:str) -> List[Dict]:
    out: List[Dict] = []
    if "romance" in genre.lower():
        arch = ROMANCE_ARCHETYPES
        quirks = ROMANCE_QUIRKS
        rel_arcs = ["fiender → vänner → förälskade", "grumpy/sunshine", "second-chance"]
    elif "thrill" in genre.lower():
        arch = THRILLER_ARCHETYPES
        quirks = THRILLER_QUIRKS
        rel_arcs = ["mentor → förrädare", "oväntad allierad", "moral vs överlevnad"]
    else:
        arch = ROMANCE_ARCHETYPES
        quirks = ROMANCE_QUIRKS
        rel_arcs = ["tilltro → konflikt → samhörighet"]

    for role, traits, want, fear in arch:
        out.append({
            "name": rand_name(),
            "role": role,
            "traits": traits,
            "gmc": gmc(want, f"Drivs av {want.lower()}", fear),
            "quirk": random.choice(quirks),
            "arc": random.choice(rel_arcs),
            "fits_pitch": pitch[:140] + ("..." if len(pitch)>140 else "")
        })
    return out
