# Stage 1: Frontend (Just copying files now)
FROM node:18-alpine as build-frontend

WORKDIR /app/frontend
# Copy the frontend folder into the container
COPY frontend/ ./

# Stage 2: Python Backend
FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
RUN pip install fastapi uvicorn pydantic requests

# Copy Backend Code
COPY backend/ backend/
COPY docs/ docs/
COPY challenge.yml .

# ✅ CRITICAL STEP: Copy the src folder (where index.html is) to /app/static
COPY --from=build-frontend /app/frontend/src /app/static

# Start the server
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
