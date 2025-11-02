import json, os
from sqlmodel import select
from app.models.db import get_session, Topic, SOP, VaultItem

DATA_DIR = os.path.join("app", "data")

def _load(name):
    with open(os.path.join(DATA_DIR, name), "r", encoding="utf-8") as f:
        return json.load(f)

def seed_all():
    with get_session() as s:
        if not s.exec(select(Topic)).first():
            for row in _load("topics.json"):
                s.add(Topic(**row))
        if not s.exec(select(SOP)).first():
            for row in _load("sops.json"):
                s.add(SOP(**row))
        if not s.exec(select(VaultItem)).first():
            for row in _load("vault.json"):
                s.add(VaultItem(**row))
        s.commit()
