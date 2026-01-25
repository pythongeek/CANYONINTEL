# **CodeCanyon Intelligence Platform \- AI Agent Documentation**

## **Complete Development Guide for AI-Assisted Coding**

---

## **📋 Document Purpose**

This document provides comprehensive instructions for AI coding agents (Claude, Cursor, GitHub Copilot, etc.) to build the CodeCanyon Product Intelligence & Launch Assistant platform using HTMX architecture.

---

## **🎯 Project Overview**

**Platform Name**: CodeCanyon Intelligence Platform  
 **Architecture**: HTMX \+ Server-Side Rendering  
 **Primary Goal**: Discover profitable CodeCanyon products and guide users in creating competitive alternatives  
 **Tech Stack**: Python/Flask \+ PostgreSQL \+ Redis \+ HTMX \+ Tailwind CSS

---

## **🏗 System Architecture**

### **High-Level Structure**

┌─────────────────────────────────────────────────────────────┐  
│                        Browser (Client)                      │  
│  HTMX \+ Alpine.js \+ Tailwind CSS \+ Chart.js                │  
└────────────────────┬────────────────────────────────────────┘  
                     │ HTTP/HTMX Requests  
                     ▼  
┌─────────────────────────────────────────────────────────────┐  
│                    Flask Application Layer                   │  
│  ├─ Routes (API \+ Pages)                                    │  
│  ├─ Template Rendering (Jinja2)                             │  
│  ├─ Business Logic                                          │  
│  └─ Middleware (Auth, CSRF, Rate Limiting)                  │  
└─────┬───────────────────────┬───────────────────────────────┘  
      │                       │  
      ▼                       ▼  
┌─────────────────┐    ┌──────────────────┐  
│   PostgreSQL    │    │      Redis       │  
│  (Primary DB)   │    │  (Cache/Queue)   │  
└─────────────────┘    └──────────────────┘  
      │  
      ▼  
┌─────────────────────────────────────────────────────────────┐  
│                    Background Workers (Celery)               │  
│  ├─ Web Scraping Tasks                                      │  
│  ├─ Analysis Calculations                                   │  
│  ├─ AI Processing                                           │  
│  └─ Scheduled Jobs                                          │  
└─────────────────────────────────────────────────────────────┘  
      │  
      ▼  
┌─────────────────────────────────────────────────────────────┐  
│                    External APIs                             │  
│  ├─ Claude API (AI Recommendations)                         │  
│  ├─ Google Custom Search (Market Research)                  │  
│  └─ ScraperAPI (Proxy Services)                             │

└─────────────────────────────────────────────────────────────┘

---

## **📁 Project Structure**

### **Directory Organization**

codecanyon-intelligence/  
├── app/  
│   ├── \_\_init\_\_.py                 \# Flask app initialization  
│   ├── config.py                   \# Configuration management  
│   ├── models/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── product.py              \# Product model  
│   │   ├── user.py                 \# User model  
│   │   ├── analysis.py             \# Analysis result model  
│   │   ├── project.py              \# User project model  
│   │   └── search.py               \# Search history model  
│   ├── routes/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── main.py                 \# Homepage, static pages  
│   │   ├── auth.py                 \# Authentication routes  
│   │   ├── search.py               \# Product search  
│   │   ├── scrape.py               \# URL scraping  
│   │   ├── analyze.py              \# Profitability analysis  
│   │   ├── recommendations.py      \# AI recommendations  
│   │   ├── planner.py              \# Project planner  
│   │   ├── dashboard.py            \# User dashboard  
│   │   └── api.py                  \# API endpoints  
│   ├── services/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── scraper.py              \# Web scraping logic  
│   │   ├── analyzer.py             \# Profitability calculations  
│   │   ├── ai\_service.py           \# Claude API integration  
│   │   ├── search\_service.py       \# Google Search integration  
│   │   └── cache\_service.py        \# Redis caching  
│   ├── utils/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── validators.py           \# Input validation  
│   │   ├── helpers.py              \# Helper functions  
│   │   └── decorators.py           \# Custom decorators  
│   ├── tasks/  
│   │   ├── \_\_init\_\_.py  
│   │   ├── scraping.py             \# Celery scraping tasks  
│   │   ├── analysis.py             \# Background analysis  
│   │   └── maintenance.py          \# Cleanup tasks  
│   └── templates/  
│       ├── layouts/  
│       │   ├── base.html           \# Master template  
│       │   └── dashboard.html      \# Dashboard layout  
│       ├── components/  
│       │   ├── navbar.html  
│       │   ├── product\_card.html  
│       │   ├── analysis\_panel.html  
│       │   ├── filter\_sidebar.html  
│       │   └── pagination.html  
│       ├── pages/  
│       │   ├── home.html  
│       │   ├── search.html  
│       │   ├── product\_detail.html  
│       │   ├── dashboard.html  
│       │   ├── planner.html  
│       │   └── settings.html  
│       └── auth/  
│           ├── login.html  
│           ├── register.html  
│           └── oauth\_callback.html  
├── static/  
│   ├── css/  
│   │   ├── tailwind.css            \# Tailwind config  
│   │   └── custom.css              \# Custom styles  
│   ├── js/  
│   │   ├── htmx.min.js             \# HTMX library  
│   │   ├── alpine.min.js           \# Alpine.js (optional)  
│   │   ├── chart.min.js            \# Chart.js  
│   │   └── app.js                  \# Custom JS  
│   └── images/  
│       └── logo.svg  
├── migrations/                      \# Database migrations  
│   └── versions/  
├── tests/  
│   ├── \_\_init\_\_.py  
│   ├── test\_models.py  
│   ├── test\_routes.py  
│   ├── test\_services.py  
│   └── test\_scraper.py  
├── .env.example                     \# Environment template  
├── .gitignore  
├── requirements.txt                 \# Python dependencies  
├── README.md  
├── run.py                          \# Application entry point

└── celery\_worker.py                \# Celery worker entry

---

## **🗄 Database Schema (PostgreSQL)**

### **Complete SQL Schema**

sql  
*\-- Enable UUID extension*  
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

*\-- Users Table*  
CREATE TABLE users (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    email VARCHAR(255) UNIQUE NOT NULL,  
    password\_hash VARCHAR(255),  
    full\_name VARCHAR(200),  
    oauth\_provider VARCHAR(50),  
    oauth\_id VARCHAR(255),  
    subscription\_tier VARCHAR(20) DEFAULT 'free' CHECK (subscription\_tier IN ('free', 'pro', 'enterprise')),  
    api\_calls\_remaining INTEGER DEFAULT 10,  
    preferences JSONB DEFAULT '{}',  
    created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    last\_login TIMESTAMP,  
    is\_active BOOLEAN DEFAULT true,  
    CONSTRAINT unique\_oauth UNIQUE (oauth\_provider, oauth\_id)  
);

CREATE INDEX idx\_users\_email ON users(email);  
CREATE INDEX idx\_users\_created\_at ON users(created\_at DESC);

*\-- Products Table*  
CREATE TABLE products (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    codecanyon\_id VARCHAR(100) UNIQUE NOT NULL,  
    url TEXT NOT NULL,  
    title VARCHAR(500) NOT NULL,  
    slug VARCHAR(500) NOT NULL,  
    category VARCHAR(100) NOT NULL,  
    subcategory VARCHAR(100),  
    price DECIMAL(10,2),  
    total\_sales INTEGER DEFAULT 0,  
    rating DECIMAL(3,2),  
    review\_count INTEGER DEFAULT 0,  
    launch\_date DATE,  
    last\_update\_date DATE,  
    author\_name VARCHAR(200),  
    author\_id VARCHAR(100),  
    technologies JSONB DEFAULT '\[\]',  
    features JSONB DEFAULT '\[\]',  
    description TEXT,  
    screenshots JSONB DEFAULT '\[\]',  
    profitability\_score DECIMAL(5,2),  
    sales\_velocity DECIMAL(10,2),  
    revenue\_potential DECIMAL(12,2),  
    market\_saturation DECIMAL(5,2),  
    scraped\_at TIMESTAMP,  
    created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    updated\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    metadata JSONB DEFAULT '{}'  
);

