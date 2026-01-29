from fastapi import APIRouter, Depends, HTTPException, status, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db
from app.models.user import User
from app.utils.security import get_password_hash, verify_password, create_access_token
from app.utils.templates import templates
from datetime import timedelta

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("pages/register.html", {"request": request})

@router.post("/register")
async def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    full_name: str = Form(None),
    db: AsyncSession = Depends(get_db)
):
    # Check if user exists
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    if result.scalars().first():
        return templates.TemplateResponse("pages/register.html", {
            "request": request,
            "error": "Email already registered"
        })
    
    import logging
    logger = logging.getLogger(__name__)
    try:
        new_user = User(
            email=email,
            password_hash=get_password_hash(password),
            full_name=full_name
        )
        db.add(new_user)
        await db.commit()
    except Exception as e:
        logger.error(f"Registration error: {e}")
        await db.rollback()
        return templates.TemplateResponse("pages/register.html", {
            "request": request,
            "error": f"Database error: {str(e)}"
        })
    
    return RedirectResponse(url="/auth/login", status_code=status.HTTP_303_SEE_OTHER)

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("pages/login.html", {"request": request})

@router.post("/login")
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalars().first()
    
    if not user or not verify_password(password, user.password_hash):
        return templates.TemplateResponse("pages/login.html", {
            "request": request,
            "error": "Invalid email or password"
        })
    
    # Create token & set cookie
    access_token = create_access_token(data={"sub": str(user.id)})
    response = RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return response

@router.get("/logout")
async def logout():
    response = RedirectResponse(url="/auth/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("access_token")
    return response
