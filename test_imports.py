try:
    from app.models.user import User
    from app.models.product import Product
    from app.models.job import ScrapingJob
    from app.routes import auth, scrape
    from api.index import app
    print("All imports successful")
except Exception as e:
    import traceback
    traceback.print_exc()
