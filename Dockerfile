# ----------------------------------------------------
# Stage 1: Frontend (Files Prepare karna)
# ----------------------------------------------------
FROM node:18-alpine as build-frontend

WORKDIR /app/frontend

# 1. Dependencies install karein (Cache layer)
COPY frontend/package*.json ./
RUN npm install

# 2. Poora frontend code copy karein
COPY frontend/ .

# ----------------------------------------------------
# Stage 2: Python Backend (Final Server)
# ----------------------------------------------------
FROM python:3.11-slim

WORKDIR /app

# 1. Python dependencies install karein
RUN pip install fastapi uvicorn pydantic requests

# 2. Backend Logic copy karein
COPY backend/ backend/
COPY challenge.yml .
# Note: Agar docs folder nahi hai to ye line hata dein warna error ayega
# COPY docs/ docs/ 

# ----------------------------------------------------
# ✅ THE CRITICAL FIX (Folders Merge Logic)
# ----------------------------------------------------

# Step A: Static folder banayein
RUN mkdir -p /app/static

# Step B: 'src' folder (index.html, styles) copy karein
COPY --from=build-frontend /app/frontend/src /app/static

# Step C: 'public' folder (source_code.zip, robots.txt) copy karein
# Docker isay pichle files ke sath mix kar dega.
COPY --from=build-frontend /app/frontend/public /app/static

# ----------------------------------------------------

# Server Start
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8080"]
