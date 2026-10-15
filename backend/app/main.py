from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from pathlib import Path

from .vault import router as vault_router

app = FastAPI()

# Frontend paths
FRONTEND_DIR = Path("/code/frontend")
TEMPLATES_DIR = FRONTEND_DIR / "templates"
STATIC_DIR = FRONTEND_DIR / "static"

# Connect CSS and JavaScript
app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static"
)

# Connect vault routes
app.include_router(vault_router, prefix="/vault")

@app.get("/")
def home():
    return FileResponse(TEMPLATES_DIR / "index.html")