CREATE INDEX idx\_products\_codecanyon\_id ON products(codecanyon\_id);  
CREATE INDEX idx\_products\_category ON products(category);  
CREATE INDEX idx\_products\_score ON products(profitability\_score DESC NULLS LAST);  
CREATE INDEX idx\_products\_created\_at ON products(created\_at DESC);  
CREATE INDEX idx\_products\_sales ON products(total\_sales DESC);  
CREATE INDEX idx\_products\_title\_fts ON products USING gin(to\_tsvector('english', title));

*\-- Search History Table*  
CREATE TABLE search\_history (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    user\_id UUID REFERENCES users(id) ON DELETE SET NULL,  
    query\_text TEXT,  
    filters JSONB DEFAULT '{}',  
    results\_count INTEGER,  
    searched\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    session\_id VARCHAR(100)  
);

CREATE INDEX idx\_search\_history\_user\_id ON search\_history(user\_id);  
CREATE INDEX idx\_search\_history\_searched\_at ON search\_history(searched\_at DESC);

*\-- Analysis Results Table*  
CREATE TABLE analysis\_results (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    product\_id UUID REFERENCES products(id) ON DELETE CASCADE,  
    profitability\_score DECIMAL(5,2) NOT NULL,  
    score\_breakdown JSONB NOT NULL,  
    trend\_analysis JSONB,  
    competition\_data JSONB,  
    feature\_gaps JSONB,  
    ai\_recommendations TEXT,  
    calculated\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    version INTEGER DEFAULT 1  
);

CREATE INDEX idx\_analysis\_product\_id ON analysis\_results(product\_id);  
CREATE INDEX idx\_analysis\_calculated\_at ON analysis\_results(calculated\_at DESC);

*\-- Market Trends Table*  
CREATE TABLE market\_trends (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    category VARCHAR(100) NOT NULL,  
    subcategory VARCHAR(100),  
    time\_period DATE NOT NULL,  
    average\_sales DECIMAL(10,2),  
    average\_price DECIMAL(10,2),  
    product\_count INTEGER,  
    trending\_technologies JSONB DEFAULT '\[\]',  
    search\_volume INTEGER,  
    created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP  
);

CREATE INDEX idx\_trends\_category ON market\_trends(category);  
CREATE INDEX idx\_trends\_time\_period ON market\_trends(time\_period DESC);

*\-- User Projects Table*  
CREATE TABLE user\_projects (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    user\_id UUID REFERENCES users(id) ON DELETE CASCADE,  
    inspired\_by\_product\_id UUID REFERENCES products(id) ON DELETE SET NULL,  
    project\_name VARCHAR(300) NOT NULL,  
    description TEXT,  
    target\_category VARCHAR(100),  
    planned\_features JSONB DEFAULT '\[\]',  
    tech\_stack JSONB DEFAULT '{}',  
    development\_stage VARCHAR(50) DEFAULT 'concept' CHECK (development\_stage IN ('concept', 'planning', 'development', 'testing', 'launched')),  
    pricing\_strategy JSONB,  
    marketing\_angle TEXT,  
    created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    updated\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP  
);

CREATE INDEX idx\_projects\_user\_id ON user\_projects(user\_id);  
CREATE INDEX idx\_projects\_stage ON user\_projects(development\_stage);

*\-- Feature Insights Table*  
CREATE TABLE feature\_insights (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    category VARCHAR(100) NOT NULL,  
    feature\_name VARCHAR(200) NOT NULL,  
    occurrence\_count INTEGER DEFAULT 0,  
    products\_with\_feature JSONB DEFAULT '\[\]',  
    average\_rating\_with\_feature DECIMAL(3,2),  
    average\_sales\_with\_feature DECIMAL(10,2),  
    sentiment\_score DECIMAL(3,2),  
    last\_analyzed TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    CONSTRAINT unique\_category\_feature UNIQUE (category, feature\_name)  
);

CREATE INDEX idx\_feature\_insights\_category ON feature\_insights(category);

*\-- Scraping Jobs Table*  
CREATE TABLE scraping\_jobs (  
    id UUID PRIMARY KEY DEFAULT uuid\_generate\_v4(),  
    url TEXT NOT NULL,  
    status VARCHAR(50) DEFAULT 'pending' CHECK (status IN ('pending', 'processing', 'completed', 'failed')),  
    user\_id UUID REFERENCES users(id) ON DELETE SET NULL,  
    result\_product\_id UUID REFERENCES products(id) ON DELETE SET NULL,  
    error\_message TEXT,  
    created\_at TIMESTAMP DEFAULT CURRENT\_TIMESTAMP,  
    completed\_at TIMESTAMP  
);

CREATE INDEX idx\_scraping\_jobs\_status ON scraping\_jobs(status);

CREATE INDEX idx\_scraping\_jobs\_user\_id ON scraping\_jobs(user\_id);

---

## **🔧 Configuration Files**

### **requirements.txt**

txt  
\# Core Framework  
Flask==3.0.0  
Flask-SQLAlchemy==3.1.1  
Flask-Migrate==4.0.5  
Flask-Login==0.6.3  
Flask-WTF==1.2.1

\# Database  
psycopg2-binary==2.9.9  
redis==5.0.1

\# Background Tasks  
celery==5.3.4  
celery\[redis\]==5.3.4

\# Web Scraping  
beautifulsoup4==4.12.2  
playwright==1.40.0  
requests==2.31.0  
lxml==4.9.3

\# AI & APIs  
anthropic==0.8.1  
google-api-python-client==2.108.0

\# Security  
python-dotenv==1.0.0  
bcrypt==4.1.2  
PyJWT==2.8.0

\# Validation  
email-validator==2.1.0  
python-slugify==8.0.1

\# Utilities  
python-dateutil==2.8.2  
pytz==2023.3

\# Development  
pytest==7.4.3  
pytest-cov==4.1.0  
black==23.12.0  
flake8==6.1.0

\# Production

gunicorn==21.2.0

### **.env.example**

bash  
*\# Flask Configuration*  
FLASK\_APP=run.py  
FLASK\_ENV=development  
SECRET\_KEY=your-secret-key-change-this-in-production

*\# Database*  
DATABASE\_URL=postgresql://username:password@localhost:5432/codecanyon\_intelligence  
REDIS\_URL=redis://localhost:6379/0

*\# Celery*  
CELERY\_BROKER\_URL=redis://localhost:6379/1  
CELERY\_RESULT\_BACKEND=redis://localhost:6379/2

*\# Claude API*  
CLAUDE\_API\_KEY=sk-ant-your-api-key-here

*\# Google Custom Search*  
GOOGLE\_SEARCH\_API\_KEY=your-google-api-key  
GOOGLE\_SEARCH\_ENGINE\_ID=your-search-engine-id

*\# OAuth (Google)*  
GOOGLE\_OAUTH\_CLIENT\_ID=your-client-id.apps.googleusercontent.com  
GOOGLE\_OAUTH\_CLIENT\_SECRET=your-client-secret

*\# Scraping*  
SCRAPER\_API\_KEY=your-scraper-api-key-optional  
PROXY\_URL=http://proxy:port-optional

*\# Application*  
APP\_URL=http://localhost:5000  
ALLOWED\_HOSTS=localhost,127.0.0.1

