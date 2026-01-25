from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from itsdangerous import URLSafeSerializer
from app.config import settings
from app.database import get_db, engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.routes import scrape

app = FastAPI(title="CodeCanyon Intelligence API")
app.include_router(scrape.router)

# Add Session Middleware
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# Setup templates
templates = Jinja2Templates(directory="templates")

# CSRF Protection
serializer = URLSafeSerializer(settings.SECRET_KEY)

def get_csrf_token(request: Request = None):
    # Safely get session_id if middleware is active and request is processed
    session_id = "anonymous"
    if request:
        try:
            session_id = request.session.get("session_id", "anonymous")
        except (RuntimeError, AttributeError):
            pass
    return serializer.dumps({"session_id": session_id})

templates.env.globals["csrf_token"] = get_csrf_token

@app.middleware("http")
async def csrf_middleware(request: Request, call_next):
    if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
        if "HX-Request" in request.headers:
            token = request.headers.get("X-CSRF-Token")
            if not token:
                raise HTTPException(status_code=403, detail="CSRF token missing")
            try:
                serializer.loads(token)
            except Exception:
                raise HTTPException(status_code=403, detail="CSRF token invalid")
    return await call_next(request)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("pages/home.html", {"request": request})

@app.get("/scraper", response_class=HTMLResponse)
async def scraper_dashboard(request: Request):
    return templates.TemplateResponse("pages/scraper.html", {"request": request})

@app.get("/test-db")
async def test_db(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return templates.TemplateResponse("components/status_badge.html", {
            "request": request,
            "status": "success",
            "message": "Database Connected"
        })
    except Exception as e:
        return templates.TemplateResponse("components/status_badge.html", {
            "request": request,
            "status": "error",
            "message": f"DB Error: {str(e)}"
        })
