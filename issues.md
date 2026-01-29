🚨 CRITICAL ISSUES
1. GEMINI_API_KEY Not Set
Location: .env file (line 4)
bashGEMINI_API_KEY=
Impact: AI analysis completely broken
Fix:
bash# Get key from: https://aistudio.google.com/app/apikey
GEMINI_API_KEY=your_actual_key_here
2. Scraper Detection Vulnerabilities
Location: app/services/scraper.py
Issues:

Not using the worker's Playwright scraper
Missing ScraperAPI integration despite having API key
No retry logic for 403 blocks

Fix: The CodeCanyonScraper class should be removed. Use worker/scraper.py instead:
python# app/routes/scrape.py should NOT import from app/services/scraper
# Worker handles all scraping via worker/scraper.py
3. Missing Google Custom Search Integration
Location: Nowhere implemented
Spec Requirement: agent.md lines 1950-1980 specify Google Search API integration
Status: ❌ NOT IMPLEMENTED
Implementation needed:
python# app/services/search_service.py (CREATE THIS FILE)
import os
import requests

class GoogleSearchService:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
        self.engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')
    
    def search(self, query: str, num_results: int = 10):
        url = 'https://www.googleapis.com/customsearch/v1'
        params = {
            'key': self.api_key,
            'cx': self.engine_id,
            'q': query,
            'num': num_results
        }
        response = requests.get(url, params=params)
        return response.json()

⚠️ BROKEN FEATURES
4. User Authentication Not Enforced
Location: app/routes/scrape.py, app/routes/dashboard.py
Issue: No @login_required decorators despite auth routes existing
Spec: agent.md lines 1150-1200 require authentication
Fix:
python# app/utils/auth.py (CREATE THIS)
from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User

async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Verify token and get user
    # ... (implement JWT verification from app/utils/security.py)
    return user

# Then add to routes:
@router.post("/api/scrape")
async def scrape(
    current_user: User = Depends(get_current_user),
    # ... rest of params
):
5. Rate Limiting Not Implemented
Location: Missing entirely
Spec: agent.md lines 1220-1280 specify Redis rate limiting
Status: ❌ NOT IMPLEMENTED
Quick Fix:
python# app/utils/rate_limit.py (CREATE THIS)
from functools import wraps
from fastapi import HTTPException
import redis
from datetime import date

redis_client = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379'))