*\# Email (Optional \- for notifications)*  
SMTP\_HOST=smtp.gmail.com  
SMTP\_PORT=587  
SMTP\_USER=your-email@gmail.com  
SMTP\_PASSWORD=your-app-password

*\# Rate Limiting*  
RATE\_LIMIT\_ENABLED=true  
FREE\_TIER\_DAILY\_ANALYSES=10  
PRO\_TIER\_DAILY\_ANALYSES=100

*\# Feature Flags*  
ENABLE\_AI\_RECOMMENDATIONS=true

ENABLE\_GOOGLE\_SEARCH=true

### **config.py**

python  
import os  
from datetime import timedelta  
from dotenv import load\_load\_dotenv()

basedir \= os.path.abspath(os.path.dirname(\_\_file\_\_))

class Config:  
    """Base configuration"""  
      
    *\# Flask*  
    SECRET\_KEY \= os.getenv('SECRET\_KEY', 'dev-secret-key-change-this')  
      
    *\# Database*  
    SQLALCHEMY\_DATABASE\_URI \= os.getenv('DATABASE\_URL')  
    SQLALCHEMY\_TRACK\_MODIFICATIONS \= False  
    SQLALCHEMY\_ENGINE\_OPTIONS \= {  
        'pool\_size': 10,  
        'pool\_recycle': 3600,  
        'pool\_pre\_ping': True  
    }  
      
    *\# Redis*  
    REDIS\_URL \= os.getenv('REDIS\_URL', 'redis://localhost:6379/0')  
      
    *\# Celery*  
    CELERY\_BROKER\_URL \= os.getenv('CELERY\_BROKER\_URL', 'redis://localhost:6379/1')  
    CELERY\_RESULT\_BACKEND \= os.getenv('CELERY\_RESULT\_BACKEND', 'redis://localhost:6379/2')  
      
    *\# Session*  
    SESSION\_TYPE \= 'redis'  
    SESSION\_PERMANENT \= True  
    PERMANENT\_SESSION\_LIFETIME \= timedelta(days\=7)  
    SESSION\_COOKIE\_SECURE \= False  *\# Set True in production with HTTPS*  
    SESSION\_COOKIE\_HTTPONLY \= True  
    SESSION\_COOKIE\_SAMESITE \= 'Lax'  
      
    *\# API Keys*  
    CLAUDE\_API\_KEY \= os.getenv('CLAUDE\_API\_KEY')  
    GOOGLE\_SEARCH\_API\_KEY \= os.getenv('GOOGLE\_SEARCH\_API\_KEY')  
    GOOGLE\_SEARCH\_ENGINE\_ID \= os.getenv('GOOGLE\_SEARCH\_ENGINE\_ID')  
      
    *\# OAuth*  
    GOOGLE\_OAUTH\_CLIENT\_ID \= os.getenv('GOOGLE\_OAUTH\_CLIENT\_ID')  
    GOOGLE\_OAUTH\_CLIENT\_SECRET \= os.getenv('GOOGLE\_OAUTH\_CLIENT\_SECRET')  
      
    *\# Rate Limiting*  
    RATE\_LIMIT\_ENABLED \= os.getenv('RATE\_LIMIT\_ENABLED', 'true').lower() \== 'true'  
      
    *\# Tier Limits*  
    TIER\_LIMITS \= {  
        'free': {  
            'daily\_analyses': 10,  
            'daily\_scrapes': 5,  
            'weekly\_ai\_recommendations': 3,  
            'max\_projects': 1  
        },  
        'pro': {  
            'daily\_analyses': 100,  
            'daily\_scrapes': 50,  
            'weekly\_ai\_recommendations': 30,  
            'max\_projects': \-1  *\# Unlimited*  
        },  
        'enterprise': {  
            'daily\_analyses': \-1,  *\# Unlimited*  
            'daily\_scrapes': \-1,  
            'weekly\_ai\_recommendations': \-1,  
            'max\_projects': \-1  
        }  
    }  
      
    *\# Scraping*  
    SCRAPER\_API\_KEY \= os.getenv('SCRAPER\_API\_KEY')  
    SCRAPING\_DELAY \= 2  *\# Seconds between requests*  
    SCRAPING\_TIMEOUT \= 30  *\# Seconds*  
    MAX\_RETRIES \= 3  
      
    *\# Cache TTL (seconds)*  
    CACHE\_TTL \= {  
        'analysis': 86400,  *\# 24 hours*  
        'search': 300,  *\# 5 minutes*  
        'trends': 3600,  *\# 1 hour*  
        'product': 7200  *\# 2 hours*  
    }

class DevelopmentConfig(Config):  
    """Development configuration"""  
    DEBUG \= True  
    TESTING \= False

class ProductionConfig(Config):  
    """Production configuration"""  
    DEBUG \= False  
    TESTING \= False  
    SESSION\_COOKIE\_SECURE \= True

class TestingConfig(Config):  
    """Testing configuration"""  
    TESTING \= True  
    SQLALCHEMY\_DATABASE\_URI \= 'postgresql://localhost/codecanyon\_test'

config \= {  
    'development': DevelopmentConfig,  
    'production': ProductionConfig,  
    'testing': TestingConfig,  
    'default': DevelopmentConfig

}

---

## **🎨 HTMX Implementation Patterns**

### **Core HTMX Configuration**

#### **static/js/app.js**

javascript  
*// HTMX Configuration*  
document.addEventListener('DOMContentLoaded', function() {  
      
    *// Configure HTMX*  
    htmx.config.defaultSwapStyle \= 'innerHTML';  
    htmx.config.timeout \= 30000; *// 30 seconds*  
      
    *// CSRF Token for all requests*  
    document.body.addEventListener('htmx:configRequest', (event) \=\> {  
        const csrfToken \= document.querySelector('meta\[name="csrf-token"\]')?.content;  
        if (csrfToken) {  
            event.detail.headers\['X-CSRFToken'\] \= csrfToken;  
        }  
    });  
      
    *// Global loading indicator*  
    document.body.addEventListener('htmx:beforeRequest', (event) \=\> {  
        document.getElementById('global-loader')?.classList.remove('hidden');  
    });  
      
    document.body.addEventListener('htmx:afterRequest', (event) \=\> {  
        document.getElementById('global-loader')?.classList.add('hidden');  
    });  
      
    *// Toast notifications*  
    document.body.addEventListener('showToast', (event) \=\> {  
        const { message, type } \= event.detail;  
        showToast(message, type);  
    });  
      
    *// Error handling*  
    document.body.addEventListener('htmx:responseError', (event) \=\> {  
        const status \= event.detail.xhr.status;  
        if (status \=== 429) {  
            showToast('Rate limit exceeded. Please try again later.', 'error');  
        } else if (status \=== 401) {  
            window.location.href \= '/auth/login';  
        } else {  
            showToast('An error occurred. Please try again.', 'error');  
        }  
    });  
});

