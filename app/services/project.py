import json
from app.models.db import get_db

def save_project(title, genre, pitch, outline, characters, chapter1):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO projects (title, genre, pitch, outline, characters, chapter1)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        title,
        genre,
        pitch,
        json.dumps(outline),
        json.dumps(characters),
        json.dumps(chapter1)
    ))
    db.commit()
    return cur.lastrowid

def list_projects():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT id, title, genre, created_at FROM projects ORDER BY id DESC")
    return cur.fetchall()

def load_project(pid):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM projects WHERE id=?", (pid,))
    row = cur.fetchone()
    if not row:
        return None
    
    return {
        "id": row[0],
        "title": row[1],
        "genre": row[2],
        "pitch": row[3],
        "outline": json.loads(row[4]),
        "characters": json.loads(row[5]),
        "chapter1": json.loads(row[6]),
        "created_at": row[7]
    }