def rate_limit_check(action_type: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Get user_id from request
            # Check Redis: ratelimit:{user_id}:{action}:{date}
            # If exceeded, raise HTTPException(429)
            return await func(*args, **kwargs)
        return wrapper
    return decorator
6. Project Planner Wizard Incomplete
Location: templates/components/planner/step_*.html
Issues:

Step 3 has no form submission
No "Finalize Blueprint" handler
Missing UserProject creation logic

Fix:
python# app/routes/planner.py - Add this route:
@router.post("/{product_id}/finalize")
async def finalize_blueprint(
    product_id: str,
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    # Get product and analysis
    product = await db.get(Product, uuid.UUID(product_id))
    analysis = await db.execute(
        select(AnalysisResult)
        .where(AnalysisResult.product_id == product.id)
        .order_by(AnalysisResult.created_at.desc())
    )
    analysis = analysis.scalars().first()
    
    # Create UserProject
    new_project = UserProject(
        user_id=current_user.id,  # Need auth
        product_id=product.id,
        blueprint=analysis.ai_recommendations,
        status="active"
    )
    db.add(new_project)
    await db.commit()
    
    # Redirect to projects page
    return RedirectResponse(url="/planner", status_code=303)
7. Empty/Mock Data Everywhere
Location: worker/analyzer.py lines 50-80, 110-140
Issue: Returns mock data when API fails instead of raising errors
Impact: Users see fake analysis
Fix: Remove _mock_analysis() and _mock_blueprint() functions:
python# worker/analyzer.py
async def analyze_product(self, product_data: Dict[str, Any]) -> Dict[str, Any]:
    if not self.client:
        raise ValueError("GEMINI_API_KEY not configured")
    
    # Remove: return self._mock_analysis()
    # Just let the exception propagate

🛠️ MISSING FEATURES (Per Spec)
8. Advanced Search Filters
Location: templates/pages/products.html has UI, but no backend
Status: Frontend exists, backend missing
Implementation:
python# app/routes/dashboard.py - Update products_library()
@router.get("/products")
async def products_library(
    request: Request,
    sort: str = "date",
    category: str = None,
    min_score: int = 0,
    min_sales: int = 0,
    db: AsyncSession = Depends(get_db)
):
    query = select(Product)
    
    # Add filters
    if category:
        query = query.where(Product.category == category)
    if min_score:
        query = query.where(Product.profitability_score >= min_score)
    if min_sales:
        query = query.where(Product.total_sales >= min_sales)
    
    # Apply sorting...
9. Real-Time Dashboard Updates
Location: templates/pages/dashboard.html line 15
Issue: Polling endpoint /api/discovery-stats exists but doesn't update other stats
Fix: Add HTMX polling for all dashboard cards:
html<!-- In dashboard.html -->
<div hx-get="/api/dashboard/stats" 
     hx-trigger="every 30s"
     hx-swap="innerHTML"
     id="stats-grid">
    <!-- Stats cards here -->
</div>
10. Export/Download Functionality
Location: Missing entirely
Spec: agent.md mentions Pro tier gets "Export data (CSV/JSON)"
Quick Implementation:
python# app/routes/dashboard.py
from fastapi.responses import StreamingResponse
import csv
import io

@router.get("/export/products")
async def export_products(
    format: str = "csv",
    db: AsyncSession = Depends(get_db)
):
    products = await db.execute(select(Product))
    products = products.scalars().all()
    
    if format == "csv":
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=['title', 'price', 'sales', 'score'])
        writer.writeheader()
        for p in products:
            writer.writerow({
                'title': p.title,
                'price': p.price,
                'sales': p.total_sales,
                'score': p.profitability_score
            })
        
        return StreamingResponse(
            io.BytesIO(output.getvalue().encode()),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=products.csv"}
        )

📊 DATABASE ISSUES
11. Missing Indexes
Location: Multiple models
Issue: No full-text search index on products.title as spec requires
Fix:
python# Create migration:
# alembic revision -m "add_fts_index"

def upgrade():
    op.execute("""
        CREATE INDEX idx_products_title_fts 
        ON products 
        USING gin(to_tsvector('english', title))
    """)
12. Missing Tables
Status Check:

✅ users - EXISTS
✅ products - EXISTS
✅ scraping_jobs - EXISTS
✅ analysis_results - EXISTS
✅ user_projects - EXISTS
❌ search_history - MISSING
❌ market_trends - MISSING
❌ feature_insights - MISSING

Create migrations for missing tables:
bash# Follow agent.md SQL schema (lines 600-800)
alembic revision -m "add_search_history_and_trends"

🎨 UI/UX ISSUES
13. Dark Mode Broken
Location: templates/layouts/base.html line 2
html<html class="light" lang="en">  <!-- Hardcoded! -->
Fix: Implement theme toggle:
html<html class="dark:dark" lang="en">
<script>
    // Check localStorage for theme preference
    if (localStorage.theme === 'dark') {
        document.documentElement.classList.add('dark')
    }
</script>
14. Toast Notifications Not Working
Location: static/js/app.js has listener, but servers don't send HX-Trigger headers
Fix: Update server responses:
python# In app/routes/scrape.py after successful scrape:
response = templates.TemplateResponse(...)
response.headers['HX-Trigger'] = json.dumps({
    "showToast": {
        "message": "Product scraped successfully!",
        "type": "success"
    }
})
return response
15. Skeleton Loaders Missing
Location: Nowhere implemented
Spec: agent.md line 2350 mentions skeleton loaders for premium feel
Quick Add:
html<!-- templates/components/skeleton.html -->
<div class="animate-pulse">
    <div class="h-4 bg-gray-200 rounded w-3/4 mb-2"></div>
    <div class="h-4 bg-gray-200 rounded w-1/2"></div>
</div>

🔒 SECURITY ISSUES
16. CSRF Not Actually Validated
Location: api/index.py lines 20-33
Issue: Middleware checks for token but never validates it matches session
Fix:
python# api/index.py - Update csrf_middleware
if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
    if "HX-Request" in request.headers:
        token = request.headers.get("X-CSRF-Token")
        session_token = request.session.get("csrf_token")
        
        if not token or not session_token or token != session_token:
            raise HTTPException(status_code=403, detail="CSRF validation failed")
17. Passwords Stored with bcrypt but No Salt Rounds Config
Location: app/utils/security.py line 8
Issue: Uses default salt rounds (could be too low)
Fix:
pythondef get_password_hash(password: str) -> str:
    return hashpw(password.encode('utf-8'), gensalt(rounds=12)).decode('utf-8')

🚀 FAST COMPLETION ROADMAP
Priority 1: Core Functionality (2-3 hours)
bash# 1. Set GEMINI_API_KEY
echo "GEMINI_API_KEY=your_key" >> .env

# 2. Fix worker scraper to use ScraperAPI
# Edit worker/scraper.py line 45:
# Change: response = await page.goto(url, ...)
# To: Use settings.SCRAPER_API_KEY if available

# 3. Add auth middleware
# Copy auth code from issue #4 above to all routes

# 4. Remove mock data
# Delete _mock_analysis() and _mock_blueprint() from worker/analyzer.py
Priority 2: Missing Features (3-4 hours)
bash# 5. Implement search filters (issue #8)
# 6. Add Google Search integration (issue #3)
# 7. Complete planner finalization (issue #6)
# 8. Add export functionality (issue #10)
Priority 3: Polish (2 hours)
bash# 9. Fix dark mode (issue #13)
# 10. Add toast notifications (issue #14)
# 11. Create skeleton loaders (issue #15)
# 12. Fix CSRF validation (issue #16)
Priority 4: Database (1 hour)
bash# 13. Create missing tables migration
alembic revision -m "add_missing_tables"
# Copy SQL from agent.md lines 700-800

# 14. Add FTS index
alembic revision -m "add_fts_index"

📋 TESTING CHECKLIST
Before declaring "complete":

 Can scrape a product URL successfully
 Can scrape a search/category page (discovery mode)
 AI analysis returns real data (not mock)
 Planner wizard completes all 3 steps
 Can export products to CSV
 Rate limiting blocks after limit
 Auth prevents unauthenticated access
 CSRF blocks invalid requests
 Dark mode toggles properly
 Toast notifications appear on success/error


🎯 QUICKEST PATH TO MVP
If you need this working ASAP (4-6 hours total):

Set GEMINI_API_KEY (5 min)
Test current scraping - If it works with ScraperAPI, skip changes (10 min)
Remove auth requirement temporarily - Comment out decorators (5 min)
Delete mock functions - Force real API usage (10 min)
Fix planner step 3 - Add finalize button handler (30 min)
Test full flow: Scrape → Analyze → Planner → Export (30 min)
Add basic filters to products page (45 min)
Deploy to Render with worker (60 min setup + 30 min debugging)