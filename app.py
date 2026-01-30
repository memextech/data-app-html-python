import modal

app = modal.App("data-app")

LOCAL_UI_DIR = "./dist"
REMOTE_UI_DIR = "/ui"

image = (
    modal.Image.debian_slim()
    .pip_install("fastapi>=0.110", "uvicorn>=0.27")
    .add_local_dir(LOCAL_UI_DIR, remote_path=REMOTE_UI_DIR, copy=True)
    .add_local_file("routes.py", remote_path="/root/routes.py", copy=True)
)


@app.function(image=image)
@modal.asgi_app()
def asgi():
    from routes import create_app
    return create_app(REMOTE_UI_DIR)