*// Toast notification function*  
function showToast(message, type \= 'info') {  
    const toast \= document.createElement('div');  
    toast.className \= \`toast toast-${type} fixed top-4 right-4 p-4 rounded shadow-lg transition-opacity duration-300\`;  
    toast.textContent \= message;  
      
    document.body.appendChild(toast);  
      
    setTimeout(() \=\> {  
        toast.style.opacity \= '0';  
        setTimeout(() \=\> toast.remove(), 300);  
    }, 3000);

}

---

## **📝 Key Route Implementations**

### **Agent Instructions for Each Route**

---

### **1\. PRODUCT SEARCH ROUTE**

**File**: `app/routes/search.py`

**Agent Task**: Implement product search with HTMX partial rendering

**Requirements**:

python  
@bp.route('/search', methods\=\['GET'\])  
def search\_products():  
    """  
    Handle product search with filters  
      
    Query Parameters:  
    \- q: Search query text  
    \- category: Category filter  
    \- min\_price, max\_price: Price range  
    \- min\_rating: Minimum rating  
    \- min\_sales: Minimum sales  
    \- sort: Sort field (sales, rating, price, score)  
    \- order: Sort order (asc, desc)  
    \- page: Page number  
      
    Returns:  
    \- Full page HTML if not HTMX request  
    \- Partial HTML (product grid \+ pagination) if HTMX request

    """

**Implementation Steps**:

1. Extract query parameters  
2. Build SQLAlchemy query with filters  
3. Apply sorting  
4. Paginate results (20 per page)  
5. Check if HTMX request (`request.headers.get('HX-Request')`)  
6. Render appropriate template:  
   * Full page: `pages/search.html`  
   * Partial: `components/product_grid.html`

**Template Structure** (`templates/components/product_grid.html`):

html  
*\<\!-- Product cards \--\>*  
\<div class\="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id\="product-grid"\>  
    {% for product in products %}  
        {% include 'components/product\_card.html' %}  
    {% endfor %}  
\</div\>

*\<\!-- Pagination \--\>*  
\<div class\="mt-8"\>  
    {% include 'components/pagination.html' %}

\</div\>

**HTMX Attributes** (in search form):

html  
\<form hx-get\="/search"   
      hx-target\="\#search-results"   
      hx-trigger\="submit, keyup delay:500ms from:\#search-input"  
      hx-indicator\="\#search-loader"  
      hx-push-url\="true"\>  
      
    \<input type\="text"   
           name\="q"   
           id\="search-input"  
           placeholder\="Search products..."  
           class\="w-full px-4 py-2 border rounded"\>  
      
    *\<\!-- Filters \--\>*  
    \<select name\="category"   
            hx-get\="/search"   
            hx-include\="closest form"  
            hx-target\="\#search-results"\>  
        \<option value\=""\>All Categories\</option\>  
        *\<\!-- Options populated from database \--\>*  
    \</select\>  
\</form\>

\<div id\="search-results"\>  
    *\<\!-- Results rendered here \--\>*

\</div\>

---

### **2\. URL SCRAPING ROUTE**

**File**: `app/routes/scrape.py`

**Agent Task**: Implement asynchronous URL scraping with progress updates

**Requirements**:

python  
@bp.route('/scrape', methods\=\['POST'\])  
@login\_required  
@rate\_limit\_check('daily\_scrapes')  
def scrape\_url():  
    """  
    Initiate product scraping from CodeCanyon URL  
      
    Form Data:  
    \- url: CodeCanyon product URL  
      
    Process:  
    1\. Validate URL format  
    2\. Check if product already exists  
    3\. Create scraping job  
    4\. Queue Celery task  
    5\. Return job ID and status endpoint  
      
    Returns:  
    \- HTML with job status container  
    \- Includes polling HTMX attribute

    """

**Implementation Steps**:

1. Validate CodeCanyon URL pattern  
2. Check database for existing product (by codecanyon\_id)  
3. If exists, return cached product  
4. If new, create `scraping_jobs` record  
5. Trigger Celery task: `tasks.scraping.scrape_product_task.delay(url, job_id)`  
6. Return status template with polling

**Celery Task** (`app/tasks/scraping.py`):

python  
@celery.task(bind\=True)  
def scrape\_product\_task(self, url, job\_id):  
    """  
    Background task to scrape CodeCanyon product  
      
    Steps:  
    1\. Update job status to 'processing'  
    2\. Fetch page with Playwright/BeautifulSoup  
    3\. Extract product data  
    4\. Save to products table  
    5\. Update job status to 'completed'  
    6\. Calculate initial profitability score  
    """  
    try:  
        *\# Update status*  
        update\_job\_status(job\_id, 'processing')  
          
        *\# Scrape*  
        scraper \= CodeCanyonScraper()  
        product\_data \= scraper.scrape(url)  
          
        *\# Save*  
        product \= Product(\*\*product\_data)  
        db.session.add(product)  
        db.session.commit()  
          
        *\# Update job*  
        update\_job\_status(job\_id, 'completed', product.id)  
          
        *\# Trigger analysis*  
        calculate\_profitability.delay(product.id)  
          
        return product.id  
          
    except Exception as e:  
        update\_job\_status(job\_id, 'failed', error\=str(e))

        raise

**Status Polling Template**:

html  
\<div hx-get\="/scrape/status/{{ job\_id }}"  
     hx-trigger\="every 2s"  
     hx-swap\="outerHTML"\>  
      
    \<div class\="flex items-center space-x-2"\>  
        \<div class\="spinner"\>\</div\>  
        \<span\>Scraping product... {{ progress }}%\</span\>  
    \</div\>

\</div\>

**Status Endpoint**:

python  
@bp.route('/scrape/status/\<job\_id\>')  
def scraping\_status(job\_id):  
    """Return current scraping job status"""  
    job \= ScrapingJob.query.get(job\_id)  
      
    if job.status \== 'completed':  
        *\# Return product card*  
        product \= Product.query.get(job.result\_product\_id)  
        return render\_template('components/product\_card.html', product\=product)  
      
    elif job.status \== 'failed':  
        return render\_template('components/error\_message.html', error\=job.error\_message)  
      
    else:  
        *\# Return progress indicator*

        return render\_template('components/scraping\_progress.html', job\=job)

---

### **3\. PROFITABILITY ANALYSIS ROUTE**

**File**: `app/routes/analyze.py`

**Agent Task**: Calculate and display profitability analysis

**Requirements**:

python  
@bp.route('/analyze/\<product\_id\>', methods\=\['GET'\])  
@login\_required  
@rate\_limit\_check('daily\_analyses')  
def analyze\_product(product\_id):  
    """  
    Generate profitability analysis for a product  
      
    Process:  
    1\. Check cache for existing analysis  
    2\. If cached and recent (\< 24h), return cached  
    3\. If not, calculate new analysis  
    4\. Render analysis panel  
      
    Returns:  
    \- HTML analysis panel with charts and metrics

    """

**Implementation** (`app/services/analyzer.py`):

python  
class ProfitabilityAnalyzer:  
    """Calculate profitability scores"""  
      
    def analyze(self, product\_id):  
        """Main analysis method"""  
          
        *\# Check cache*  
        cached \= self.get\_cached\_analysis(product\_id)  
        if cached:  
            return cached  
          
        product \= Product.query.get(product\_id)  
          
        *\# Calculate metrics*  
        metrics \= {  
            'sales\_velocity': self.calculate\_sales\_velocity(product),  
            'revenue\_potential': self.calculate\_revenue\_potential(product),  
            'market\_saturation': self.calculate\_market\_saturation(product),  
            'update\_frequency': self.calculate\_update\_frequency(product),  
            'rating\_quality': self.calculate\_rating\_quality(product)  
        }  
          
        *\# Calculate weighted score*  
        score \= self.calculate\_weighted\_score(metrics)  
          
        *\# Get trend data*  
        trends \= self.get\_trend\_analysis(product)  
          
        *\# Get competition data*  
        competition \= self.get\_competition\_data(product)  
          
        *\# Save result*  
        result \= {  
            'product\_id': product\_id,  
            'profitability\_score': score\['total'\],  
            'score\_breakdown': metrics,  
            'trend\_analysis': trends,  
            'competition\_data': competition  
        }  
          
        *\# Cache and save*  
        self.cache\_analysis(product\_id, result)  
        self.save\_to\_database(result)  
          
        return result  
      
    def calculate\_sales\_velocity(self, product):  
        """(Total Sales / Days Since Launch) × 100"""  
        days \= (datetime.now().date() \- product.launch\_date).days  
        if days \== 0:  
            return 0  
        return (product.total\_sales / days) \* 100  
      
    def calculate\_revenue\_potential(self, product):  
        """Price × Average Monthly Sales"""  
        days \= (datetime.now().date() \- product.launch\_date).days  
        if days \== 0:  
            return 0

        monthly\_sales \= (product.total\_

Continue

5:33 PM

sales / days) \* 30 return product.price \* monthly\_sales

def calculate\_market\_saturation(self, product):  
    """100 / Number of Similar Products"""  
    similar\_count \= Product.query.filter\_by(  
        category=product.category  
    ).count()  
    return 100 / similar\_count if similar\_count \> 0 else 100

def calculate\_update\_frequency(self, product):  
    """(Updates in Last 12 Months / 12\) × 100"""  
    \# This requires tracking update history  
    \# For now, estimate based on last\_update\_date  
    months\_since\_update \= (datetime.now().date() \- product.last\_update\_date).days / 30  
    if months\_since\_update \< 1:  
        return 100  
    elif months\_since\_update \< 6:  
        return 60  
    else:  
        return 20

def calculate\_rating\_quality(self, product):  
    """(Rating / 5\) × 100 × Review Count Weight"""  
    import math  
    review\_weight \= min(1, math.log10(product.review\_count \+ 1\) / 3\)  
    return (product.rating / 5\) \* 100 \* (0.5 \+ 0.5 \* review\_weight)

def calculate\_weighted\_score(self, metrics):  
    """Apply weights and return total score"""  
    weights \= {  
        'sales\_velocity': 0.30,  
        'revenue\_potential': 0.25,  
        'market\_saturation': 0.20,  
        'update\_frequency': 0.15,  
        'rating\_quality': 0.10  
    }  
      
    \# Normalize revenue\_potential (scale 0-100)  
    normalized \= metrics.copy()  
    normalized\['sales\_velocity'\] \= min(100, metrics\['sales\_velocity'\])  
    normalized\['revenue\_potential'\] \= min(100, (metrics\['revenue\_potential'\] / 1000\) \* 10\)  
      
    total \= sum(normalized\[k\] \* weights\[k\] for k in weights)  
      
    return {  
        'total': round(total, 2),  
        'breakdown': normalized,  
        'weights': weights

    }

\*\*Template\*\* (\`templates/components/analysis\_panel.html\`):  
\`\`\`html  
\<div class="bg-white rounded-lg shadow-lg p-6"\>  
    \<\!-- Score Gauge \--\>  
    \<div class="text-center mb-8"\>  
        \<div class="text-6xl font-bold text-blue-600"\>  
            {{ analysis.profitability\_score }}  
        \</div\>  
        \<div class="text-gray-600"\>Profitability Score\</div\>  
        \<div class="mt-2"\>  
            {% if analysis.profitability\_score \>= 80 %}  
                \<span class="px-3 py-1 bg-green-100 text-green-800 rounded-full"\>Excellent\</span\>  
            {% elif analysis.profitability\_score \>= 60 %}  
                \<span class="px-3 py-1 bg-yellow-100 text-yellow-800 rounded-full"\>Good\</span\>  
            {% else %}  
                \<span class="px-3 py-1 bg-red-100 text-red-800 rounded-full"\>Poor\</span\>  
            {% endif %}  
        \</div\>  
    \</div\>  
      
    \<\!-- Metric Breakdown \--\>  
    \<div class="grid grid-cols-2 gap-4 mb-8"\>  
        \<div class="metric-card"\>  
            \<div class="text-sm text-gray-600"\>Sales Velocity\</div\>  
            \<div class="text-2xl font-bold"\>{{ analysis.score\_breakdown.sales\_velocity|round(1) }}\</div\>  
        \</div\>  
        \<div class="metric-card"\>  
            \<div class="text-sm text-gray-600"\>Revenue Potential\</div\>  
            \<div class="text-2xl font-bold"\>${{ analysis.score\_breakdown.revenue\_potential|round(0) }}\</div\>  
        \</div\>  
        \<div class="metric-card"\>  
            \<div class="text-sm text-gray-600"\>Market Saturation\</div\>  
            \<div class="text-2xl font-bold"\>{{ analysis.score\_breakdown.market\_saturation|round(1) }}%\</div\>  
        \</div\>  
        \<div class="metric-card"\>  
            \<div class="text-sm text-gray-600"\>Rating Quality\</div\>  
            \<div class="text-2xl font-bold"\>{{ analysis.score\_breakdown.rating\_quality|round(1) }}\</div\>  
        \</div\>  
    \</div\>  
      
    \<\!-- Chart \--\>  
    \<div class="mb-8"\>  
        \<canvas id="breakdown-chart" data-metrics='{{ analysis.score\_breakdown|tojson }}'\>\</canvas\>  
    \</div\>  
      
    \<\!-- Actions \--\>  
    \<div class="flex space-x-4"\>  
        \<button hx-post="/recommendations/{{ product.id }}"  
                hx-target="\#ai-recommendations"  
                class="btn btn-primary"\>  
            Get AI Recommendations  
        \</button\>  
        \<button hx-post="/planner/create"  
                hx-vals='{"product\_id": "{{ product.id }}"}'  
                class="btn btn-secondary"\>  
            Create Project Plan  
        \</button\>  
    \</div\>  
\</div\>

\<script\>  
    // Render Chart.js radar chart  
    const ctx \= document.getElementById('breakdown-chart').getContext('2d');  
    const metrics \= JSON.parse(ctx.canvas.dataset.metrics);  
      
    new Chart(ctx, {  
        type: 'radar',  
        data: {  
            labels: \['Sales Velocity', 'Revenue Potential', 'Market Saturation', 'Update Frequency', 'Rating Quality'\],  
            datasets: \[{  
                label: 'Score Breakdown',  
                data: \[  
                    metrics.sales\_velocity,  
                    metrics.revenue\_potential,  
                    metrics.market\_saturation,  
                    metrics.update\_frequency,  
                    metrics.rating\_quality  
                \],  
                backgroundColor: 'rgba(59, 130, 246, 0.2)',  
                borderColor: 'rgb(59, 130, 246)',  
                borderWidth: 2  
            }\]  
        },  
        options: {  
            scales: {  
                r: {  
                    beginAtZero: true,  
                    max: 100  
                }  
            }  
        }  
    });  
\</script\>  
\`\`\`

\---

\#\#\# 4\. AI RECOMMENDATIONS ROUTE

\*\*File\*\*: \`app/routes/recommendations.py\`

\*\*Agent Task\*\*: Generate AI-powered recommendations using Claude API

\*\*Requirements\*\*:  
\`\`\`python  
@bp.route('/recommendations/\<product\_id\>', methods=\['POST'\])  
@login\_required  
@rate\_limit\_check('weekly\_ai\_recommendations')  
def generate\_recommendations(product\_id):  
    """  
    Generate AI recommendations using Claude API  
      
    Process:  
    1\. Gather product context (features, competitors, reviews)  
    2\. Call Claude API with structured prompt  
    3\. Parse response  
    4\. Render recommendations  
      
    Returns:  
    \- HTML with feature gaps, tech suggestions, pricing strategy  
    """  
\`\`\`

\*\*Implementation\*\* (\`app/services/ai\_service.py\`):  
\`\`\`python  
from anthropic import Anthropic

class AIRecommendationService:  
    """Generate AI-powered recommendations"""  
      
    def \_\_init\_\_(self):  
        self.client \= Anthropic(api\_key=current\_app.config\['CLAUDE\_API\_KEY'\])  
      
    def generate\_recommendations(self, product\_id):  
        """Main recommendation generation"""  
          
        \# Prepare context  
        context \= self.prepare\_context(product\_id)  
          
        \# Build prompt  
        prompt \= self.build\_prompt(context)  
          
        \# Call Claude API  
        response \= self.client.messages.create(  
            model="claude-sonnet-4-5",  
            max\_tokens=2000,  
            messages=\[  
                {"role": "user", "content": prompt}  
            \]  
        )  
          
        \# Parse response  
        recommendations \= self.parse\_response(response.content\[0\].text)  
          
        \# Cache result  
        self.cache\_recommendations(product\_id, recommendations)  
          
        return recommendations  
      
    def prepare\_context(self, product\_id):  
        """Gather all context needed for AI"""  
        product \= Product.query.get(product\_id)  
          
        \# Get competitors  
        competitors \= Product.query.filter(  
            Product.category \== product.category,  
            Product.id \!= product.id  
        ).order\_by(Product.total\_sales.desc()).limit(5).all()  
          
        \# Get analysis  
        analysis \= AnalysisResult.query.filter\_by(  
            product\_id=product\_id  
        ).order\_by(AnalysisResult.calculated\_at.desc()).first()  
          
        \# Get market trends  
        trends \= MarketTrend.query.filter\_by(  
            category=product.category  
        ).order\_by(MarketTrend.time\_period.desc()).first()  
          
        return {  
            'product': product,  
            'competitors': competitors,  
            'analysis': analysis,  
            'trends': trends  
        }  
      
    def build\_prompt(self, context):  
        """Build structured prompt for Claude"""  
          
        product \= context\['product'\]  
        competitors \= context\['competitors'\]  
          
        competitor\_list \= "\\n".join(\[  
            f"- {c.title}: {c.total\_sales} sales, ${c.price}, {c.rating}★"  
            for c in competitors  
        \])  
          
        prompt \= f"""  
Analyze this CodeCanyon product and provide strategic recommendations for creating a competitive alternative:

PRODUCT DETAILS:  
\- Name: {product.title}  
\- Category: {product.category}  
\- Price: ${product.price}  
\- Sales: {product.total\_sales}  
\- Rating: {product.rating}★ ({product.review\_count} reviews)  
\- Technologies: {', '.join(product.technologies or \[\])}

TOP COMPETITORS:  
{competitor\_list}

PROFITABILITY SCORE: {context\['analysis'\].profitability\_score if context\['analysis'\] else 'N/A'}

Please provide:

1\. FEATURE GAPS (5 items):  
   List the top 5 features that competitors have but this product lacks, or innovative features that could differentiate a new product.

2\. TECHNOLOGY RECOMMENDATIONS:  
   Suggest modern technology stack improvements and why they would provide competitive advantages.

3\. PRICING STRATEGY:  
   Recommend optimal pricing based on market analysis and feature set.

4\. UNIQUE SELLING PROPOSITIONS (3 items):  
   Suggest 3 unique angles that would make a competitive product stand out.

5\. DEVELOPMENT EFFORT:  
   Estimate the development complexity (Low/Medium/High) and rough timeline.

Format your response as JSON:  
{{  
  "feature\_gaps": \[  
    {{"name": "...", "description": "...", "impact": "high|medium|low"}}  
  \],  
  "tech\_recommendations": {{  
    "frontend": "...",  
    "backend": "...",  
    "database": "...",  
    "rationale": "..."  
  }},  
  "pricing\_strategy": {{  
    "recommended\_price": 0,  
    "reasoning": "...",  
    "pricing\_tiers": \[...\]  
  }},  
  "unique\_selling\_propositions": \["...", "...", "..."\],  
  "development\_effort": {{  
    "complexity": "low|medium|high",  
    "estimated\_timeline": "...",  
    "key\_challenges": \["..."\]  
  }}  
}}  
"""  
        return prompt  
      
    def parse\_response(self, response\_text):  
        """Parse Claude's JSON response"""  
        import json  
        import re  
          
        \# Extract JSON from response (handle markdown code blocks)  
        json\_match \= re.search(r'\`\`\`json\\n(.\*?)\\n\`\`\`', response\_text, re.DOTALL)  
        if json\_match:  
            json\_str \= json\_match.group(1)  
        else:  
            json\_str \= response\_text  
          
        try:  
            return json.loads(json\_str)  
        except json.JSONDecodeError:  
            \# Fallback: return raw text  
            return {'raw\_response': response\_text}  
\`\`\`

\*\*Template\*\* (\`templates/components/ai\_recommendations.html\`):  
\`\`\`html  
\<div class="space-y-6"\>  
    \<\!-- Feature Gaps \--\>  
    \<div class="card"\>  
        \<h3 class="text-xl font-bold mb-4"\>🎯 Feature Gaps & Opportunities\</h3\>  
        \<div class="space-y-3"\>  
            {% for feature in recommendations.feature\_gaps %}  
            \<div class="p-4 border rounded-lg"\>  
                \<div class="flex items-start justify-between"\>  
                    \<div class="flex-1"\>  
                        \<h4 class="font-semibold"\>{{ feature.name }}\</h4\>  
                        \<p class="text-gray-600 text-sm mt-1"\>{{ feature.description }}\</p\>  
                    \</div\>  
                    \<span class="badge badge-{{ 'success' if feature.impact \== 'high' else 'warning' if feature.impact \== 'medium' else 'secondary' }}"\>  
                        {{ feature.impact }} impact  
                    \</span\>  
                \</div\>  
            \</div\>  
            {% endfor %}  
        \</div\>  
    \</div\>  
      
    \<\!-- Tech Stack \--\>  
    \<div class="card"\>  
        \<h3 class="text-xl font-bold mb-4"\>💻 Technology Recommendations\</h3\>  
        \<div class="grid grid-cols-3 gap-4 mb-4"\>  
            \<div\>  
                \<div class="text-sm text-gray-600"\>Frontend\</div\>  
                \<div class="font-semibold"\>{{ recommendations.tech\_recommendations.frontend }}\</div\>  
            \</div\>  
            \<div\>  
                \<div class="text-sm text-gray-600"\>Backend\</div\>  
                \<div class="font-semibold"\>{{ recommendations.tech\_recommendations.backend }}\</div\>  
            \</div\>  
            \<div\>  
                \<div class="text-sm text-gray-600"\>Database\</div\>  
                \<div class="font-semibold"\>{{ recommendations.tech\_recommendations.database }}\</div\>  
            \</div\>  
        \</div\>  
        \<p class="text-gray-700"\>{{ recommendations.tech\_recommendations.rationale }}\</p\>  
    \</div\>  
      
    \<\!-- Pricing Strategy \--\>  
    \<div class="card"\>  
        \<h3 class="text-xl font-bold mb-4"\>💰 Pricing Strategy\</h3\>  
        \<div class="text-4xl font-bold text-green-600 mb-2"\>  
            ${{ recommendations.pricing\_strategy.recommended\_price }}  
        \</div\>  
        \<p class="text-gray-700 mb-4"\>{{ recommendations.pricing\_strategy.reasoning }}\</p\>  
        {% if recommendations.pricing\_strategy.pricing\_tiers %}  
        \<div class="flex space-x-4"\>  
            {% for tier in recommendations.pricing\_strategy.pricing\_tiers %}  
            \<div class="flex-1 border rounded-lg p-3 text-center"\>  
                \<div class="text-sm text-gray-600"\>{{ tier.name }}\</div\>  
                \<div class="text-2xl font-bold"\>${{ tier.price }}\</div\>  
            \</div\>  
            {% endfor %}  
        \</div\>  
        {% endif %}  
    \</div\>  
      
    \<\!-- USPs \--\>  
    \<div class="card"\>  
        \<h3 class="text-xl font-bold mb-4"\>⭐ Unique Selling Propositions\</h3\>  
        \<ul class="space-y-2"\>  
            {% for usp in recommendations.unique\_selling\_propositions %}  
            \<li class="flex items-start"\>  
                \<span class="text-blue-600 mr-2"\>✓\</span\>  
                \<span\>{{ usp }}\</span\>  
            \</li\>  
            {% endfor %}  
        \</ul\>  
    \</div\>  
      
    \<\!-- Development Effort \--\>  
    \<div class="card"\>  
        \<h3 class="text-xl font-bold mb-4"\>⏱️ Development Effort\</h3\>  
        \<div class="flex items-center space-x-4 mb-4"\>  
            \<div\>  
                \<span class="text-sm text-gray-600"\>Complexity:\</span\>  
                \<span class="ml-2 px-3 py-1 rounded-full font-semibold  
                    {% if recommendations.development\_effort.complexity \== 'low' %}bg-green-100 text-green-800  
                    {% elif recommendations.development\_effort.complexity \== 'medium' %}bg-yellow-100 text-yellow-800  
                    {% else %}bg-red-100 text-red-800{% endif %}"\>  
                    {{ recommendations.development\_effort.complexity|upper }}  
                \</span\>  
            \</div\>  
            \<div\>  
                \<span class="text-sm text-gray-600"\>Timeline:\</span\>  
                \<span class="ml-2 font-semibold"\>{{ recommendations.development\_effort.estimated\_timeline }}\</span\>  
            \</div\>  
        \</div\>  
        \<div\>  
            \<div class="text-sm font-semibold text-gray-700 mb-2"\>Key Challenges:\</div\>  
            \<ul class="list-disc list-inside space-y-1 text-gray-600"\>  
                {% for challenge in recommendations.development\_effort.key\_challenges %}  
                \<li\>{{ challenge }}\</li\>  
                {% endfor %}  
            \</ul\>  
        \</div\>  
    \</div\>  
      
    \<\!-- Action Button \--\>  
    \<div class="text-center"\>  
        \<button hx-post="/planner/create"  
                hx-vals='{"product\_id": "{{ product\_id }}", "recommendations": {{ recommendations|tojson|safe }}}'  
                hx-target="\#main-content"  
                class="btn btn-primary btn-lg"\>  
            Create Development Plan Based on These Recommendations  
        \</button\>  
    \</div\>  
\</div\>  
\`\`\`

\---

\#\# ⚙️ Critical Implementation Notes for AI Agent

\#\#\# Database Migrations

\*\*Command to create migration\*\*:  
\`\`\`bash  
flask db init  \# First time only  
flask db migrate \-m "Initial schema"  
flask db upgrade  
\`\`\`

\#\#\# Web Scraping Implementation

\*\*File\*\*: \`app/services/scraper.py\`  
\`\`\`python  
from playwright.sync\_api import sync\_playwright  
from bs4 import BeautifulSoup  
import time  
import re

class CodeCanyonScraper:  
    """Scrape CodeCanyon product pages"""  
      
    def scrape(self, url):  
        """  
        Main scraping method  
          
        Returns dict with:  
        \- codecanyon\_id  
        \- title  
        \- category  
        \- price  
        \- total\_sales  
        \- rating  
        \- review\_count  
        \- launch\_date  
        \- last\_update\_date  
        \- author\_name  
        \- technologies  
        \- features  
        \- description  
        \- screenshots  
        """  
          
        with sync\_playwright() as p:  
            browser \= p.chromium.launch(headless=True)  
            page \= browser.new\_page()  
              
            try:  
                \# Load page  
                page.goto(url, wait\_until='networkidle')  
                time.sleep(2)  \# Wait for dynamic content  
                  
                \# Get HTML  
                html \= page.content()  
                soup \= BeautifulSoup(html, 'lxml')  
                  
                \# Extract data  
                data \= {  
                    'codecanyon\_id': self.extract\_codecanyon\_id(url),  
                    'url': url,  
                    'title': self.extract\_title(soup),  
                    'category': self.extract\_category(soup),  
                    'price': self.extract\_price(soup),  
                    'total\_sales': self.extract\_sales(soup),  
                    'rating': self.extract\_rating(soup),  
                    'review\_count': self.extract\_review\_count(soup),  
                    'launch\_date': self.extract\_launch\_date(soup),  
                    'last\_update\_date': self.extract\_last\_update(soup),  
                    'author\_name': self.extract\_author(soup),  
                    'technologies': self.extract\_technologies(soup),  
                    'features': self.extract\_features(soup),  
                    'description': self.extract\_description(soup),  
                    'screenshots': self.extract\_screenshots(soup)  
                }  
                  
                return data  
                  
            finally:  
                browser.close()  
      
    def extract\_codecanyon\_id(self, url):  
        """Extract ID from URL"""  
        match \= re.search(r'/item/\[^/\]+/(\\d+)', url)  
        return match.group(1) if match else None  
      
    def extract\_title(self, soup):  
        """Extract product title"""  
        \# Agent: Find the appropriate selector for CodeCanyon  
        title\_elem \= soup.select\_one('h1.t-heading--xl') \# Example selector  
        return title\_elem.text.strip() if title\_elem else None  
      
    def extract\_price(self, soup):  
        """Extract price"""  
        price\_elem \= soup.select\_one('.js-item-purchase\_\_price')  
        if price\_elem:  
            price\_text \= price\_elem.text.strip()  
            \# Extract number from "$29" format  
            match \= re.search(r'\\$(\\d+(?:\\.\\d{2})?)', price\_text)  
            return float(match.group(1)) if match else None  
        return None  
      
    \# Agent: Implement similar methods for other fields  
    \# Use CSS selectors specific to CodeCanyon's structure  
\`\`\`

\*\*Important for Agent\*\*:  
\- CodeCanyon's HTML structure may change  
\- Use multiple fallback selectors  
\- Handle missing data gracefully  
\- Add proper error logging  
\- Test with multiple product URLs

\---

\#\#\# Rate Limiting Decorator

\*\*File\*\*: \`app/utils/decorators.py\`  
\`\`\`python  
from functools import wraps  
from flask import session, jsonify, render\_template, request  
from app.models import User  
from datetime import date

def rate\_limit\_check(action\_type):  
    """  
    Decorator to check rate limits based on user tier  
      
    Usage:  
    @rate\_limit\_check('daily\_analyses')  
    def analyze\_product():  
        ...  
    """  
    def decorator(f):  
        @wraps(f)  
        def decorated\_function(\*args, \*\*kwargs):  
            user\_id \= session.get('user\_id')  
            if not user\_id:  
                return jsonify({'error': 'Unauthorized'}), 401  
              
            user \= User.query.get(user\_id)  
            tier \= user.subscription\_tier  
            limits \= current\_app.config\['TIER\_LIMITS'\]\[tier\]  
              
            \# Get limit for this action  
            limit\_key \= f"{action\_type}"  
            limit \= limits.get(limit\_key, \-1)  
              
            \# Unlimited tier  
            if limit \== \-1:  
                return f(\*args, \*\*kwargs)  
              
            \# Check usage  
            usage\_key \= f"ratelimit:{user\_id}:{action\_type}:{date.today()}"  
            current\_usage \= redis\_client.get(usage\_key)  
            current\_usage \= int(current\_usage) if current\_usage else 0  
              
            if current\_usage \>= limit:  
                \# Return error (HTMX-friendly)  
                if request.headers.get('HX-Request'):  
                    return render\_template(  
                        'components/rate\_limit\_error.html',  
                        action=action\_type,  
                        limit=limit  
                    ), 429  
                else:  
                    return jsonify({  
                        'error': 'Rate limit exceeded',  
                        'limit': limit  
                    }), 429  
              
            \# Increment usage  
            redis\_client.incr(usage\_key)  
            redis\_client.expire(usage\_key, 86400\)  \# 24 hours  
              
            return f(\*args, \*\*kwargs)  
          
        return decorated\_function  
    return decorator  
\`\`\`

\---

\#\#\# Celery Task Configuration

\*\*File\*\*: \`celery\_worker.py\`  
\`\`\`python  
from app import create\_app, celery

app \= create\_app()  
app.app\_context().push()

if \_\_name\_\_ \== '\_\_main\_\_':  
    celery.start()  
\`\`\`

\*\*Run worker\*\*:  
\`\`\`bash  
celery \-A celery\_worker.celery worker \--loglevel=info  
\`\`\`

\*\*Run beat scheduler\*\* (for periodic tasks):  
\`\`\`bash  
celery \-A celery\_worker.celery beat \--loglevel=info  
\`\`\`

\---

\#\# 🎨 Frontend Component Library

\#\#\# Base Layout Template

\*\*File\*\*: \`templates/layouts/base.html\`  
\`\`\`html  
\<\!DOCTYPE html\>  
\<html lang="en"\>  
\<head\>  
    \<meta charset="UTF-8"\>  
    \<meta name="viewport" content="width=device-width, initial-scale=1.0"\>  
    \<meta name="csrf-token" content="{{ csrf\_token() }}"\>  
    \<title\>{% block title %}CodeCanyon Intelligence{% endblock %}\</title\>  
      
    \<\!-- Tailwind CSS \--\>  
    \<script src="https://cdn.tailwindcss.com"\>\</script\>  
      
    \<\!-- HTMX \--\>  
    \<script src="https://unpkg.com/htmx.org@1.9.10"\>\</script\>  
      
    \<\!-- Alpine.js (optional) \--\>  
    \<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"\>\</script\>  
      
    \<\!-- Chart.js \--\>  
    \<script src="https://cdn.jsdelivr.net/npm/chart.js"\>\</script\>  
      
    \<\!-- Custom CSS \--\>  
    \<link rel="stylesheet" href="{{ url\_for('static', filename='css/custom.css') }}"\>  
\</head\>  
\<body class="bg-gray-50"\>  
    \<\!-- Global Loader \--\>  
    \<div id="global-loader" class="htmx-indicator hidden fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 z-50 flex items-center justify-center"\>  
        \<div class="bg-white p-6 rounded-lg shadow-xl"\>  
            \<div class="spinner"\>\</div\>  
            \<div class="mt-4 text-center"\>Loading...\</div\>  
        \</div\>  
    \</div\>  
      
    \<\!-- Navigation \--\>  
    {% include 'components/navbar.html' %}  
      
    \<\!-- Main Content \--\>  
    \<main class="container mx-auto px-4 py-8" id="main-content"\>  
        {% block content %}{% endblock %}  
    \</main\>  
      
    \<\!-- Footer \--\>  
    \<footer class="bg-gray-800 text-white py-8 mt-16"\>  
        \<div class="container mx-auto px-4 text-center"\>  
            \<p\>\&copy; 2024 CodeCanyon Intelligence. All rights reserved.\</p\>  
        \</div\>  
    \</footer\>  
      
    \<\!-- Custom JS \--\>  
    \<script src="{{ url\_for('static', filename='js/app.js') }}"\>\</script\>  
      
    {% block scripts %}{% endblock %}  
\</body\>  
\</html\>  
\`\`\`

\---

\#\# 🚀 Deployment Instructions

\#\#\# Production Checklist

1\. \*\*Environment Setup\*\*:  
\`\`\`bash  
export FLASK\_ENV=production  
export SECRET\_KEY=generate-strong-random-key  
\# Set all production environment variables  
\`\`\`

2\. \*\*Database Setup\*\*:  
\`\`\`bash  
createdb codecanyon\_prod  
flask db upgrade  
\`\`\`

3\. \*\*Static Files\*\*:  
\`\`\`bash  
\# If using compiled Tailwind  
npm run build:css  
\`\`\`

4\. \*\*Run with Gunicorn\*\*:  
\`\`\`bash  
gunicorn \-w 4 \-b 0.0.0.0:8000 "app:create\_app()"  
\`\`\`

5\. \*\*Start Celery\*\*:  
\`\`\`bash  
celery \-A celery\_worker.celery worker \-l info &  
celery \-A celery\_worker.celery beat \-l info &  
\`\`\`

6\. \*\*Nginx Configuration\*\*: (See main documentation)

\---

\#\# 📋 Testing Guide

\#\#\# Unit Test Example

\*\*File\*\*: \`tests/test\_analyzer.py\`  
\`\`\`python  
import pytest  
from app.services.analyzer import ProfitabilityAnalyzer  
from app.models import Product  
from datetime import datetime, timedelta

def test\_sales\_velocity\_calculation():  
    """Test sales velocity formula"""  
    analyzer \= ProfitabilityAnalyzer()  
      
    product \= Product(  
        total\_sales=1000,  
        launch\_date=datetime.now().date() \- timedelta(days=100)  
    )  
      
    velocity \= analyzer.calculate\_sales\_velocity(product)  
      
    \# (1000 / 100\) \* 100 \= 1000  
    assert velocity \== 1000.0

def test\_profitability\_score\_range():  
    """Ensure score is between 0-100"""  
    analyzer \= ProfitabilityAnalyzer()  
      
    product \= create\_mock\_product()  
    score \= analyzer.analyze(product.id)  
      
    assert 0 \<= score\['profitability\_score'\] \<= 100  
\`\`\`

\---

\#\# 🎯 Final Agent Instructions

\#\#\#Priority Implementation Order

\*\*Phase 1: Core Foundation\*\* (Week 1-2)  
1\. Set up project structure  
2\. Implement database models  
3\. Create base templates  
4\. Implement authentication

\*\*Phase 2: Core Features\*\* (Week 3-4)  
5\. Product search with filters  
6\. URL scraping (basic)  
7\. Profitability analysis  
8\. Product detail pages

\*\*Phase 3: Advanced Features\*\* (Week 5-6)  
9\. AI recommendations  
10\. Google search integration  
11\. Project planner wizard  
12\. Dashboard with analytics

\*\*Phase 4: Polish & Deploy\*\* (Week 7-8)  
13\. Rate limiting  
14\. Caching optimization  
15\. Error handling  
16\. Testing & deployment

\#\#\# Key Success Criteria

✅ All HTMX interactions work without full page reloads    
✅ Forms validate both client and server-side    
✅ Background jobs handle long-running tasks    
✅ Caching reduces duplicate calculations    
✅ Rate limiting prevents abuse    
✅ UI is responsive and accessible    
✅ Error messages are user-friendly    
✅ Database queries are optimized with indexes  

\#\#\# Common Pitfalls to Avoid

❌ Don't use localStorage (HTMX is server-side focused)    
❌ Don't forget CSRF tokens on forms    
❌ Don't skip input validation    
❌ Don't make synchronous API calls in request handlers    
❌ Don't forget to close database connections    
❌ Don't hard-code CSS selectors for scraping (use fallbacks)    
❌ Don't skip error handling in Celery tasks  

\---

\#\# 📞 Support & Resources

\- \*\*HTMX Docs\*\*: https://htmx.org/docs/  
\- \*\*Flask Docs\*\*: https://flask.palletsprojects.com/  
\- \*\*SQLAlchemy\*\*: https://docs.sqlalchemy.org/  
\- \*\*Celery\*\*: https://docs.celeryq.dev/  
\- \*\*Anthropic Claude API\*\*: https://docs.anthropic.com/

\---

\*\*This documentation is complete and ready for AI-assisted development. Begin with Phase 1 and proceed sequentially.\*\*

