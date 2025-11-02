from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Publishing Suite — Minimal MVP")

ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "https://ai-pub-suite.onrender.com",
    "https://*.netlify.app",
    "https://publishing-wizard.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.models.db import init_db
from app.routers import topics, sops, vault, outline, characters, chapters, projects


app = FastAPI(title="AI Publishing Suite — Minimal MVP")
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(topics.router)
app.include_router(sops.router)
app.include_router(vault.router)
app.include_router(outline.router)
app.include_router(characters.router)
app.include_router(chapters.router)
app.include_router(projects.router)



@app.get("/")
def root():
    return {"ok": True}
