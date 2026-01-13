from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.routes import dashboard, workflow, appeal, flag

app = FastAPI(title="Compliance System")

app.include_router(dashboard.router)
app.include_router(workflow.router)
app.include_router(appeal.router)
app.include_router(flag.router)

# Mount the static frontend files
app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# Catch-all to serve index.html (SPA routing)
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    # ✅ FIX: Serve the compiled HTML file, not the raw JSX
    return FileResponse("/app/static/index.html")
