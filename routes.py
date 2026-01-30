from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles


def create_app(static_dir: str) -> FastAPI:
    api = APIRouter()

    @api.get("/health")
    def health():
        return {"ok": True}

    app = FastAPI()
    app.include_router(api, prefix="/api")
    app.mount("/", StaticFiles(directory=static_dir, html=True), name="ui")
    return app
