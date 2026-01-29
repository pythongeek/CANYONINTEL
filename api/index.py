import os
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware
from app.config import settings
from app.database import get_db, engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, desc
from app.models.product import Product
from app.routes import scrape, auth, dashboard, planner
from app.utils.templates import templates, serializer

from fastapi.staticfiles import StaticFiles

app = FastAPI(title="CodeCanyon Intelligence API")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(scrape.router)
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(planner.router)

# Middleware will be added below in correct order

# CSRF token global is now handled in app.utils.templates

@app.middleware("http")
async def csrf_middleware(request: Request, call_next):
    # 1. Initialize or get CSRF token from session
    if "csrf_token" not in request.session:
        request.session["csrf_token"] = os.urandom(32).hex()
    
    # 2. Inject into scope for templates
    request.scope["csrf_token"] = request.session["csrf_token"]

    # 3. Validate on mutation methods
    if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
        if "HX-Request" in request.headers:
            token = request.headers.get("X-CSRF-Token")
            if not token or token != request.session["csrf_token"]:
                raise HTTPException(status_code=403, detail="CSRF token invalid or missing")
    
    return await call_next(request)

# IMPORTANT: Middleware order is Last-In-First-Out (LIFO) in Starlette.
# We want SessionMiddleware to run FIRST (be the outermost), then csrf_middleware.
# So we add csrf_middleware first (closest to app), then SessionMiddleware.
app.add_middleware(SessionMiddleware, secret_key=settings.SECRET_KEY)

# Root route is now handled by dashboard.router

@app.get("/scraper", response_class=HTMLResponse)
async def scraper_dashboard(request: Request, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).order_by(desc(Product.created_at)).limit(8))
    recent_products = result.scalars().all()
    return templates.TemplateResponse("pages/scraper.html", {
        "request": request, 
        "recent_products": recent_products
    })

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
