import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.app.routes import dashboard, workflow, appeal, flag

app = FastAPI(title="Compliance System")

# API Routers
app.include_router(dashboard.router)
app.include_router(workflow.router)
app.include_router(appeal.router)
app.include_router(flag.router)

# Mount static files (optional, but good for assets)
app.mount("/static", StaticFiles(directory="/app/static"), name="static")

# ✅ FIXED CATCH-ALL ROUTE
@app.get("/{full_path:path}")
async def catch_all(full_path: str):
    # Check if the requested file actually exists on disk (e.g., source_code.zip)
    file_path = f"/app/static/{full_path}"
    
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return FileResponse(file_path)

    # If file not found (or it's a UI route like /dashboard), serve index.html
    return FileResponse("/app/static/index.html")
