# app/models/db.py
import sqlite3
from pathlib import Path

_DB_PATH = Path(__file__).resolve().parents[2] / "app.db"
_conn = None

def get_db():
    """Return a singleton sqlite connection."""
    global _conn
    if _conn is None:
        _conn = sqlite3.connect(_DB_PATH, check_same_thread=False)
    return _conn

def init_db():
    """Create required tables if they do not exist."""
    db = get_db()
    cur = db.cursor()  # <-- THIS must exist before cur.execute()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        genre TEXT,
        pitch TEXT,
        outline TEXT,
        characters TEXT,
        chapter1 TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    db.commit()

