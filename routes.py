import hashlib
import os

from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


def get_file_hash(filepath: str) -> str:
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def create_app(static_dir: str) -> FastAPI:
    api = APIRouter()
    templates = Jinja2Templates(directory=static_dir)

    @api.get("/health")
    def health():
        return {"ok": True}

    app = FastAPI()
    app.include_router(api, prefix="/api")

    @app.get("/", response_class=HTMLResponse)
    def index(request: Request):
        css_hash = get_file_hash(os.path.join(static_dir, "styles.css"))
        js_hash = get_file_hash(os.path.join(static_dir, "app.js"))
        return templates.TemplateResponse(
            request, "index.html", {"css_hash": css_hash, "js_hash": js_hash}
        )

    # Crawlers only look at the root path, but StaticFiles is mounted at
    # /static — without this route the file is unreachable at /robots.txt.
    @app.get("/robots.txt", include_in_schema=False)
    def robots():
        return FileResponse(os.path.join(static_dir, "robots.txt"))

    app.mount("/static", StaticFiles(directory=static_dir), name="ui")
    return app
